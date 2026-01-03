#!/bin/bash

# SETUP FOR KALI LINUX ~
echo -e "\e[33mSETUP FOR KALI LINUX ~\e[0m";
apt update -y && apt upgrade -y;


# ZSH
cp .zshrc ~


# DIRECTORIES
mkdir /home/kali/HTB;
mkdir /home/kali/tools;
mdkir /home/kali/tools/SecLists
mkdir /home/kali/tools/bloodhound
mkdir /home/kali/tools/windows
mkdir /home/kali/tools/kerbrute


# TOOLS
# neovim
apt install neovim -y;
# xclip
apt install xclip -y;
# jq
apt install jq -y
# batcat
apt install bat -y;
# gobuster
apt install gobuster -y;
# SecLists
git clone https://github.com/danielmiessler/SecLists.git /home/kali/tools/SecLists;
# Bloodhound
curl -L https://ghst.ly/getbhce > /home/kali/tools/bloodhound/docker-compose.yml # To execute: docker pull &&  docker compose up
# Kerbrute
git clone https://github.com/ropnop/kerbrute.git /home/kali/tools/kerbrute;
apt install golang-go -y;
cd /home/kali/tools/kerbrute;
go build -ldflags "-s -w" .;
# RunasCs
cd /home/kali/tools/windows;
wget https://github.com/antonioCoco/RunasCs/releases/download/v1.5/RunasCs.zip;
unzip RunasCs.zip;
rm RunasCs.zip;
# SharpGPOAbuse
curl -L -o SharpGPOAbuse.exe https://github.com/byronkg/SharpGPOAbuse/raw/main/SharpGPOAbuse-master/SharpGPOAbuse.exe;
# PKINIT && Pywhisker
git clone https://github.com/dirkjanm/PKINITtools && git clone https://github.com/ShutdownRepo/pywhisker
#Ghidra
#apt install ghidra;


#APPS
#Visual Studio Code
wget -O code.deb 'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64';
dpkg -i code.deb;
rm code.deb;
#Protonvpn
#wget https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.4_all.deb;
#sudo dpkg -i ./protonvpn-stable-release_1.0.4_all.deb && sudo apt update;
#sudo apt install proton-vpn-gnome-desktop;
#rm protonvpn-stable-release_1.0.4_all.deb;


echo -e "\e[31mSETUP FINISHED!! ENJOY ;)\e[0m";

