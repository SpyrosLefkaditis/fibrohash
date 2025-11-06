#!/bin/bash

# FibroHash Password Generator Launcher Script
# This script provides a safe way to launch FibroHash with proper error handling

set -euo pipefail  # Exit on any error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check Python version
check_python_version() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "Python not found. Please install Python 3.7 or higher."
        exit 1
    fi

    # Check Python version
    PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
    REQUIRED_VERSION="3.7"
    
    if ! $PYTHON_CMD -c "import sys; exit(0 if sys.version_info >= (3,7) else 1)"; then
        print_error "Python $PYTHON_VERSION detected. FibroHash requires Python $REQUIRED_VERSION or higher."
        exit 1
    fi
    
    print_info "Using Python $PYTHON_VERSION"
}

# Function to check if required files exist
check_files() {
    local required_files=("main.py" "config.py" "security_utils.py")
    
    for file in "${required_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            print_error "Required file '$file' not found in current directory."
            print_info "Please ensure you're running this script from the FibroHash directory."
            exit 1
        fi
    done
    
    print_success "All required files found"
}

# Function to initialize configuration if needed
init_config() {
    if [[ ! -f "fibrohash_config.json" ]]; then
        print_info "Configuration file not found. Creating default configuration..."
        if $PYTHON_CMD config.py; then
            print_success "Default configuration created"
        else
            print_warning "Could not create configuration file. Using built-in defaults."
        fi
    else
        print_info "Configuration file found"
    fi
}

# Function to run security tests
run_tests() {
    if [[ "$1" == "--test" ]]; then
        print_info "Running security test suite..."
        if $PYTHON_CMD test.py; then
            print_success "Security tests completed"
        else
            print_error "Security tests failed"
            exit 1
        fi
        return 0
    fi
    return 1
}

# Function to show help
show_help() {
    echo "FibroHash Password Generator Launcher"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --test     Run security test suite instead of interactive mode"
    echo "  --help     Show this help message"
    echo "  --version  Show version information"
    echo ""
    echo "Examples:"
    echo "  $0              # Launch interactive password generator"
    echo "  $0 --test       # Run comprehensive security tests"
    echo ""
}

# Function to show version
show_version() {
    echo "FibroHash Password Generator"
    echo "Version: 2.0.0 (Enterprise Security Edition)"
    echo "Python requirement: 3.7+"
    echo "License: MIT"
}

# Main execution
main() {
    echo "=================================="
    echo " FibroHash Password Generator"
    echo "=================================="
    echo ""
    
    # Parse command line arguments
    case "${1:-}" in
        --help|-h)
            show_help
            exit 0
            ;;
        --version|-v)
            show_version
            exit 0
            ;;
        --test)
            check_python_version
            check_files
            if run_tests "--test"; then
                exit 0
            fi
            ;;
        "")
            # Default behavior - run main program
            ;;
        *)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
    
    # Pre-flight checks
    print_info "Performing pre-flight security checks..."
    check_python_version
    check_files
    init_config
    
    # Launch main program
    print_info "Starting FibroHash Password Generator..."
    print_info "Press Ctrl+C at any time to exit safely"
    echo ""
    
    if $PYTHON_CMD main.py; then
        print_success "FibroHash completed successfully"
    else
        print_error "FibroHash encountered an error"
        exit 1
    fi
}

# Handle interrupts gracefully
trap 'echo -e "\n${YELLOW}[INFO]${NC} FibroHash interrupted by user. Exiting safely..."; exit 0' INT TERM

# Run main function with all arguments
main "$@"
