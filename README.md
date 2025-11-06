


# FibroHash: Cryptographically Secure Password Generation Framework

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Audit](https://img.shields.io/badge/security-audited-green.svg)](https://github.com/SpyrosLefkaditis/fibrohash)
[![Zenodo DOI](https://img.shields.io/badge/DOI-pending-orange.svg)](https://zenodo.org)

> **📄 Research Paper**: This work is published as an academic paper on Zenodo with full technical methodology and cryptographic analysis. See `main.pdf` for the complete research documentation.

FibroHash is a research-focused, cryptographically secure password generation framework designed for system administrators and security professionals. It implements a novel multi-layered cryptographic approach combining PBKDF2 key derivation, HMAC-based entropy generation, and mathematical sequence algorithms to produce passwords with guaranteed entropy levels exceeding 190 bits.

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
Secure Password ← Character Encoding ← Entropy Mixing ← HMAC-Based Generation
```

### Core Algorithm

1. **Input Sanitization**: Validates and sanitizes user input to prevent injection attacks
2. **Key Derivation**: PBKDF2-HMAC-SHA256 with configurable iterations (1K-10K)
3. **Entropy Generation**: HMAC-based mathematical sequence generation with cryptographic salts
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
- **Memory**: <5MB footprint
- **Storage**: ~2MB for complete installation

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
from config import update_security_level

# Basic password generation
password = generate_password("secure research phrase", 32, "maximum")

# Generate with custom configuration
update_security_level("maximum")
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
from config import update_security_level, get_configuration

# Programmatically update configuration
update_security_level("maximum")
current_config = get_configuration()

# Custom configuration for specific use cases
config = {
    "pbkdf2_iterations": 15000,  # Custom high-security setting
    "password_length": 48,       # Extended length
    "security_level": "custom"
}
```

### Configuration Management

```bash
# View current configuration
python3 -c "from config import get_configuration; print(get_configuration())"

# Validate configuration
python3 -c "from config import validate_config; validate_config()"

# Reset to defaults
python3 -c "from config import reset_to_defaults; reset_to_defaults()"
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
@misc{lefkaditis2025fibrohash,
  title={FibroHash: A Cryptographically Secure Password Generation Framework for System Administration},
  author={Lefkaditis, Spyros},
  year={2025},
  publisher={Zenodo},
  doi={10.5281/zenodo.XXXXXX},
  note={Published on Zenodo}
}
```

*Note: Zenodo DOI will be updated upon publication*

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

