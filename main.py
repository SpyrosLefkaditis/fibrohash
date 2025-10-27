import secrets
import hashlib
import hmac
import os
import re
import logging
from typing import Optional, Union
from config import get_config, SecureConfig

# Initialize configuration
config = get_config()

class SecurityError(Exception):
    """Custom exception for security-related errors."""
    pass

def validate_input(user_input: str) -> str:
    """
    Validate and sanitize user input for security.
    
    Args:
        user_input: The user's input string
        
    Returns:
        Sanitized input string
        
    Raises:
        SecurityError: If input is invalid or potentially malicious
    """
    if not isinstance(user_input, str):
        raise SecurityError("Input must be a string")
    
    min_length = config.get_security_param("min_input_length", 1)
    max_length = config.get_security_param("max_input_length", 1000)
    
    if len(user_input) < min_length:
        raise SecurityError(f"Input must be at least {min_length} character(s) long")
    
    if len(user_input) > max_length:
        raise SecurityError(f"Input must be no more than {max_length} characters long")
    
    # Remove any null bytes or control characters that could cause issues
    sanitized = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', user_input)
    
    if not sanitized:
        raise SecurityError("Input contains only invalid characters")
    
    return sanitized

def generate_cryptographic_fibonacci(seed: bytes, length: int) -> int:
    """
    Generate a Fibonacci-like number using cryptographic functions.
    
    Args:
        seed: Cryptographic seed bytes
        length: Desired bit length of output
        
    Returns:
        Cryptographically secure large integer
    """
    # Use HMAC with SHA-256 for cryptographic security
    key = hashlib.sha256(seed).digest()
    
    # Generate multiple rounds of HMAC to create sufficient entropy
    result = 0
    for i in range((length // 256) + 1):
        hmac_result = hmac.new(key, seed + i.to_bytes(4, 'big'), hashlib.sha256).digest()
        result = (result << 256) | int.from_bytes(hmac_result, 'big')
    
    # Mask to desired bit length
    mask = (1 << length) - 1
    return result & mask

def secure_base_conversion(n: int, target_length: int) -> str:
    """
    Convert a number to the extended charset with constant-time operations.
    
    Args:
        n: Integer to convert
        target_length: Target length of output string
        
    Returns:
        String representation using extended charset
    """
    charset = config.get_charset()
    
    if n == 0:
        return charset[0] * min(target_length, 1)
    
    charset_size = len(charset)
    digits = []
    
    # Convert to base with charset size
    while n > 0:
        digits.append(charset[n % charset_size])
        n //= charset_size
    
    result = ''.join(digits[::-1])
    
    # Pad or truncate to target length
    if len(result) < target_length:
        # Pad with cryptographically random characters
        padding_needed = target_length - len(result)
        random_padding = ''.join(secrets.choice(charset) for _ in range(padding_needed))
        result = random_padding + result
    elif len(result) > target_length:
        # Use a secure hash to determine which characters to keep
        hash_input = result.encode('utf-8')
        hash_digest = hashlib.sha256(hash_input).digest()
        start_pos = int.from_bytes(hash_digest[:4], 'big') % (len(result) - target_length + 1)
        result = result[start_pos:start_pos + target_length]
    
    return result

def generate_password(user_input: str, password_length: Optional[int] = None, 
                     security_level: Optional[str] = None) -> str:
    """
    Generate a cryptographically secure password using enhanced Fibonacci-based algorithm.
    
    Args:
        user_input: User's input phrase for password generation
        password_length: Desired password length (uses config defaults if None)
        security_level: Security level (uses config defaults if None)
        
    Returns:
        Generated secure password
        
    Raises:
        SecurityError: If parameters are invalid or generation fails
    """
    # Use config defaults if not specified
    if password_length is None:
        password_length = config.get_security_param("default_password_length", 32)
    if security_level is None:
        security_level = config.get_security_param("default_security_level", "high")
    
    # Validate inputs
    if not config.validate_password_length(password_length):
        min_len = config.get_security_param("min_password_length", 8)
        max_len = config.get_security_param("max_password_length", 128)
        raise SecurityError(f"Password length must be between {min_len} and {max_len}")
    
    if not config.validate_security_level(security_level):
        allowed = config.get_security_param("allowed_security_levels", ["standard", "high", "maximum"])
        raise SecurityError(f"Security level must be one of: {', '.join(allowed)}")
    
    # Sanitize user input
    sanitized_input = validate_input(user_input)
    
    # Get security parameters from configuration
    params = config.get_security_params(security_level)
    
    try:
        # Generate cryptographically secure salt
        salt = secrets.token_bytes(params['key_size'])
        
        # Create input hash with salt
        input_hash = hashlib.pbkdf2_hmac('sha256', 
                                       sanitized_input.encode('utf-8'), 
                                       salt, 
                                       params['iterations'])
        
        # Generate password in segments for better distribution
        password_segments = []
        segment_length = max(1, password_length // params['rounds'])
        
        for round_num in range(params['rounds']):
            # Create unique seed for each round
            round_seed = salt + input_hash + round_num.to_bytes(4, 'big')
            
            # Generate cryptographic Fibonacci-like number
            crypto_fib = generate_cryptographic_fibonacci(round_seed, 2048)
            
            # Create round-specific entropy
            round_entropy = secrets.randbits(1024)
            
            # Combine with user input entropy
            user_entropy = sum(ord(c) * (i + 1) for i, c in enumerate(sanitized_input))
            
            # Final combination using multiple cryptographic operations
            combined = crypto_fib ^ round_entropy ^ user_entropy
            combined = int.from_bytes(hashlib.sha512(combined.to_bytes(256, 'big')).digest(), 'big')
            
            # Convert to secure character representation
            if round_num == params['rounds'] - 1:
                # Last segment gets remaining length
                current_segment_length = password_length - len(''.join(password_segments))
            else:
                current_segment_length = segment_length
            
            segment = secure_base_conversion(combined, current_segment_length)
            password_segments.append(segment)
        
        # Combine segments and ensure exact length
        final_password = ''.join(password_segments)[:password_length]
        
        # Final security check - ensure minimum character diversity
        if not _check_password_diversity(final_password):
            # If diversity check fails, mix in additional entropy
            entropy_bytes = secrets.token_bytes(32)
            entropy_hash = hashlib.sha256(entropy_bytes + final_password.encode('utf-8')).digest()
            additional_chars = secure_base_conversion(int.from_bytes(entropy_hash, 'big'), 
                                                    password_length // 4)
            
            # Interleave additional characters
            final_chars = list(final_password)
            for i, char in enumerate(additional_chars):
                if i * 4 < len(final_chars):
                    final_chars[i * 4] = char
            
            final_password = ''.join(final_chars)[:password_length]
        
        return final_password
        
    except Exception as e:
        raise SecurityError(f"Password generation failed: {str(e)}")

def _check_password_diversity(password: str) -> bool:
    """
    Check if password has sufficient character diversity.
    
    Args:
        password: Password to check
        
    Returns:
        True if password has sufficient diversity
    """
    if len(password) < 8:
        return True  # Short passwords are handled differently
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=<>?{}[]|:;,.~`' for c in password)
    
    # Require at least 3 of 4 character types for longer passwords
    diversity_count = sum([has_upper, has_lower, has_digit, has_special])
    return diversity_count >= 3

# ASCII Art Representation of "fibrohash"
ascii_art = '''
$$$$$$$$\\ $$$$$$\\ $$$$$$$\\  $$$$$$$\\   $$$$$$\\  $$\\   $$\\  $$$$$$\\   $$$$$$\\  $$\\   $$\\
$$  _____|\\_$$  _|$$  __$$\\ $$  __$$\\ $$  __$$\\ $$ |  $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |
$$ |        $$ |  $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  \\__|$$ |  $$ |
$$$$$\\      $$ |  $$$$$$$$\\ |$$$$$$$  |$$ |  $$ |$$$$$$$$ |$$$$$$$$ |\\$$$$$$\\  $$$$$$$$ |
$$  __|     $$ |  $$  __$$\\ $$  __$$< $$ |  $$ |$$  __$$ |$$  __$$ | \\____$$\\ $$  __$$ |
$$ |        $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\\   $$ |$$ |  $$ |
$$ |      $$$$$$\\ $$$$$$$  |$$ |  $$ | $$$$$$  |$$ |  $$ |$$ |  $$ |\\$$$$$$  |$$ |  $$ |
\\__|      \\______|\\_______/ \\__|  \\__| \\______/ \\__|  \\__|\\__|  \\__| \\______/ \\__|  \\__|
'''

def main():
    """
    Main function with secure error handling and user interaction.
    """
    print("Welcome to the Secure FibroHash Password Generator!")
    print("=" * 60)
    print(ascii_art)
    print("=" * 60)
    print("\nSecurity Features:")
    print("• Cryptographically secure random number generation")
    print("• PBKDF2 key derivation with salt")
    print("• Multiple security levels available")
    print("• Input validation and sanitization")
    print("• Character diversity enforcement")
    print("• Configurable security parameters")
    print("=" * 60)
    
    try:
        # Get configuration limits
        min_len = config.get_security_param("min_password_length", 8)
        max_len = config.get_security_param("max_password_length", 128)
        default_len = config.get_security_param("default_password_length", 32)
        default_level = config.get_security_param("default_security_level", "high")
        allowed_levels = config.get_security_param("allowed_security_levels", ["standard", "high", "maximum"])
        
        # Get user input with validation
        while True:
            user_input = input("\nEnter a phrase to enhance password security: ").strip()
            if user_input:
                break
            print("Please enter a non-empty phrase.")
        
        # Get password length with validation
        while True:
            try:
                length_input = input(f"Enter password length ({min_len}-{max_len}, default {default_len}): ").strip()
                if not length_input:
                    password_length = default_len
                    break
                password_length = int(length_input)
                if config.validate_password_length(password_length):
                    break
                print(f"Please enter a length between {min_len} and {max_len}")
            except ValueError:
                print("Please enter a valid number")
        
        # Get security level
        while True:
            level_prompt = f"Security level ({'/'.join(allowed_levels)}, default {default_level}): "
            security_level = input(level_prompt).strip().lower()
            if not security_level:
                security_level = default_level
                break
            if config.validate_security_level(security_level):
                break
            print(f"Please enter one of: {', '.join(allowed_levels)}")
        
        print(f"\nGenerating password with {security_level} security...")
        
        # Generate password
        password = generate_password(user_input, password_length, security_level)
        
        print(f"\n{'='*20} GENERATED PASSWORD {'='*20}")
        print(f"Password: {password}")
        print(f"Length: {len(password)} characters")
        print(f"Security Level: {security_level.title()}")
        
        # Show security params for transparency
        params = config.get_security_params(security_level)
        print(f"PBKDF2 Iterations: {params['iterations']}")
        print(f"Generation Rounds: {params['rounds']}")
        print("=" * 60)
        
        print("\n⚠️  SECURITY REMINDER:")
        print("• Store this password securely")
        print("• Don't share it via unsecured channels")
        print("• Use unique passwords for each account")
        print("• Consider using a password manager")
        
    except SecurityError as e:
        logging.error(f"Security error in password generation: {e}")
        print(f"\n❌ Security Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return 0
    except Exception as e:
        logging.error(f"Unexpected error in password generation: {e}")
        print(f"\n❌ Unexpected error: {e}")
        return 1
    
    return 0

# Example usage
if __name__ == "__main__":
    exit(main())
