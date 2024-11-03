#!/bin/bash

#SETUP FOR KALI LINUX ~
apt update; apt upgrade;

#ZSH
curl https://raw.githubusercontent.com/pablo-972/Scripts/refs/heads/main/Kali%20Setup/.zshrc > ~/.zshrc

#DIRECTORIES
mkdir Tools;
mkdir HTB;

#SOME APPS & TOOLS
#xclip
apt install xclip;

#batcat
apt install bat;

#Visual Studio Code
wget -O code.deb 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64';
dpkg -i code.deb;
rm code.deb;

#Protonvpn
wget https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.4_all.deb;
sudo dpkg -i ./protonvpn-stable-release_1.0.4_all.deb && sudo apt update;
sudo apt install proton-vpn-gnome-desktop;
rm protonvpn-stable-release_1.0.4_all.deb;

#Ghidra
apt install ghidra;

chistory;
