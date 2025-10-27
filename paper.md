---
title: 'FibroHash: A Cryptographically Secure Password Generation Framework for System Administration'
tags:
  - Python
  - cryptography
  - password generation
  - security
  - system administration
  - PBKDF2
  - entropy analysis
authors:
  - name: Spyros Lefkaditis
    orcid: 0009-0000-8432-4667
    equal-contrib: true
    affiliation: "1"
affiliations:
 - name: Independent Researcher
   index: 1
date: 27 October 2025
bibliography: paper.bib
---

# Summary

FibroHash is an enterprise-grade, cryptographically secure password generation framework designed specifically for system administrators and security professionals. Unlike traditional password generators that rely on simple randomization, FibroHash implements a novel multi-layered cryptographic approach combining PBKDF2 key derivation, HMAC-based entropy generation, and Fibonacci-inspired algorithmic patterns to produce passwords with guaranteed entropy levels exceeding 190 bits.

The framework addresses critical security gaps in existing password generation tools by implementing proper cryptographic salt handling, resistance to timing attacks, and compliance with modern security standards including NIST SP 800-63B [@nist2017digital], PCI DSS, and ISO/IEC 27001. FibroHash operates entirely offline using only Python's standard library, ensuring no external dependencies or network communications that could compromise security.

# Statement of need

System administrators and security professionals require password generation tools that provide both high entropy and reproducible security analysis. Existing solutions often suffer from predictable patterns, insufficient entropy, or lack proper cryptographic foundations. Recent research on password behavior through persuasion techniques [@paudel2024priming] demonstrates the importance of user-centered approaches to secure password creation. Many tools also require external dependencies or network connectivity, introducing potential security vulnerabilities, while contemporary studies on password manager adoption [@tian2025unraveling] reveal ongoing challenges in organizational credential management practices. Recent analysis of password hashing methods using CSPRNG and PBKDF2 [@mustafa2024analysis] demonstrates the critical importance of implementing proper cryptographic foundations in password generation tools.

FibroHash addresses these limitations by providing:

1. **Cryptographic Security**: Implementation of PBKDF2-HMAC-SHA256 with configurable iterations (1,000-10,000) following NIST SP 800-63B guidelines [@nist2017digital] ensuring resistance to rainbow table and brute-force attacks
2. **Entropy Verification**: Built-in entropy analysis tools providing Shannon entropy calculations and character distribution analysis
3. **Compliance Framework**: Automated validation against industry security standards with detailed audit reporting
4. **Research Reproducibility**: Comprehensive test suite enabling security researchers to validate and extend the cryptographic methodology

The framework has been designed with system administrators in mind, providing both command-line interfaces for operational use and programmatic APIs for integration into larger security frameworks.

# Research Contribution and Methodology

FibroHash introduces an approach to password generation that combines mathematical sequence generation with modern cryptographic primitives [@nist2017digital]. The key contribution lies in the use of HMAC-based Fibonacci-inspired number generation, which provides the benefits of mathematical predictability for testing while maintaining cryptographic security through proper PBKDF2 key derivation.

## Cryptographic Architecture

The password generation process follows a multi-stage cryptographic pipeline:

1. **Input Processing**: User phrases undergo validation and sanitization to prevent injection attacks
2. **Key Derivation**: PBKDF2-HMAC-SHA256 transforms user input and cryptographic salt into derived keys
3. **Entropy Generation**: Multiple entropy sources including HMAC-based sequence generation and secure random number generation
4. **Character Encoding**: Secure base conversion using extended character sets with 90+ characters
5. **Quality Assurance**: Automated validation of character diversity and entropy levels

## Security Analysis

The framework provides theoretical entropy levels of 192+ bits for 32-character passwords using a 90-character alphabet. Security analysis includes:

- **Timing Attack Resistance**: Consistent operation times regardless of input characteristics
- **Salt Uniqueness**: Cryptographically secure salt generation for each password instance
- **Pattern Avoidance**: Detection and mitigation of sequential, keyboard, and dictionary patterns

## Validation Framework

FibroHash includes a comprehensive validation framework enabling reproducible security research:

```python
from main import generate_password
from security_utils import generate_security_report

# Generate cryptographically secure password
password = generate_password("research phrase", 32, "maximum")

# Perform comprehensive security analysis
report = generate_security_report(password)
print(f"Entropy: {report['audit_results']['entropy_analysis']['theoretical_entropy']} bits")
print(f"Security Score: {report['audit_results']['security_score']}/100")
```

# Examples

## Basic Usage

```python
from main import generate_password

# Generate password with default settings (32 chars, high security)
password = generate_password("secure research phrase")

# Generate with custom parameters
password = generate_password("phrase", password_length=24, security_level="maximum")
```

## Security Analysis

```python
from security_utils import SecurityAuditor, SecurePasswordValidator

auditor = SecurityAuditor()
validator = SecurePasswordValidator()

# Comprehensive security audit
audit_results = auditor.audit_password_quality(password)

# Policy validation
is_valid, violations = validator.validate(password)
```

## Configuration and Testing

```bash
# Setup and configuration
python3 setup.sh

# Run comprehensive security test suite
python3 test.py

# Interactive password generation
./init.sh
```

# Impact and Applications

FibroHash has applications in:

- **System Administration**: Secure password generation for server and service accounts
- **Security Research**: Reproducible password security analysis and entropy validation
- **Compliance Auditing**: Automated validation against security standards
- **Educational Use**: Teaching cryptographic principles and password security

The framework's emphasis on reproducible security analysis makes it particularly valuable for security researchers studying password generation algorithms and entropy analysis techniques.

# Acknowledgements

The author acknowledges the Python cryptography community for establishing secure cryptographic practices and the NIST Cybersecurity Framework for providing security standards guidance.

# References