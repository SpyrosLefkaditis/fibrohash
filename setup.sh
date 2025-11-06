#!/bin/bash

# FibroHash Setup Script
# This script helps set up FibroHash on your system

set -euo pipefail

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

echo "========================================"
echo " FibroHash Password Generator Setup"
echo "========================================"
echo ""

# Check Python installation
print_info "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
else
    print_error "Python not found!"
    print_info "Please install Python 3.7+ from https://python.org"
    exit 1
fi

if ! $PYTHON_CMD -c "import sys; exit(0 if sys.version_info >= (3,7) else 1)"; then
    print_error "Python $PYTHON_VERSION found, but FibroHash requires Python 3.7+"
    print_info "Please upgrade Python or install a newer version"
    exit 1
fi

print_success "Python $PYTHON_VERSION detected"

# Check required modules
print_info "Checking required Python modules..."
required_modules=("secrets" "hashlib" "hmac" "json" "logging" "time" "collections" "re" "os" "pathlib" "typing" "statistics")
missing_modules=()

for module in "${required_modules[@]}"; do
    if ! $PYTHON_CMD -c "import $module" 2>/dev/null; then
        missing_modules+=("$module")
    fi
done

if [ ${#missing_modules[@]} -ne 0 ]; then
    print_error "Missing required Python modules: ${missing_modules[*]}"
    print_info "These modules should be included with Python 3.7+. Please check your Python installation."
    exit 1
fi

print_success "All required modules available"

# Set up executable permissions
print_info "Setting up executable permissions..."
if [ -f "init.sh" ]; then
    chmod +x init.sh
    print_success "init.sh is now executable"
else
    print_warning "init.sh not found - manual execution will be required"
fi

# Create default configuration
print_info "Creating default configuration..."
if $PYTHON_CMD config.py; then
    print_success "Default configuration created"
else
    print_warning "Could not create configuration file - will use built-in defaults"
fi

# Run basic functionality test
print_info "Running basic functionality test..."
if $PYTHON_CMD -c "
from main import generate_password
try:
    pwd = generate_password('test', 16, 'standard')
    print(f'✓ Test password generated: {pwd[:4]}...{pwd[-4:]}')
    print('✓ Basic functionality working')
except Exception as e:
    print(f'✗ Test failed: {e}')
    exit(1)
"; then
    print_success "Basic functionality test passed"
else
    print_error "Basic functionality test failed"
    exit 1
fi

# Final setup
print_info "Final setup steps..."
echo ""
print_success "FibroHash setup completed successfully!"
echo ""
echo "You can now use FibroHash in the following ways:"
echo ""
echo "1. Interactive mode:"
echo "   ./init.sh"
echo "   or"
echo "   $PYTHON_CMD main.py"
echo ""
echo "2. Run security tests:"
echo "   ./init.sh --test"
echo "   or"
echo "   $PYTHON_CMD test.py"
echo ""
echo "3. Programmatic usage:"
echo "   from main import generate_password"
echo "   password = generate_password('your phrase')"
echo ""
print_info "See README.md for comprehensive documentation"
print_info "Configuration file: fibrohash_config.json"
echo ""
print_success "Setup complete! FibroHash is ready to use."