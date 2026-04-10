# Setup Script
An automated installation script to configure any Debian/Ubuntu distribution with essential cybersecurity tools for various domains. 

## Features
- **Modular installation**: Choose which tools to install based on your needs
- **Multiple tool sets**:
  - `--common`: Basic tools (networking, system utilities, development)
  - `--pentest`: Penetration testing tools
  - `--malware`: Malware analysis tools
  - `--exploitdev`: Exploit development tools
  - `--all`: Install all modules
- **Full automation**: Installs and configures everything automatically

## Quick Installation
### Prerequisites
- Debian/Ubuntu-based distribution
- Internet connection
### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/tu-usuario/Scripts.git
   cd Scripts/Bash/Setup
   ```
2. **Set execution permissions**:
   ```bash
   chmod +x setup.sh
   ```
3. **Run the script as root**:
   ```bash
   sudo ./setup.sh --install --all
   ```

## Detailed Usage
### Basic Syntax
```bash
./setup.sh -i|--install [modules]    # Install tools
./setup.sh -u|--uninstall [modules]  # Uninstall tools
./setup.sh -h|--help                 # View help
```
### Examples
```bash
# Install only common tools
./setup.sh --install --common
# Install pentest and exploit development tools
./setup.sh --install --pentest --exploitdev
# Install everything
./setup.sh --install --all
# Uninstall specific modules
./setup.sh --uninstall --malware
```

## Available Modules
### `--common`
Essential tools:
- **Networking**: curl, wget, net-tools, dnsutils, traceroute, whois
- **System utilities**: zip, unzip, p7zip, tar, tree, htop, jq
- **Development**: build-essential, python3, python3-pip, git
### `--pentest`
Specialized tools for penetration testing
### `--malware`
Tools for malware analysis and research
### `--exploitdev`
Tools for exploit research and development
## Project Structure
```
.
├── README.md           # This file
├── setup.sh            # Main script
├── lib/
│   ├── customrc        # Custom configurations
│   └── utils.sh        # Auxiliary functions
└── packages/
    ├── common.sh       # Common tools module
    ├── pentest.sh      # Penetration testing module
    ├── malware.sh      # Malware analysis module
    └── exploitdev.sh   # Exploit development module
```
## Important Notes
- **Requires root access**: This script modifies system settings
- **Backup recommended**: Make a backup before running
- **Active connection**: You need an Internet connection throughout the installation


## Contact and Contributions
If you find bugs or have suggestions for improvements, open an issue or submit a pull request.
---
**Last updated**: April 2026 




