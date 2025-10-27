from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fibrohash",
    version="2.0.0",
    author="Spyros Lefkaditis",
    author_email="spyros.lefkaditis@example.com",
    description="Cryptographically secure password generation framework for system administration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpyrosLefkaditis/fibrohash",
    project_urls={
        "Bug Tracker": "https://github.com/SpyrosLefkaditis/fibrohash/issues",
        "Documentation": "https://github.com/SpyrosLefkaditis/fibrohash/blob/main/README.md",
        "Source Code": "https://github.com/SpyrosLefkaditis/fibrohash",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "fibrohash=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "fibrohash": ["fibrohash_config.json"],
    },
    keywords="cryptography password-generator security pbkdf2 entropy-analysis system-administration",
    zip_safe=False,
)