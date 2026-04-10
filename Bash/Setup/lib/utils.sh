#!/bin/bash

go_install() {
    local package="$1"
    echo "[+] Installing Go package: $package"
    GOBIN=/usr/local/bin GOPATH=/root/go go install "$package@latest"
}

pip_install() {
    local package="$1"
    echo "[+] Installing Python package: $package"
    pip3 install "$package" --break-system-packages 2>/dev/null || pip3 install "$package"
}

clone_repo() {
    local repo="$1"
    local dest="$2"
    echo "[+] Cloning repo: $repo -> $dest"

    if [[ ! -d "$dest" ]]; then
        git clone "$repo" "$dest"
    else
        echo "[!] Repo already exists, skipping"
    fi
}

add_to_shellrc() {
    local LINE="$1"

    if [[ -n "$ZSH_VERSION" ]]; then
        RC="$HOME/.zshrc"
    else
        RC="$HOME/.bashrc"
    fi

    if ! grep -Fxq "$LINE" "$RC"; then
        echo "$LINE" >> "$RC"
        echo "[+] Added to RC: $LINE"
    fi
}