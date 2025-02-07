import math
import logging
from main import generate_password  # Make sure this is your actual function import path

# Set up logging to record test results
logging.basicConfig(filename="password_generation_results.log", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

def calculate_entropy(password):
    """
    Calculate the entropy of the password.
    Entropy = log2(Number of possible password combinations)
    """
    charset_size = len('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?{}[]|')
    password_length = len(password)
    possible_combinations = charset_size ** password_length
    return math.log2(possible_combinations)

def test_password_strength(user_input):
    """
    Generate a password and test its strength.
    Log the results to a file.
    """
    # Generate a password using the password generator function
    password = generate_password(user_input)
    
    # Test password length
    password_length = len(password)
    
    # Calculate the entropy of the password
    entropy = calculate_entropy(password)
    
    # Assess password strength based on entropy
    if entropy < 40:
        strength = "Very Weak"
    elif entropy < 60:
        strength = "Weak"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    # Log the results in a structured way
    logging.info(f"User Input: {user_input}")
    logging.info(f"Generated Password: {password}")
    logging.info(f"Password Length: {password_length} characters")
    logging.info(f"Password Entropy: {entropy:.2f} bits")
    logging.info(f"Password Strength: {strength}\n")

if __name__ == "__main__":
    # Expanded list of test phrases for more comprehensive testing
    test_phrases = [
        "es",
        "key",
        "brin",
        "1",
        "l",
        "Secure123",      
          "hey" ,        # Basic phrase with numbers
        "Hed!",               # Common phrase with special character
        "ComplexPassword@2025",      # Complex password with special characters and numbers
        "mysecurephrase",            # Simple but strong phrase
        "password123!",              # Simple password with numbers and a symbol
        "P@ssw0rd2025",              # Password with special characters, numbers, and mixed case
        "QwErTy!@#1",                # Mixed case with symbols
        "abcdefgH!3jkL12@",         # Mixed letters and numbers with a special symbol
        "Sunshine2025$$",            # Word with numbers and special symbols
        "T3st1ngGener@t0r",          # Mixed case and symbols with numbers
        "C0mpLex!2025_Pass",         # Uppercase, lowercase, numbers, and symbols
        "QwertyUIOp@12345",          # Common word with numbers and symbols
        "SimplePassword2025",        # Simple password with numbers
        "ThisIsASecurePassword!",    # Longer phrase with uppercase, lowercase, and symbols
        "12345abcdeABCDE!",          # Numbers mixed with letters and a symbol
        "!@#2025$%^",                # Special characters and numbers only
        "passw0rD!#3456789",         # Mixed case, numbers, and special characters
        "TheQ#G34Kw0R1#Password",    # Complex mixed case with symbols and numbers
        "data!5ENcryptX@ssion42",    # A mix of uppercase, numbers, special characters, and meaningful phrase
        "time2Sh1ne#WithU$3",        # Random mix of letters, numbers, and special symbols
        "BeStrong&Keep@Moving2025!"   # Phrase with numbers and symbols that could relate to motivation
    ]
    
    # Run the tests and log the results
    for phrase in test_phrases:
        test_password_strength(phrase)

    print("Password strength testing complete. Check 'password_generation_results.log' for details.")
