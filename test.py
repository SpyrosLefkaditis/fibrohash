import math
import logging
import time
import hashlib
import statistics
from collections import Counter
from typing import List, Dict, Tuple
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import generate_password, SecurityError
from config import get_config

# Set up comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("password_security_test.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def calculate_theoretical_entropy(password: str) -> float:
    """
    Calculate the theoretical entropy of the password.
    Entropy = log2(Number of possible password combinations)
    """
    config = get_config()
    charset = config.get_charset()
    charset_size = len(charset)
    password_length = len(password)
    possible_combinations = charset_size ** password_length
    return math.log2(possible_combinations)

def calculate_actual_entropy(password: str) -> float:
    """
    Calculate actual entropy based on character frequency distribution.
    """
    if not password:
        return 0.0
    
    # Count character frequencies
    char_counts = Counter(password)
    password_length = len(password)
    
    # Calculate Shannon entropy
    entropy = 0.0
    for count in char_counts.values():
        probability = count / password_length
        if probability > 0:
            entropy -= probability * math.log2(probability)
    
    return entropy * password_length

def analyze_character_distribution(password: str) -> Dict[str, int]:
    """
    Analyze character type distribution in password.
    """
    analysis = {
        'uppercase': 0,
        'lowercase': 0,
        'digits': 0,
        'special': 0,
        'unique_chars': 0
    }
    
    unique_chars = set()
    for char in password:
        unique_chars.add(char)
        if char.isupper():
            analysis['uppercase'] += 1
        elif char.islower():
            analysis['lowercase'] += 1
        elif char.isdigit():
            analysis['digits'] += 1
        else:
            analysis['special'] += 1
    
    analysis['unique_chars'] = len(unique_chars)
    return analysis

def test_password_uniqueness(user_input: str, iterations: int = 100) -> Tuple[int, List[str]]:
    """
    Test password uniqueness by generating multiple passwords with same input.
    """
    passwords = set()
    password_list = []
    
    for _ in range(iterations):
        password = generate_password(user_input)
        passwords.add(password)
        password_list.append(password)
    
    return len(passwords), password_list

def test_timing_attack_resistance(test_inputs: List[str], iterations: int = 10) -> Dict[str, float]:
    """
    Test for timing attack resistance by measuring generation times.
    """
    timing_results = {}
    
    for input_text in test_inputs:
        times = []
        for _ in range(iterations):
            start_time = time.perf_counter()
            generate_password(input_text)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        
        avg_time = statistics.mean(times)
        std_dev = statistics.stdev(times) if len(times) > 1 else 0
        timing_results[input_text] = {
            'avg_time': avg_time,
            'std_dev': std_dev,
            'coefficient_of_variation': std_dev / avg_time if avg_time > 0 else 0
        }
    
    return timing_results

def test_security_levels() -> Dict[str, Dict]:
    """
    Test all security levels for consistency and strength.
    """
    test_input = "security_level_test"
    results = {}
    
    for level in ['standard', 'high', 'maximum']:
        try:
            start_time = time.perf_counter()
            password = generate_password(test_input, 32, level)
            generation_time = time.perf_counter() - start_time
            
            results[level] = {
                'password': password,
                'length': len(password),
                'theoretical_entropy': calculate_theoretical_entropy(password),
                'actual_entropy': calculate_actual_entropy(password),
                'character_analysis': analyze_character_distribution(password),
                'generation_time': generation_time
            }
        except Exception as e:
            results[level] = {'error': str(e)}
    
    return results

def comprehensive_password_test(user_input: str, security_level: str = 'high') -> Dict:
    """
    Perform comprehensive testing of password generation and security.
    """
    try:
        # Generate password
        start_time = time.perf_counter()
        password = generate_password(user_input, security_level=security_level)
        generation_time = time.perf_counter() - start_time
        
        # Calculate entropy metrics
        theoretical_entropy = calculate_theoretical_entropy(password)
        actual_entropy = calculate_actual_entropy(password)
        
        # Analyze character distribution
        char_analysis = analyze_character_distribution(password)
        
        # Test uniqueness
        unique_count, _ = test_password_uniqueness(user_input, 20)
        uniqueness_ratio = unique_count / 20
        
        # Assess strength based on multiple factors
        strength_score = 0
        strength_factors = []
        
        # Entropy-based scoring
        if theoretical_entropy >= 160:
            strength_score += 30
            strength_factors.append("Excellent theoretical entropy")
        elif theoretical_entropy >= 120:
            strength_score += 25
            strength_factors.append("Good theoretical entropy")
        elif theoretical_entropy >= 80:
            strength_score += 20
            strength_factors.append("Moderate theoretical entropy")
        else:
            strength_score += 10
            strength_factors.append("Low theoretical entropy")
        
        # Character diversity scoring
        char_types = sum(1 for count in [char_analysis['uppercase'], char_analysis['lowercase'], 
                                       char_analysis['digits'], char_analysis['special']] 
                        if count > 0)
        
        if char_types >= 4:
            strength_score += 25
            strength_factors.append("Excellent character diversity")
        elif char_types >= 3:
            strength_score += 20
            strength_factors.append("Good character diversity")
        elif char_types >= 2:
            strength_score += 15
            strength_factors.append("Moderate character diversity")
        else:
            strength_score += 5
            strength_factors.append("Limited character diversity")
        
        # Uniqueness scoring
        if uniqueness_ratio >= 0.95:
            strength_score += 25
            strength_factors.append("Excellent uniqueness")
        elif uniqueness_ratio >= 0.85:
            strength_score += 20
            strength_factors.append("Good uniqueness")
        elif uniqueness_ratio >= 0.70:
            strength_score += 15
            strength_factors.append("Moderate uniqueness")
        else:
            strength_score += 10
            strength_factors.append("Low uniqueness")
        
        # Length scoring
        if len(password) >= 32:
            strength_score += 20
            strength_factors.append("Excellent length")
        elif len(password) >= 20:
            strength_score += 15
            strength_factors.append("Good length")
        elif len(password) >= 12:
            strength_score += 10
            strength_factors.append("Adequate length")
        else:
            strength_score += 5
            strength_factors.append("Short length")
        
        # Overall strength assessment
        if strength_score >= 90:
            overall_strength = "Excellent"
        elif strength_score >= 75:
            overall_strength = "Very Strong"
        elif strength_score >= 60:
            overall_strength = "Strong"
        elif strength_score >= 45:
            overall_strength = "Moderate"
        else:
            overall_strength = "Weak"
        
        results = {
            'input': user_input,
            'password': password,
            'security_level': security_level,
            'length': len(password),
            'generation_time': generation_time,
            'theoretical_entropy': theoretical_entropy,
            'actual_entropy': actual_entropy,
            'character_analysis': char_analysis,
            'uniqueness_ratio': uniqueness_ratio,
            'strength_score': strength_score,
            'overall_strength': overall_strength,
            'strength_factors': strength_factors,
            'passed_tests': []
        }
        
        # Additional security tests
        results['passed_tests'].append("Generation successful")
        
        if uniqueness_ratio >= 0.8:
            results['passed_tests'].append("High uniqueness")
        
        if char_types >= 3:
            results['passed_tests'].append("Character diversity")
        
        if theoretical_entropy >= 80:
            results['passed_tests'].append("Sufficient entropy")
        
        return results
        
    except Exception as e:
        return {
            'input': user_input,
            'error': str(e),
            'security_level': security_level,
            'passed_tests': [],
            'overall_strength': 'Error'
        }

def run_security_test_suite():
    """
    Run comprehensive security test suite.
    """
    logger.info("Starting FibroHash Security Test Suite")
    logger.info("=" * 60)
    
    # Test phrases with varying complexity
    test_phrases = [
        # Short inputs
        "a", "ab", "abc",
        # Medium inputs
        "test", "hello", "secure",
        # Complex inputs
        "Secure123", "ComplexPassword@2025", "P@ssw0rd2025",
        # Special cases
        "!@#$%^&*()", "1234567890", "ABCDEFGHIJK",
        # Real-world scenarios
        "mysecurephrase", "ThisIsASecurePassword!",
        "data!5ENcryptX@ssion42", "BeStrong&Keep@Moving2025!"
    ]
    
    # Test results storage
    all_results = []
    security_level_results = {}
    
    # Test individual passwords
    logger.info("Testing individual password generation...")
    for phrase in test_phrases:
        logger.info(f"\nTesting phrase: '{phrase}'")
        result = comprehensive_password_test(phrase)
        all_results.append(result)
        
        if 'error' not in result:
            logger.info(f"Password: {result['password']}")
            logger.info(f"Length: {result['length']}")
            logger.info(f"Strength: {result['overall_strength']} (Score: {result['strength_score']}/100)")
            logger.info(f"Theoretical Entropy: {result['theoretical_entropy']:.2f} bits")
            logger.info(f"Character Types: {sum(1 for x in result['character_analysis'].values() if x > 0 and x != result['character_analysis']['unique_chars'])}")
            logger.info(f"Uniqueness: {result['uniqueness_ratio']:.2%}")
        else:
            logger.error(f"Error: {result['error']}")
    
    # Test security levels
    logger.info("\n" + "=" * 60)
    logger.info("Testing security levels...")
    security_level_results = test_security_levels()
    
    for level, result in security_level_results.items():
        logger.info(f"\nSecurity Level: {level.upper()}")
        if 'error' not in result:
            logger.info(f"Password: {result['password']}")
            logger.info(f"Generation Time: {result['generation_time']:.4f}s")
            logger.info(f"Theoretical Entropy: {result['theoretical_entropy']:.2f} bits")
            logger.info(f"Character Analysis: {result['character_analysis']}")
        else:
            logger.error(f"Error: {result['error']}")
    
    # Test timing attack resistance
    logger.info("\n" + "=" * 60)
    logger.info("Testing timing attack resistance...")
    timing_test_inputs = ["short", "mediumlength", "verylonginputfortimingtests"]
    timing_results = test_timing_attack_resistance(timing_test_inputs)
    
    for input_text, result in timing_results.items():
        logger.info(f"Input: '{input_text}'")
        logger.info(f"  Average time: {result['avg_time']:.4f}s")
        logger.info(f"  Std deviation: {result['std_dev']:.4f}s")
        logger.info(f"  Coefficient of variation: {result['coefficient_of_variation']:.3f}")
    
    # Edge case tests
    logger.info("\n" + "=" * 60)
    logger.info("Testing edge cases...")
    
    edge_cases = [
        ("", "Empty input"),
        ("x" * 1001, "Very long input"),
        ("тест", "Unicode input"),
        ("test\x00test", "Null byte input"),
        ("test\ntest", "Newline input")
    ]
    
    for test_input, description in edge_cases:
        logger.info(f"\nTesting {description}:")
        try:
            result = generate_password(test_input)
            logger.info(f"SUCCESS - Password generated (length: {len(result)})")
        except SecurityError as e:
            logger.info(f"EXPECTED ERROR - {e}")
        except Exception as e:
            logger.error(f"UNEXPECTED ERROR - {e}")
    
    # Generate summary statistics
    logger.info("\n" + "=" * 60)
    logger.info("TEST SUMMARY")
    logger.info("=" * 60)
    
    successful_tests = [r for r in all_results if 'error' not in r]
    failed_tests = [r for r in all_results if 'error' in r]
    
    if successful_tests:
        avg_entropy = statistics.mean(r['theoretical_entropy'] for r in successful_tests)
        avg_strength_score = statistics.mean(r['strength_score'] for r in successful_tests)
        avg_generation_time = statistics.mean(r['generation_time'] for r in successful_tests)
        
        strength_distribution = Counter(r['overall_strength'] for r in successful_tests)
        
        logger.info(f"Successful tests: {len(successful_tests)}/{len(all_results)}")
        logger.info(f"Failed tests: {len(failed_tests)}")
        logger.info(f"Average theoretical entropy: {avg_entropy:.2f} bits")
        logger.info(f"Average strength score: {avg_strength_score:.1f}/100")
        logger.info(f"Average generation time: {avg_generation_time:.4f}s")
        logger.info(f"Strength distribution: {dict(strength_distribution)}")
        
        # Security assessment
        high_security_count = sum(1 for r in successful_tests if r['strength_score'] >= 75)
        security_ratio = high_security_count / len(successful_tests)
        
        logger.info(f"\nSECURITY ASSESSMENT:")
        logger.info(f"High security passwords: {high_security_count}/{len(successful_tests)} ({security_ratio:.1%})")
        
        if security_ratio >= 0.9:
            logger.info("✅ EXCELLENT - Generator produces consistently strong passwords")
        elif security_ratio >= 0.7:
            logger.info("✅ GOOD - Generator produces mostly strong passwords")
        elif security_ratio >= 0.5:
            logger.info("⚠️  MODERATE - Generator needs improvement")
        else:
            logger.info("❌ POOR - Generator has significant security issues")
    
    logger.info("\n" + "=" * 60)
    logger.info("Security test suite completed!")
    logger.info("Detailed results saved to password_security_test.log")

if __name__ == "__main__":
    try:
        run_security_test_suite()
    except Exception as e:
        logger.error(f"Test suite failed with error: {e}")
        sys.exit(1)
