


# FibroHash: Cryptographically Secure Password Generation Framework

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Audit](https://img.shields.io/badge/security-audited-green.svg)](https://github.com/SpyrosLefkaditis/fibrohash)
[![JOSS Status](https://img.shields.io/badge/JOSS-under%20review-orange.svg)](https://joss.theoj.org/)

FibroHash is a research-focused, cryptographically secure password generation framework designed for system administrators and security professionals. It implements a novel multi-layered approach combining PBKDF2 key derivation, HMAC-based entropy generation, and Fibonacci-inspired algorithms to produce passwords with guaranteed entropy levels exceeding 190 bits.

## Research Applications

- **System Administration**: Secure password generation for enterprise environments
- **Security Research**: Reproducible password security analysis and entropy validation
- **Compliance Auditing**: Automated validation against NIST, PCI DSS, and ISO standards
- **Cryptographic Education**: Teaching modern password security and entropy analysis

## Key Features

- **🔐 Cryptographic Security**: PBKDF2-HMAC-SHA256 with 1,000-10,000 configurable iterations
- **📊 Entropy Analysis**: Built-in Shannon entropy calculation and character distribution analysis
- **✅ Standards Compliance**: NIST SP 800-63B, PCI DSS, ISO/IEC 27001 validation
- **🔬 Research Tools**: Comprehensive security auditing and reproducible testing framework
- **📱 Zero Dependencies**: Uses only Python standard library for maximum security
- **🌐 Offline Operation**: No network communication or external service dependencies

## Cryptographic Methodology

FibroHash implements a novel multi-stage cryptographic pipeline:

```
User Input → Validation → PBKDF2-HMAC-SHA256 → Multi-Round Generation
                                                        ↓
Secure Password ← Character Encoding ← Entropy Mixing ← HMAC-Fibonacci
```

### Core Algorithm

1. **Input Sanitization**: Validates and sanitizes user input to prevent injection attacks
2. **Key Derivation**: PBKDF2-HMAC-SHA256 with configurable iterations (1K-10K)
3. **Entropy Generation**: HMAC-based Fibonacci sequence generation with cryptographic salts
4. **Multi-Round Processing**: Multiple generation rounds with independent entropy sources
5. **Quality Assurance**: Automated validation of entropy levels and character diversity

### Security Properties

- **Theoretical Entropy**: 192+ bits for 32-character passwords
- **Salt Uniqueness**: Cryptographically secure salt for each generation
- **Timing Attack Resistance**: Consistent operation times regardless of input
- **Pattern Avoidance**: Detection and mitigation of predictable sequences

## Requirements

- **Python**: 3.7+ (uses standard library only)
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Dependencies**: None (zero external dependencies for security)
- **Memory**: <5MB footprint

## Installation

### Quick Setup

```bash
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash
python3 setup.py install  # or pip install -e .
```

### Development Installation

```bash
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash
python3 -m pip install -e .
```

## Usage

### Command Line Interface

```bash
# Interactive mode
python3 -m fibrohash

# Direct generation
python3 -c "from main import generate_password; print(generate_password('research phrase'))"
```

### Programmatic API

```python
from main import generate_password
from security_utils import generate_security_report

# Basic password generation
password = generate_password("secure research phrase", 32, "maximum")

# Security analysis
report = generate_security_report(password)
print(f"Entropy: {report['audit_results']['entropy_analysis']['theoretical_entropy']} bits")
```

### Research Applications

```python
from security_utils import SecurityAuditor

# Comprehensive entropy analysis
auditor = SecurityAuditor()
results = auditor.audit_password_quality(password)

# Character distribution analysis
char_analysis = results['character_analysis']
print(f"Character diversity: {char_analysis['diversity_score']}/100")
```




## Configuration

FibroHash uses `fibrohash_config.json` for security parameter configuration:

```json
{
  "security": {
    "min_password_length": 8,
    "max_password_length": 128,
    "default_security_level": "high"
  },
  "cryptography": {
    "pbkdf2_iterations": {
      "standard": 1000,
      "high": 5000,  
      "maximum": 10000
    }
  }
}
```

### Security Levels

| Level | PBKDF2 Iterations | Key Size | Entropy | Research Use |
|-------|------------------|----------|---------|--------------|
| Standard | 1,000 | 32 bytes | 190+ bits | Educational/Testing |
| High | 5,000 | 64 bytes | 192+ bits | Research/Production |
| Maximum | 10,000 | 128 bytes | 195+ bits | High-security Research |

## Testing & Validation

### Automated Testing

```bash
# Run comprehensive security test suite
python3 test.py

# Run specific entropy validation
python3 -c "from test import test_security_levels; test_security_levels()"
```

### Security Analysis

```python
from security_utils import SecurityAuditor, generate_security_report

# Comprehensive password analysis
auditor = SecurityAuditor()
report = auditor.audit_password_quality(password)

# Generate research-ready security report
full_report = generate_security_report(password)
```

### Reproducible Research

FibroHash includes tools for reproducible security research:

```python
# Entropy analysis for research
from test import calculate_theoretical_entropy, calculate_actual_entropy

theoretical = calculate_theoretical_entropy(password)
actual = calculate_actual_entropy(password)
print(f"Theoretical: {theoretical:.2f} bits, Actual: {actual:.2f} bits")
```

## 📊 Example Output & Analysis

### Generated Password Examples

```
Security Level: High (32 characters)
Password: K7#mP9$vL2@nR8&qT4!wE6%yU1^sA3*z

Analysis:
- Theoretical Entropy: 190.7 bits
- Character Types: 4/4 (uppercase, lowercase, digits, symbols)
- Uniqueness: 100% (no repeated characters)
- Security Score: 94/100
- Compliance: ✅ NIST, PCI-DSS, ISO27001
```

### Security Features Demonstration

```
🔐 Security Features Active:
✅ Cryptographic RNG (secrets module)
✅ PBKDF2-HMAC-SHA256 key derivation
✅ Multiple entropy sources combined
✅ Input validation & sanitization
✅ Character diversity enforcement
✅ Timing attack mitigation
```

## Security Considerations

### Cryptographic Properties

- **Entropy**: 192+ bits theoretical entropy for 32-character passwords
- **Salt**: Unique cryptographic salt for each password generation
- **Key Derivation**: PBKDF2-HMAC-SHA256 with configurable iterations
- **Timing Attacks**: Consistent operation times regardless of input

### Best Practices

- Use unique input phrases for different applications
- Store generated passwords in secure password managers
- Validate entropy levels using provided analysis tools
- Regular security audits using built-in compliance checking

### Research Applications

- Reproducible password security analysis
- Entropy distribution studies
- Cryptographic algorithm validation
- Security compliance verification

## Standards Compliance

FibroHash implements and validates against:

- **NIST SP 800-63B**: Digital identity guidelines for authentication
- **PCI DSS**: Payment card industry data security standards  
- **ISO/IEC 27001**: Information security management systems
- **OWASP**: Open Web Application Security Project guidelines

### Automated Compliance Validation

```python
from security_utils import SecurePasswordValidator

validator = SecurePasswordValidator()
is_compliant, violations = validator.validate(password)
```

## Project Structure

```
fibrohash/
├── main.py                    # Core password generation engine
├── config.py                  # Configuration management
├── security_utils.py          # Security analysis and validation
├── test.py                   # Comprehensive test suite
├── setup.py                  # Package configuration
├── paper.md                  # JOSS research paper
├── paper.bib                 # Bibliography
├── CONTRIBUTING.md           # Contribution guidelines
├── docs/                     # Documentation directory
├── .github/workflows/        # CI/CD configuration
└── fibrohash_config.json    # Security configuration
```

## Contributing

We welcome contributions from the research community! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Development Setup

```bash
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash
python3 -m pip install -e .[dev]
```

### Running Tests

```bash
python3 test.py  # Security test suite
python3 -m pytest  # Unit tests (when available)
```

## Citation

If you use FibroHash in your research, please cite:

```bibtex
@article{lefkaditis2025fibrohash,
  title={FibroHash: A Cryptographically Secure Password Generation Framework for System Administration},
  author={Lefkaditis, Spyros},
  journal={Journal of Open Source Software},
  year={2025},
  note={Under review}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python Cryptography Community for establishing security best practices
- NIST Cybersecurity Framework for security standards guidance
- Open source security researchers and contributors

## Support

- **Documentation**: See [docs/](docs/) directory
- **Issues**: [GitHub Issues](https://github.com/SpyrosLefkaditis/fibrohash/issues)
- **Security Issues**: Please report privately to maintainers
- **Research Collaboration**: Contact via GitHub or paper citations

---

**Disclaimer**: FibroHash implements current cryptographic best practices. Users should evaluate security requirements and keep software updated. No cryptographic system provides absolute security.



```

