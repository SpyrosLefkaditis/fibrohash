# Contributing to FibroHash

Thank you for your interest in contributing to FibroHash! This document provides guidelines for contributing to this cryptographically secure password generation framework.

## Code of Conduct

This project adheres to a code of conduct that promotes an inclusive and respectful environment. By participating, you agree to uphold these standards.

## How to Contribute

### Reporting Issues

Before creating an issue, please check if it already exists. When reporting bugs:

1. Use a clear and descriptive title
2. Describe the exact steps to reproduce the issue
3. Include your Python version and operating system
4. For security vulnerabilities, please email directly rather than creating public issues

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

1. Use a clear and descriptive title
2. Provide a detailed description of the proposed enhancement
3. Explain why this enhancement would be useful
4. Consider backward compatibility implications

### Security Contributions

Security is paramount for FibroHash. When contributing security-related changes:

1. Follow secure coding practices
2. Include comprehensive tests for security features
3. Document security implications of changes
4. Consider timing attack resistance and entropy implications

## Development Process

### Quick Start for Contributors

```bash
# Get started immediately
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash
./init.sh --version  # Verify setup
./init.sh --test     # Run test suite
```

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/SpyrosLefkaditis/fibrohash.git
cd fibrohash

# Quick setup using the initialization script
./init.sh

# Or manual setup
python3 -m pip install -e .

# Verify installation
python3 -c "from main import generate_password; print('Development environment ready!')"
```

### Running Tests

```bash
# Run all tests using the init script
./init.sh --test

# Or run tests directly
python3 test.py

# Run security audit and generate report
python3 -c "from main import generate_password; from security_utils import generate_security_report; pwd = generate_password('test', 32, 'high'); report = generate_security_report(pwd); print('Security tests passed!')"

# Test configuration management
python3 -c "from config import get_config; config = get_config(); print(f'Config loaded: {config.get_security_param(\"default_security_level\")}')"
```

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Include docstrings for all public functions
- Maintain backward compatibility when possible

### Commit Messages

Use clear, descriptive commit messages:

```
🔐 Add timing attack resistance to key derivation
📊 Improve entropy analysis accuracy
🐛 Fix character encoding edge case
📚 Update documentation for new security features
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation as needed
7. Commit your changes (`git commit -m '🔐 Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Pull Request Requirements

- [ ] Tests pass
- [ ] Security implications documented
- [ ] Documentation updated
- [ ] Backward compatibility maintained
- [ ] Code follows project style guidelines

## Security Considerations

### Cryptographic Changes

Changes to cryptographic functions require:

1. Detailed security analysis
2. Comprehensive testing
3. Documentation of security properties
4. Consideration of attack vectors

### Performance vs Security

When optimizing performance:

1. Security must not be compromised
2. Timing attack resistance must be maintained
3. Entropy levels must not be reduced

## Testing Guidelines

### Unit Tests

All new functions should include unit tests:

```python
def test_password_generation():
    password = generate_password("test phrase", 16, "high")
    assert len(password) == 16
    assert isinstance(password, str)
```

### Security Tests

Security-critical functions require comprehensive testing:

```python
def test_entropy_levels():
    passwords = [generate_password("test", 32) for _ in range(100)]
    assert len(set(passwords)) == 100  # All unique
```

## Documentation

### Code Documentation

- All public functions must have docstrings
- Security implications should be documented
- Examples should be included for complex functions

### README Updates

When adding features, update:

- Installation instructions if needed
- Usage examples
- Security considerations
- Performance implications

## Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Create release notes
5. Tag release
6. Update documentation

## Getting Help

- Check existing issues and documentation
- Ask questions in discussions
- For security issues, email maintainers directly

## Recognition

Contributors will be acknowledged in:

- CONTRIBUTORS.md file
- Release notes
- Paper acknowledgments (for significant contributions)

Thank you for helping make FibroHash more secure and useful for the research community!