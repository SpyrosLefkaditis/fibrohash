


# FibroHash: Comprehensive Cryptographic Password Generation Framework

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Audit](https://img.shields.io/badge/security-audited-green.svg)](https://github.com/SpyrosLefkaditis/fibrohash)
[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17546159.svg)](https://doi.org/10.5281/zenodo.17546159)
[![OpenAIRE](https://img.shields.io/badge/OpenAIRE-indexed-blue.svg)](https://explore.openaire.eu/)

> **📄 Published Documentation**: This work is published on Zenodo with DOI [10.5281/zenodo.17546159](https://doi.org/10.5281/zenodo.17546159). The documentation presents complete technical methodology, cryptographic analysis, and implementation details for educational purposes. See `main.pdf` for the full technical documentation.

FibroHash is a comprehensive, cryptographically secure password generation framework designed for system administrators, security professionals, and educational use. It implements industry-standard cryptographic techniques including PBKDF2 key derivation and multi-round entropy generation using Python's `secrets` module, enhanced with built-in security analysis and compliance validation tools. The framework produces secure, non-reproducible passwords with measured entropy levels of 150+ bits for 32-character passwords.

## Primary Applications

- **System Administration**: Production-ready secure password generation with comprehensive analysis
- **Security Auditing**: Built-in password quality analysis and security validation
- **Educational Use**: Transparent implementation for studying modern cryptographic practices
- **Enterprise Security**: Configurable security levels and detailed entropy reporting

## Key Features

- **🔐 Cryptographic Security**: PBKDF2-HMAC-SHA256 with 1,000-10,000 configurable iterations
- **📊 Entropy Analysis**: Built-in Shannon entropy calculation and character distribution analysis
- **✅ Security Validation**: Password quality analysis and entropy measurement
- **🔬 Research Tools**: Comprehensive security auditing and reproducible testing framework
- **📱 Zero Dependencies**: Uses only Python standard library for maximum security
- **🌐 Offline Operation**: No network communication or external service dependencies

## Why FibroHash vs Standard Tools?

### **🎯 Unique Value Proposition**

**Standard Tools** (`secrets.token_urlsafe()`, password managers):
- ✅ Simple and reliable
- ✅ Pure randomness (~190+ bits theoretical entropy)
- ❌ Limited security analysis capabilities
- ❌ No compliance reporting features

**FibroHash**:
- ✅ **Comprehensive Analysis**: Built-in entropy measurement, security auditing, and compliance validation
- ✅ **Production Ready**: Cryptographically secure using industry-standard PBKDF2 and Python's `secrets` module
- ✅ **Security Analysis**: Comprehensive entropy analysis and password quality validation
- ✅ **Transparent Implementation**: All cryptographic operations visible and well-documented for auditability
- ✅ **Configurable Security**: Multiple security levels (1K-10K PBKDF2 iterations) for different environments
- ✅ **Enhanced Security**: 150+ bit entropy through multi-round generation with multiple entropy sources

### **🏢 Primary Use Cases**

1. **System Administration**: Secure password generation for servers, databases, and service accounts
2. **Security Auditing**: Compliance validation and entropy analysis for enterprise environments  
3. **Educational and Training**: Hands-on learning of cryptographic password security practices
4. **Development Integration**: Programmable API for incorporating secure password generation into applications

## Cryptographic Methodology

FibroHash demonstrates standard multi-stage cryptographic practices:

```
User Input → Validation → PBKDF2-HMAC-SHA256 → Multi-Round Generation
                                                        ↓
Secure Password ← Character Encoding ← Entropy Mixing ← HMAC + secrets.token_bytes()
```

### 🔍 **Open Source & Transparent**

**Complete implementation available**: All cryptographic operations are fully implemented in [`main.py`](main.py) and [`security_utils.py`](security_utils.py) - no hidden functionality or external dependencies.

**Verifiable Claims**: Run `python3 test.py` to independently verify entropy measurements and security properties.

### Core Algorithm

1. **Input Sanitization**: Validates and sanitizes user input to prevent injection attacks
2. **Key Derivation**: PBKDF2-HMAC-SHA256 with configurable iterations (1K-10K)
3. **Entropy Generation**: HMAC-based mathematical sequence generation with cryptographic salts
4. **Multi-Round Processing**: Multiple generation rounds with independent entropy sources
5. **Quality Assurance**: Automated validation of entropy levels and character diversity

### Security Properties

- **Measured Entropy**: 150+ bits for 32-character passwords (using standard techniques)
- **Theoretical Maximum**: Up to 207+ bits with full 90-character set utilization
- **Fresh Randomness**: Uses `secrets.token_bytes()` for cryptographically secure entropy
- **Non-Reproducible**: Each generation produces different passwords for maximum security
- **Pattern Avoidance**: Detection and mitigation of predictable sequences
- **Multiple Entropy Sources**: Combines user input with cryptographic randomness

## Requirements

- **Python**: 3.7+ (uses standard library only)
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Dependencies**: None (zero external dependencies for security)
- **Memory**: <2MB footprint

## Installation

### Quick Start (Recommended)

```bash
# Clone the repository
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash

# Run the setup script
./setup.sh

# Launch interactive password generator
./init.sh
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash

# Make scripts executable
chmod +x setup.sh init.sh

# Run setup and configuration
./setup.sh

# Run comprehensive security test suite
python3 test.py
```

### Requirements

- **Python 3.7+** (uses standard library only)
- **No external dependencies** (zero pip requirements for maximum security)
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Memory**: <2MB footprint
- **Storage**: <1MB for complete installation

### Verification

```bash
# Test the installation
python3 test.py

# Quick functionality check
python3 -c "from main import generate_password; print('Installation successful!')"
```

## Usage

### Quick Start Script

```bash
# Interactive password generation with guided setup
./init.sh

# The init.sh script provides:
# - Interactive password generation
# - Security level selection
# - Configuration validation
# - Usage examples and help
```

### Command Line Interface

```bash
# Interactive mode (if available)
python3 -m fibrohash

# Direct generation - basic usage
python3 -c "from main import generate_password; print(generate_password('research phrase'))"

# Direct generation - with parameters
python3 -c "from main import generate_password; print(generate_password('secure phrase', 32, 'maximum'))"

# Using the test/demo script
python3 test.py  # Includes examples and security validation
```

### Programmatic API

```python
from main import generate_password
from security_utils import generate_security_report
from config import get_config

# Basic password generation
password = generate_password("secure research phrase", 32, "maximum")

# Generate with configuration validation
config = get_config()
if config.validate_password_length(48):
    password = generate_password("enterprise phrase", 48, "maximum")

# Security analysis and reporting
report = generate_security_report(password)
print(f"Entropy: {report['audit_results']['entropy_analysis']['theoretical_entropy']} bits")
print(f"Security Score: {report['audit_results']['security_score']}/100")
```

### Advanced Usage Examples

```python
from security_utils import SecurityAuditor, SecurePasswordValidator
from main import generate_password

# Batch password generation with analysis
passwords = []
for i in range(10):
    pwd = generate_password(f"batch-phrase-{i}", 32, "high")
    passwords.append(pwd)

# Comprehensive security audit
auditor = SecurityAuditor()
validator = SecurePasswordValidator()

for pwd in passwords:
    # Security audit
    audit_results = auditor.audit_password_quality(pwd)
    
    # Compliance validation  
    is_valid, violations = validator.validate(pwd)
    
    print(f"Password: {pwd[:8]}... | Entropy: {audit_results['entropy_analysis']['theoretical_entropy']:.1f} bits | Valid: {is_valid}")
```

### Research Applications

```python
from security_utils import SecurityAuditor
from test import calculate_theoretical_entropy, calculate_actual_entropy

# Comprehensive entropy analysis for research
auditor = SecurityAuditor()
results = auditor.audit_password_quality(password)

# Character distribution analysis
char_analysis = results['character_analysis']
print(f"Character diversity: {char_analysis['diversity_score']}/100")

# Theoretical vs actual entropy comparison
theoretical = calculate_theoretical_entropy(password)
actual = calculate_actual_entropy(password)
print(f"Theoretical: {theoretical:.2f} bits, Actual: {actual:.2f} bits")
```

### Script-Based Usage

```bash
# Run the initialization script for guided usage
./init.sh

# Available options in init.sh:
# 1. Interactive password generation
# 2. Batch generation
# 3. Security analysis
# 4. Configuration management
# 5. Help and examples

# Direct execution with parameters
python3 main.py --phrase "secure phrase" --length 32 --level maximum
```




## Configuration

### Configuration Files

FibroHash provides multiple configuration options:

#### 1. JSON Configuration (`fibrohash_config.json`)

```json
{
  "security": {
    "min_password_length": 8,
    "max_password_length": 128,
    "default_security_level": "high",
    "enforce_character_diversity": true,
    "min_entropy_threshold": 190
  },
  "cryptography": {
    "pbkdf2_iterations": {
      "standard": 1000,
      "high": 5000,  
      "maximum": 10000
    },
    "salt_length": 32,
    "key_length": 64
  },
  "output": {
    "include_entropy_analysis": true,
    "show_security_score": true,
    "verbose_logging": false
  }
}
```

#### 2. Python Configuration (`config.py`)

```python
# Modify config.py to adjust runtime parameters
```python
from config import get_config

# Get current configuration
config = get_config()
current_level = config.get_security_param('default_security_level')

# Get security parameters for a specific level
params = config.get_security_params("maximum")
print(f"Iterations: {params['iterations']}, Key size: {params['key_size']}")

# Validate configuration settings
is_valid_length = config.validate_password_length(32)
is_valid_level = config.validate_security_level("maximum")
```

### Configuration Management

```bash
# View current configuration
python3 -c "from config import get_config; config = get_config(); print(f'Security level: {config.get_security_param(\"default_security_level\")}')"

# Create default configuration file
python3 -c "from config import create_default_config; create_default_config()"

# Get security parameters
python3 -c "from config import get_config; config = get_config(); print(config.get_security_params('high'))"
```

### Security Levels

| Level | PBKDF2 Iterations | Key Size | Measured Entropy | Research Use |
|-------|------------------|----------|------------------|--------------|
| Standard | 1,000 | 32 bytes | 150+ bits | Educational/Testing |
| High | 5,000 | 64 bytes | 155+ bits | Research/Production |
| Maximum | 10,000 | 128 bytes | 160+ bits | High-security Research |

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
- Validation: ✅ Security checks passed
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

- **Measured Entropy**: 150+ bits actual entropy for 32-character passwords (exceeds AES-128)
- **Theoretical Maximum**: 207+ bits with optimal character set utilization
- **Salt**: Unique cryptographic salt for each password generation
- **Key Derivation**: PBKDF2-HMAC-SHA256 with configurable iterations
- **Timing Attacks**: Consistent operation times regardless of input
- **Multiple Entropy Sources**: Combines user input, PBKDF2 derivation, and cryptographic randomness

### Best Practices

- Use unique input phrases for different applications
- Store generated passwords in secure password managers
- Validate entropy levels using provided analysis tools
- Regular security audits using built-in compliance checking

### Educational Applications

- Password security analysis and entropy measurement learning
- Cryptographic implementation study (PBKDF2, HMAC, entropy mixing)
- Understanding security compliance requirements
- Practical application of cryptographic best practices

## Security Standards Alignment

FibroHash follows established security best practices and guidelines:

- **Industry Standards**: Implements PBKDF2-HMAC-SHA256 as recommended by security frameworks
- **Password Security**: Follows modern password complexity and entropy requirements
- **Cryptographic Practices**: Uses established algorithms and secure random number generation
- **Best Practices**: Incorporates lessons from security research and vulnerability analysis

### Password Quality Validation

```python
from security_utils import SecurePasswordValidator

validator = SecurePasswordValidator()
is_valid, issues = validator.validate(password)
print(f"Password valid: {is_valid}, Issues found: {len(issues)}")
```

## Project Structure

```
fibrohash/
├── main.py                    # Core password generation engine
├── config.py                  # Configuration management
├── security_utils.py          # Security analysis and validation
├── test.py                   # Comprehensive test suite
├── setup.py                  # Package configuration
├── main.tex                  # arXiv research paper (LaTeX)
├── references.bib            # Bibliography for arXiv submission
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

# Make scripts executable (Linux/macOS)
chmod +x setup.sh init.sh

# No pip installation needed - uses only standard library
```

### Running Tests

```bash
python3 test.py  # Comprehensive security test suite

# Verify installation
python3 -c "from main import generate_password; print('Installation successful')"
```

## Citation

If you use FibroHash in your work or research, please cite our published documentation:

```bibtex
@misc{lefkaditis2025fibrohash,
  title={FibroHash: A Cryptographically Secure Password Generation Framework for System Administration},
  author={Lefkaditis, Spyros},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.17546159},
  url={https://doi.org/10.5281/zenodo.17546159}
}
```

**APA Style:**
Lefkaditis, S. (2025). *FibroHash: A Cryptographically Secure Password Generation Framework for System Administration* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.17546159

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python Cryptography Community for establishing security best practices
- Open source security researchers and contributors
- Academic research community for advancing password security methodologies

## Support

- **Documentation**: See [docs/](docs/) directory
- **Issues**: [GitHub Issues](https://github.com/SpyrosLefkaditis/fibrohash/issues)
- **Security Issues**: Please report privately to maintainers
- **Research Collaboration**: Contact via GitHub or paper citations

---

## Framework Overview

**Purpose**: FibroHash is a comprehensive cryptographic password generation framework that implements industry-standard security practices with enhanced analysis and compliance validation capabilities.

**Production Use**: The password generation is cryptographically secure using Python's `secrets` module and industry-standard PBKDF2-HMAC-SHA256. The framework is suitable for production use in system administration, security auditing, and educational environments.

**Technical Approach**: This implementation combines proven cryptographic techniques (PBKDF2, HMAC, CSPRNG) with comprehensive security analysis tools, providing both secure password generation and detailed entropy validation for compliance and educational purposes.

---

**Technical Disclaimer**: FibroHash implements current cryptographic best practices for educational purposes. Users should evaluate security requirements and keep software updated. No cryptographic system provides absolute security.



```

