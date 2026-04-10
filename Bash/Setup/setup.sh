#!/bin/bash

set -e

# Must be root
if [[ $EUID -ne 0 ]]; then
    echo "[!] This script must be run as root"
    exit 1
fi

# Flags
ACTION=""        
MODULES=()

# Parse args
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -i|--install)
            ACTION="install"
            ;;
        -u|--uninstall)
            ACTION="uninstall"
            ;;
        --common)
            MODULES+=("common")
            ;;
        --pentest)
            MODULES+=("pentest")
            ;;
        --malware)
            MODULES+=("malware")
            ;;
        --exploitdev)
            MODULES+=("exploitdev")
            ;;
        --all)
            MODULES=("common" "pentest" "malware" "exploitdev")
            ;;
        -h|--help)
            echo "Usage:"
            echo "  $0 -i|--install [modules]"
            echo "  $0 -u|--uninstall [modules]"
            echo ""
            echo "Modules:"
            echo "  --common"
            echo "  --pentest"
            echo "  --malware"
            echo "  --exploitdev"
            echo "  --all"
            exit 0
            ;;
        *)
            echo "[!] Unknown option: $1"
            exit 1
            ;;
    esac
    shift
done

# Validate action
if [[ -z "$ACTION" ]]; then
    echo "[!] Must specify -i or -u. Use -h for help."
    exit 1
fi

# Validate modules
if [[ ${#MODULES[@]} -eq 0 ]]; then
    echo "[!] No modules specified. Use -h for help."
    exit 1
fi

echo "[+] Cybersecurity Setup ($ACTION)"

# Load & run modules
source "lib/utils.sh"

for MODULE in "${MODULES[@]}"; do
    FILE="packages/${MODULE}.sh"

    if [[ ! -f "$FILE" ]]; then
        echo "[!] Module not found: $MODULE"
        exit 1
    fi

    source "$FILE"

    if [[ "$ACTION" == "install" ]]; then
        echo "[+] Installing $MODULE..."
        install_"$MODULE"
    else
        echo "[+] Uninstalling $MODULE..."
        uninstall_"$MODULE"
    fi
done

echo "[+] Done!"


