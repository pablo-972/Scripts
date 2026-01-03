#!/bin/bash

GREEN='\033[0;32m'
BLUE='\033[0;34m'
WHITE='\033[1;37m'
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
RESET='\033[0m'


echo -e "${WHITE}"
echo "##########################################################################"
echo -e "${YELLOW}"
echo "_________              .__                                         "
echo "\_   ___ \ __ _________|  | ___.__."
echo "/    \  \/|  |  \_  __ \  |<   |  |"
echo "\     \___|  |  /|  | \/  |_\___  |"
echo " \______  /____/ |__|  |____/ ____|"
echo "        \/                  \/      "
echo -e "${WHITE}"
echo "##########################################################################"
echo -e "${RESET}"
echo -e "By Sulkaz\n"

# How to use it
usage() {
    echo -e "Usage: $0 -u <url> -l <route_list> [-c] [-s]\n"
    echo "Options:"
    echo "  -u    url"
    echo "  -l    route_list file"
    echo "  -c    content of the response"
    echo "  -s    only status of the response"
    echo "  -h    help"
    exit 1
}

# Default variables
show_content=1
show_status=0

# Arguments
while getopts ":h:u:l:cs" opt; do
    case $opt in
        u) url=$OPTARG ;;
        l) route_list=$OPTARG ;;
        c) show_content=1 ;;
        s)
            show_status=1
            show_content=0
            ;;
        h) usage ;;
        \?)
            echo "Invalid option: -$OPTARG"
            usage
            ;;
    esac
done

# Verify arguments
if [ -z "$url" ] || [ -z "$route_list" ]; then
    echo "ERROR: Both URL and route list must be specified."
    usage
fi

if [ ! -f "$route_list" ]; then
    echo "ERROR: Route list file does not exist: $route_list"
    exit 1
fi

# Starting curl-enumeration
echo -e "${YELLOW}[+] Starting curl-enumeration...${RESET}\n"

while IFS= read -r route; do
    if [ -z "$route" ]; then
        continue
    fi

    # Concatenate url with route
    full_url="${url}${route}"
    echo -e "\n"
    echo -e "${WHITE}CURL request: ${BLUE}$full_url${RESET}"

    # ---- CURL STATUS ----
    if [ $show_status -eq 1 ]; then
        http_code=$(curl -s -o /dev/null -w "%{http_code}" "$full_url")

        # Color based on HTTP status code range
        if [[ $http_code -ge 100 && $http_code -lt 200 ]]; then
            echo -e "${CYAN}[${http_code}] ${full_url}${RESET}"
        elif [[ $http_code -ge 200 && $http_code -lt 300 ]]; then
            echo -e "${GREEN}[${http_code}] ${full_url}${RESET}"
        elif [[ $http_code -ge 300 && $http_code -lt 400 ]]; then
            echo -e "${ORANGE}[${http_code}] ${full_url}${RESET}"
        elif [[ $http_code -ge 400 && $http_code -lt 500 ]]; then
            echo -e "${RED}[${http_code}] ${full_url}${RESET}"
        elif [[ $http_code -ge 500 && $http_code -lt 600 ]]; then
            echo -e "${YELLOW}[${http_code}] ${full_url}${RESET}"
        else
            echo -e "${WHITE}[${http_code}] ${full_url}${RESET}"
        fi
    fi

    # ---- CURL CONTENT ----
    if [ $show_content -eq 1 ]; then
        curl -s "${full_url}"
    fi

done < "$route_list"

echo -e "\n"
echo -e "${GREEN}Enumeration completed.${RESET}"



    



