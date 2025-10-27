"""
Secure configuration management for FibroHash password generator.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
import secrets

class SecureConfig:
    """Manage secure configuration settings for password generation."""
    
    # Default secure configuration
    DEFAULT_CONFIG = {
        "security": {
            "min_password_length": 8,
            "max_password_length": 128,
            "default_password_length": 32,
            "min_input_length": 1,
            "max_input_length": 1000,
            "default_security_level": "high",
            "allowed_security_levels": ["standard", "high", "maximum"],
            "enforce_character_diversity": True,
            "min_diversity_types": 3
        },
        "cryptography": {
            "pbkdf2_iterations": {
                "standard": 1000,
                "high": 5000,
                "maximum": 10000
            },
            "key_sizes": {
                "standard": 32,
                "high": 64,
                "maximum": 128
            },
            "generation_rounds": {
                "standard": 3,
                "high": 5,
                "maximum": 10
            },
            "fibonacci_bit_length": 2048,
            "entropy_bit_length": 1024
        },
        "charset": {
            "extended_charset": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=<>?{}[]|:;,.~`",
            "allow_custom_charset": False,
            "min_charset_size": 64
        },
        "logging": {
            "log_level": "INFO",
            "log_file": "fibrohash.log",
            "enable_security_logging": True,
            "log_failed_attempts": True
        },
        "performance": {
            "max_concurrent_generations": 10,
            "generation_timeout_seconds": 30,
            "memory_limit_mb": 100
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration manager.
        
        Args:
            config_path: Path to configuration file, defaults to ./fibrohash_config.json
        """
        if config_path is None:
            config_path = os.path.join(os.getcwd(), "fibrohash_config.json")
        
        self.config_path = Path(config_path)
        self.config = self.DEFAULT_CONFIG.copy()
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from file if it exists."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                self._merge_config(file_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load config file {self.config_path}: {e}")
                print("Using default configuration.")
    
    def _merge_config(self, file_config: Dict[str, Any]) -> None:
        """
        Merge file configuration with defaults, validating security settings.
        
        Args:
            file_config: Configuration loaded from file
        """
        # Deep merge configuration
        for section, settings in file_config.items():
            if section in self.config and isinstance(settings, dict):
                self.config[section].update(settings)
            else:
                self.config[section] = settings
        
        # Validate critical security settings
        self._validate_security_config()
    
    def _validate_security_config(self) -> None:
        """Validate security-critical configuration settings."""
        security = self.config.get("security", {})
        
        # Ensure minimum security standards
        if security.get("min_password_length", 0) < 8:
            security["min_password_length"] = 8
        
        if security.get("max_password_length", 0) > 256:
            security["max_password_length"] = 256
        
        if security.get("min_input_length", 0) < 1:
            security["min_input_length"] = 1
        
        if security.get("max_input_length", 0) > 10000:
            security["max_input_length"] = 1000
        
        # Validate cryptographic settings
        crypto = self.config.get("cryptography", {})
        for level in ["standard", "high", "maximum"]:
            iterations = crypto.get("pbkdf2_iterations", {}).get(level, 0)
            if iterations < 1000:
                if "pbkdf2_iterations" not in crypto:
                    crypto["pbkdf2_iterations"] = {}
                crypto["pbkdf2_iterations"][level] = max(1000, iterations)
    
    def get(self, section: str, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            section: Configuration section
            key: Configuration key
            default: Default value if not found
            
        Returns:
            Configuration value or default
        """
        return self.config.get(section, {}).get(key, default)
    
    def get_security_param(self, key: str, default: Any = None) -> Any:
        """Get security configuration parameter."""
        return self.get("security", key, default)
    
    def get_crypto_param(self, key: str, default: Any = None) -> Any:
        """Get cryptography configuration parameter."""
        return self.get("cryptography", key, default)
    
    def get_charset(self) -> str:
        """Get the configured character set."""
        return self.get("charset", "extended_charset", self.DEFAULT_CONFIG["charset"]["extended_charset"])
    
    def save_config(self) -> None:
        """Save current configuration to file."""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, sort_keys=True)
        except IOError as e:
            raise RuntimeError(f"Could not save configuration: {e}")
    
    def create_default_config(self) -> None:
        """Create a default configuration file."""
        self.config = self.DEFAULT_CONFIG.copy()
        self.save_config()
        print(f"Created default configuration file: {self.config_path}")
    
    def validate_password_length(self, length: int) -> bool:
        """Validate if password length is within configured limits."""
        min_len = self.get_security_param("min_password_length", 8)
        max_len = self.get_security_param("max_password_length", 128)
        return min_len <= length <= max_len
    
    def validate_security_level(self, level: str) -> bool:
        """Validate if security level is allowed."""
        allowed = self.get_security_param("allowed_security_levels", ["standard", "high", "maximum"])
        return level in allowed
    
    def get_security_params(self, level: str) -> Dict[str, Any]:
        """
        Get security parameters for specified level.
        
        Args:
            level: Security level (standard/high/maximum)
            
        Returns:
            Dictionary of security parameters
        """
        if not self.validate_security_level(level):
            level = self.get_security_param("default_security_level", "high")
        
        return {
            "rounds": self.get_crypto_param("generation_rounds", {}).get(level, 5),
            "key_size": self.get_crypto_param("key_sizes", {}).get(level, 64),
            "iterations": self.get_crypto_param("pbkdf2_iterations", {}).get(level, 5000),
            "fibonacci_bits": self.get_crypto_param("fibonacci_bit_length", 2048),
            "entropy_bits": self.get_crypto_param("entropy_bit_length", 1024)
        }

# Global configuration instance
_config_instance = None

def get_config(config_path: Optional[str] = None) -> SecureConfig:
    """
    Get global configuration instance.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        SecureConfig instance
    """
    global _config_instance
    if _config_instance is None or config_path is not None:
        _config_instance = SecureConfig(config_path)
    return _config_instance

def create_default_config(config_path: Optional[str] = None) -> None:
    """Create a default configuration file."""
    config = SecureConfig(config_path)
    config.create_default_config()

if __name__ == "__main__":
    # Create default configuration file
    create_default_config()
    print("Default configuration file created successfully.")