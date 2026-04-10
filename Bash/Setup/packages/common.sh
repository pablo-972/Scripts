#!/bin/bash

COMMON_TOOLS=(
    # NETWORKING
    curl
    wget
    net-tools
    iproute2
    dnsutils
    traceroute
    whois

    # SYSTEM UTILITIES
    unzip
    zip
    p7zip-full
    tar
    tree
    lsb-release
    jq
    xclip
    htop

    # DEV ESSENTIALS
    build-essential
    pkgconf
    python3
    python3-pip
    python3-dev

    # TERMINAL / PRODUCTIVITY
    neovim
    tmux
    bat

    # GIT
    git
)


install_common() {
    apt install -y "${COMMON_TOOLS[@]}"
}

uninstall_common() {
    apt remove -y "${COMMON_TOOLS[@]}"
}



