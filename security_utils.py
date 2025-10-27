"""
Security utilities and audit tools for FibroHash password generator.
"""

import hashlib
import hmac
import secrets
import time
import logging
from typing import Dict, List, Optional, Tuple, Any
from collections import Counter
import re

class SecurityAuditor:
    """Security auditing and analysis tools for password generation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def audit_password_quality(self, password: str) -> Dict[str, Any]:
        """
        Comprehensive password quality audit.
        
        Args:
            password: Password to audit
            
        Returns:
            Dictionary containing detailed security analysis
        """
        audit_results = {
            'timestamp': time.time(),
            'password_length': len(password),
            'character_analysis': self._analyze_characters(password),
            'pattern_analysis': self._analyze_patterns(password),
            'entropy_analysis': self._analyze_entropy(password),
            'security_score': 0,
            'vulnerabilities': [],
            'recommendations': [],
            'compliance': self._check_compliance(password)
        }
        
        # Calculate overall security score
        audit_results['security_score'] = self._calculate_security_score(audit_results)
        
        # Generate recommendations
        audit_results['recommendations'] = self._generate_recommendations(audit_results)
        
        return audit_results
    
    def _analyze_characters(self, password: str) -> Dict[str, Any]:
        """Analyze character composition and distribution."""
        char_analysis = {
            'total_chars': len(password),
            'unique_chars': len(set(password)),
            'repetition_ratio': 1 - (len(set(password)) / len(password)) if password else 0,
            'char_types': {
                'uppercase': sum(1 for c in password if c.isupper()),
                'lowercase': sum(1 for c in password if c.islower()),
                'digits': sum(1 for c in password if c.isdigit()),
                'special': sum(1 for c in password if not c.isalnum()),
                'unicode': sum(1 for c in password if ord(c) > 127)
            },
            'char_frequency': dict(Counter(password)),
            'most_common_char': Counter(password).most_common(1)[0] if password else ('', 0)
        }
        
        # Calculate character diversity score
        char_types_used = sum(1 for count in char_analysis['char_types'].values() if count > 0)
        char_analysis['diversity_score'] = min(100, (char_types_used / 4) * 100)
        
        return char_analysis
    
    def _analyze_patterns(self, password: str) -> Dict[str, Any]:
        """Analyze password for common patterns and weaknesses."""
        patterns = {
            'sequential_chars': self._find_sequential_patterns(password),
            'repeated_substrings': self._find_repeated_substrings(password),
            'keyboard_patterns': self._find_keyboard_patterns(password),
            'dictionary_words': self._find_dictionary_patterns(password),
            'common_substitutions': self._find_substitution_patterns(password)
        }
        
        # Calculate pattern vulnerability score
        pattern_penalties = 0
        if patterns['sequential_chars']:
            pattern_penalties += 20
        if patterns['repeated_substrings']:
            pattern_penalties += 15
        if patterns['keyboard_patterns']:
            pattern_penalties += 25
        if patterns['dictionary_words']:
            pattern_penalties += 30
        
        patterns['vulnerability_score'] = min(100, pattern_penalties)
        
        return patterns
    
    def _analyze_entropy(self, password: str) -> Dict[str, float]:
        """Calculate various entropy metrics."""
        if not password:
            return {'shannon_entropy': 0.0, 'theoretical_entropy': 0.0, 'normalized_entropy': 0.0}
        
        # Shannon entropy
        char_counts = Counter(password)
        password_length = len(password)
        shannon_entropy = 0.0
        
        for count in char_counts.values():
            probability = count / password_length
            if probability > 0:
                import math
                shannon_entropy -= probability * math.log2(probability)
        
        # Theoretical entropy (assuming uniform distribution)
        charset_size = len(set(password))
        import math
        theoretical_entropy = password_length * math.log2(charset_size) if charset_size > 1 else 0
        
        # Normalized entropy (0-1 scale)
        max_possible_entropy = password_length * ((256).bit_length() - 1)  # Assuming 256 possible characters
        normalized_entropy = shannon_entropy / max_possible_entropy if max_possible_entropy > 0 else 0
        
        return {
            'shannon_entropy': shannon_entropy,
            'theoretical_entropy': theoretical_entropy,
            'normalized_entropy': normalized_entropy
        }
    
    def _find_sequential_patterns(self, password: str) -> List[str]:
        """Find sequential character patterns."""
        sequences = []
        for i in range(len(password) - 2):
            substring = password[i:i+3]
            if (ord(substring[1]) == ord(substring[0]) + 1 and 
                ord(substring[2]) == ord(substring[1]) + 1):
                sequences.append(substring)
        return sequences
    
    def _find_repeated_substrings(self, password: str) -> List[str]:
        """Find repeated substrings."""
        repeated = []
        for length in range(2, len(password) // 2 + 1):
            for i in range(len(password) - length + 1):
                substring = password[i:i+length]
                if password.count(substring) > 1 and substring not in repeated:
                    repeated.append(substring)
        return repeated
    
    def _find_keyboard_patterns(self, password: str) -> List[str]:
        """Find keyboard pattern sequences."""
        keyboard_rows = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm',
            '1234567890'
        ]
        
        patterns = []
        for row in keyboard_rows:
            for i in range(len(row) - 2):
                pattern = row[i:i+3]
                if pattern.lower() in password.lower():
                    patterns.append(pattern)
        
        return patterns
    
    def _find_dictionary_patterns(self, password: str) -> List[str]:
        """Find common dictionary words (simplified)."""
        common_words = [
            'password', 'admin', 'user', 'login', 'test', 'demo',
            'secret', 'key', 'access', 'secure', 'private', 'public'
        ]
        
        found_words = []
        password_lower = password.lower()
        for word in common_words:
            if word in password_lower:
                found_words.append(word)
        
        return found_words
    
    def _find_substitution_patterns(self, password: str) -> List[str]:
        """Find common character substitutions."""
        substitutions = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'
        }
        
        found_substitutions = []
        for original, substitute in substitutions.items():
            if substitute in password and original not in password.lower():
                found_substitutions.append(f"{original}->{substitute}")
        
        return found_substitutions
    
    def _check_compliance(self, password: str) -> Dict[str, bool]:
        """Check password compliance with various standards."""
        compliance = {
            'nist_basic': len(password) >= 8,
            'nist_enhanced': len(password) >= 14,
            'pci_dss': (len(password) >= 7 and 
                       any(c.isupper() for c in password) and
                       any(c.islower() for c in password) and
                       any(c.isdigit() for c in password)),
            'iso27001': (len(password) >= 8 and
                        sum(1 for c in password if c.isupper()) >= 1 and
                        sum(1 for c in password if c.islower()) >= 1 and
                        sum(1 for c in password if c.isdigit()) >= 1 and
                        sum(1 for c in password if not c.isalnum()) >= 1),
            'enterprise_minimum': len(password) >= 12
        }
        
        return compliance
    
    def _calculate_security_score(self, audit_results: Dict[str, Any]) -> int:
        """Calculate overall security score (0-100)."""
        score = 0
        
        # Length scoring (0-25 points)
        length = audit_results['password_length']
        if length >= 32:
            score += 25
        elif length >= 20:
            score += 20
        elif length >= 12:
            score += 15
        elif length >= 8:
            score += 10
        else:
            score += 5
        
        # Character diversity scoring (0-25 points)
        diversity_score = audit_results['character_analysis']['diversity_score']
        score += int(diversity_score * 0.25)
        
        # Entropy scoring (0-25 points)
        normalized_entropy = audit_results['entropy_analysis']['normalized_entropy']
        score += int(normalized_entropy * 25)
        
        # Pattern vulnerability penalty (0-25 points)
        pattern_vulnerability = audit_results['pattern_analysis']['vulnerability_score']
        score += max(0, 25 - int(pattern_vulnerability * 0.25))
        
        return min(100, max(0, score))
    
    def _generate_recommendations(self, audit_results: Dict[str, Any]) -> List[str]:
        """Generate security recommendations based on audit results."""
        recommendations = []
        
        # Length recommendations
        if audit_results['password_length'] < 12:
            recommendations.append("Increase password length to at least 12 characters")
        
        # Character diversity recommendations
        char_types = audit_results['character_analysis']['char_types']
        if char_types['uppercase'] == 0:
            recommendations.append("Add uppercase letters")
        if char_types['lowercase'] == 0:
            recommendations.append("Add lowercase letters")
        if char_types['digits'] == 0:
            recommendations.append("Add numeric digits")
        if char_types['special'] == 0:
            recommendations.append("Add special characters")
        
        # Pattern recommendations
        patterns = audit_results['pattern_analysis']
        if patterns['sequential_chars']:
            recommendations.append("Avoid sequential character patterns")
        if patterns['repeated_substrings']:
            recommendations.append("Reduce repeated substrings")
        if patterns['keyboard_patterns']:
            recommendations.append("Avoid keyboard patterns")
        if patterns['dictionary_words']:
            recommendations.append("Avoid common dictionary words")
        
        # Repetition recommendations
        repetition_ratio = audit_results['character_analysis']['repetition_ratio']
        if repetition_ratio > 0.3:
            recommendations.append("Reduce character repetition")
        
        return recommendations

class SecurePasswordValidator:
    """Validate passwords against security policies."""
    
    def __init__(self, policy: Optional[Dict[str, Any]] = None):
        self.policy = policy or self._default_policy()
        self.auditor = SecurityAuditor()
    
    def _default_policy(self) -> Dict[str, Any]:
        """Default security policy."""
        return {
            'min_length': 12,
            'max_length': 128,
            'require_uppercase': True,
            'require_lowercase': True,
            'require_digits': True,
            'require_special': True,
            'min_character_types': 3,
            'max_repetition_ratio': 0.3,
            'min_entropy_score': 60,
            'forbidden_patterns': ['password', '123456', 'qwerty'],
            'max_sequential_chars': 3
        }
    
    def validate(self, password: str) -> Tuple[bool, List[str]]:
        """
        Validate password against policy.
        
        Args:
            password: Password to validate
            
        Returns:
            Tuple of (is_valid, list_of_violations)
        """
        violations = []
        
        # Length checks
        if len(password) < self.policy['min_length']:
            violations.append(f"Password must be at least {self.policy['min_length']} characters")
        if len(password) > self.policy['max_length']:
            violations.append(f"Password must not exceed {self.policy['max_length']} characters")
        
        # Character type requirements
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        if self.policy['require_uppercase'] and not has_upper:
            violations.append("Password must contain uppercase letters")
        if self.policy['require_lowercase'] and not has_lower:
            violations.append("Password must contain lowercase letters")
        if self.policy['require_digits'] and not has_digit:
            violations.append("Password must contain digits")
        if self.policy['require_special'] and not has_special:
            violations.append("Password must contain special characters")
        
        # Character type diversity
        char_types = sum([has_upper, has_lower, has_digit, has_special])
        if char_types < self.policy['min_character_types']:
            violations.append(f"Password must use at least {self.policy['min_character_types']} character types")
        
        # Audit-based checks
        audit_results = self.auditor.audit_password_quality(password)
        
        # Repetition check
        repetition_ratio = audit_results['character_analysis']['repetition_ratio']
        if repetition_ratio > self.policy['max_repetition_ratio']:
            violations.append("Password has too much character repetition")
        
        # Entropy check
        if audit_results['security_score'] < self.policy['min_entropy_score']:
            violations.append(f"Password security score too low (minimum: {self.policy['min_entropy_score']})")
        
        # Forbidden patterns
        password_lower = password.lower()
        for pattern in self.policy['forbidden_patterns']:
            if pattern in password_lower:
                violations.append(f"Password contains forbidden pattern: {pattern}")
        
        # Sequential character check
        sequential_patterns = audit_results['pattern_analysis']['sequential_chars']
        if len(sequential_patterns) > 0:
            violations.append("Password contains sequential character patterns")
        
        return len(violations) == 0, violations

def generate_security_report(password: str, save_to_file: bool = True) -> Dict[str, Any]:
    """
    Generate comprehensive security report for a password.
    
    Args:
        password: Password to analyze
        save_to_file: Whether to save report to file
        
    Returns:
        Complete security analysis report
    """
    auditor = SecurityAuditor()
    validator = SecurePasswordValidator()
    
    # Perform audit
    audit_results = auditor.audit_password_quality(password)
    
    # Perform validation
    is_valid, violations = validator.validate(password)
    
    # Compile report
    report = {
        'timestamp': time.time(),
        'password_masked': password[:3] + '*' * (len(password) - 6) + password[-3:] if len(password) > 6 else '*' * len(password),
        'audit_results': audit_results,
        'validation_results': {
            'is_valid': is_valid,
            'violations': violations
        },
        'summary': {
            'overall_rating': _get_rating_from_score(audit_results['security_score']),
            'key_strengths': _identify_strengths(audit_results),
            'key_weaknesses': _identify_weaknesses(audit_results, violations),
            'compliance_status': audit_results['compliance']
        }
    }
    
    if save_to_file:
        filename = f"security_report_{int(time.time())}.json"
        import json
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        print(f"Security report saved to {filename}")
    
    return report

def _get_rating_from_score(score: int) -> str:
    """Convert numeric score to rating."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Fair"
    else:
        return "Poor"

def _identify_strengths(audit_results: Dict[str, Any]) -> List[str]:
    """Identify password strengths."""
    strengths = []
    
    if audit_results['password_length'] >= 16:
        strengths.append("Good length")
    
    if audit_results['character_analysis']['diversity_score'] >= 75:
        strengths.append("High character diversity")
    
    if audit_results['entropy_analysis']['normalized_entropy'] >= 0.7:
        strengths.append("High entropy")
    
    if not audit_results['pattern_analysis']['dictionary_words']:
        strengths.append("No common dictionary words")
    
    if audit_results['character_analysis']['repetition_ratio'] < 0.2:
        strengths.append("Low character repetition")
    
    return strengths

def _identify_weaknesses(audit_results: Dict[str, Any], violations: List[str]) -> List[str]:
    """Identify password weaknesses."""
    weaknesses = []
    
    if violations:
        weaknesses.extend(violations)
    
    if audit_results['pattern_analysis']['sequential_chars']:
        weaknesses.append("Contains sequential patterns")
    
    if audit_results['pattern_analysis']['keyboard_patterns']:
        weaknesses.append("Contains keyboard patterns")
    
    if audit_results['character_analysis']['repetition_ratio'] > 0.4:
        weaknesses.append("High character repetition")
    
    return weaknesses

if __name__ == "__main__":
    # Example usage
    test_password = "TestPassword123!"
    report = generate_security_report(test_password)
    print(f"Security report generated for test password")
    print(f"Overall rating: {report['summary']['overall_rating']}")
    print(f"Security score: {report['audit_results']['security_score']}/100")