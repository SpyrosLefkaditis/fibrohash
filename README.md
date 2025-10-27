


# FibroHash - Enterprise-Grade Secure Password Generator

`FibroHash` is a cryptographically secure password generator that combines advanced mathematical concepts with modern security practices. It uses cryptographic Fibonacci-based algorithms, PBKDF2 key derivation, and multiple entropy sources to generate highly secure, unpredictable passwords suitable for enterprise environments.

## 🔐 Security Features

- **Cryptographic Security**: Uses `secrets` module for cryptographically secure random number generation
- **PBKDF2 Key Derivation**: Industry-standard key derivation with configurable iterations
- **Multiple Entropy Sources**: Combines user input, cryptographic salts, and Fibonacci-based algorithms
- **Input Validation**: Comprehensive sanitization and validation of all inputs
- **Timing Attack Resistance**: Constant-time operations where possible
- **Character Diversity Enforcement**: Ensures passwords meet complexity requirements
- **Configurable Security Levels**: Standard, High, and Maximum security modes
- **Security Auditing**: Built-in password quality analysis and compliance checking

## 🔬 How It Works

FibroHash employs a multi-layered security approach:

1. **Input Processing**: User input is validated, sanitized, and processed through PBKDF2 with cryptographic salt
2. **Cryptographic Fibonacci Generation**: Creates large numbers using HMAC-SHA256 in a Fibonacci-inspired pattern
3. **Multi-Round Generation**: Generates password segments through multiple cryptographic rounds
4. **Entropy Mixing**: Combines multiple entropy sources using secure cryptographic operations
5. **Character Encoding**: Maps numeric values to characters using a secure base conversion system
6. **Quality Assurance**: Validates output for character diversity and security compliance

### Security Architecture

```
User Input → Input Validation → PBKDF2 + Salt → Multi-Round Generation
                                                         ↓
Password ← Character Encoding ← Entropy Mixing ← Crypto-Fibonacci
```

## 📋 System Requirements

- **Python**: 3.7 or higher
- **Dependencies**: Standard library only (no external dependencies)
- **Platforms**: Cross-platform (Windows, macOS, Linux)
- **Memory**: Minimal footprint (~1MB)
- **Performance**: Optimized for security over speed

## 🚀 Installation & Quick Start

### Prerequisites

Ensure you have Python 3.7+ installed on your system:

```bash
python --version  # Should be 3.7 or higher
```

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SpyrosLefkaditis/fibrohash.git
   cd fibrohash
   ```

2. **Set up configuration** (optional):
   ```bash
   python config.py  # Creates default configuration file
   ```

3. **Run FibroHash**:

   **Linux/macOS**:
   ```bash
   chmod +x init.sh
   ./init.sh
   ```

   **Windows**:
   ```cmd
   python main.py
   ```

   **Direct Python execution**:
   ```bash
   python3 main.py
   ```

### Quick Usage Examples

**Interactive Mode**:
```bash
python main.py
# Follow the prompts to generate a secure password
```

**Programmatic Usage**:
```python
from main import generate_password

# Generate with defaults (32 chars, high security)
password = generate_password("my secure phrase")

# Generate with custom parameters
password = generate_password("my phrase", password_length=16, security_level="maximum")
```




## 🔧 Configuration

FibroHash supports extensive configuration through `fibrohash_config.json`:

```json
{
  "security": {
    "min_password_length": 8,
    "max_password_length": 128,
    "default_password_length": 32,
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

| Level | PBKDF2 Iterations | Key Size | Rounds | Use Case |
|-------|------------------|----------|---------|----------|
| **Standard** | 1,000 | 32 bytes | 3 | General use |
| **High** | 5,000 | 64 bytes | 5 | Business/Personal |
| **Maximum** | 10,000 | 128 bytes | 10 | High-security environments |

## 🧪 Testing & Validation

### Comprehensive Security Testing

Run the enhanced security test suite:

```bash
python test.py
```

This performs:
- **Entropy Analysis**: Shannon entropy, theoretical entropy calculations
- **Character Distribution**: Diversity and pattern analysis
- **Uniqueness Testing**: Collision detection across multiple generations
- **Timing Attack Resistance**: Performance consistency analysis
- **Edge Case Testing**: Input validation and error handling
- **Compliance Checking**: NIST, PCI-DSS, ISO27001 standards

### Security Audit Tools

Generate detailed security reports:

```python
from security_utils import generate_security_report

# Analyze any password
report = generate_security_report("YourPasswordHere")
print(f"Security Score: {report['audit_results']['security_score']}/100")
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

## 🛡️ Security Best Practices

### For Users
- **Use unique input phrases** for different services
- **Store generated passwords securely** (password manager recommended)
- **Don't share passwords** via unsecured channels
- **Regenerate passwords periodically** for high-security accounts
- **Use maximum security level** for critical systems

### For Developers
- **Review security configuration** before deployment
- **Monitor for security updates** to dependencies
- **Implement proper logging** for security events
- **Test with your security requirements** using provided tools
- **Consider hardware security modules** for enterprise deployments

### Input Recommendations
- **Length**: 8+ characters provide better entropy mixing
- **Complexity**: Mix of letters, numbers, symbols in input
- **Uniqueness**: Use different phrases for different passwords
- **Avoid**: Personal information, dictionary words, patterns

## 🔍 Security Audit & Compliance

### Standards Compliance
- ✅ **NIST SP 800-63B**: Password composition guidelines
- ✅ **PCI DSS**: Payment card industry requirements
- ✅ **ISO/IEC 27001**: Information security management
- ✅ **OWASP**: Web application security best practices

### Regular Security Testing
```bash
# Run comprehensive security test suite
python test.py

# Generate security audit report
python -c "from security_utils import generate_security_report; generate_security_report('test_password')"

# Test with custom configuration
python config.py  # Creates/updates config file
```

## 📁 Project Structure

```
fibrohash/
├── main.py              # Core password generation engine
├── config.py            # Configuration management system
├── security_utils.py    # Security auditing and validation tools
├── test.py             # Comprehensive security test suite
├── init.sh             # Linux/macOS launcher script
├── fibrohash_config.json # Configuration file (auto-generated)
├── README.md           # This documentation
└── LICENSE             # MIT license
```

## 🚨 Security Considerations

### What FibroHash Does NOT Do
- **Store passwords**: All generation is stateless
- **Network communication**: Fully offline operation
- **Log sensitive data**: Input phrases are not logged
- **Guarantee uniqueness**: Use different inputs for different passwords

### Threat Model
FibroHash is designed to resist:
- 🔐 **Brute force attacks**: High entropy output
- ⚡ **Timing attacks**: Consistent operation times
- 🎯 **Pattern analysis**: Cryptographic randomness
- 📊 **Statistical analysis**: Multiple entropy sources
- 🔍 **Input prediction**: PBKDF2 with salt

## 🤝 Contributing

We welcome security-focused contributions:

1. **Security reviews** and vulnerability reports
2. **Performance optimizations** maintaining security
3. **Compliance enhancements** for additional standards
4. **Documentation improvements**
5. **Test coverage expansion**

### Reporting Security Issues
For security vulnerabilities, please:
1. **Do not** create public issues
2. **Email directly** to maintainers
3. **Provide details** for reproduction
4. **Allow time** for coordinated disclosure

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Python Cryptography Community** for security best practices
- **NIST** for password security guidelines
- **OWASP** for application security standards
- **Security researchers** who review and improve this tool

---

**⚠️ Security Notice**: While FibroHash implements current security best practices, no password generator is 100% secure. Use in conjunction with other security measures and keep software updated.



```

