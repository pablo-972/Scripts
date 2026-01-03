# SMTP builder

This script is designed to generate a list of email addresses from a list of usernames by appending a domain to each one. 
The primary purpose is to allow the verification of whether users exist on a given SMTP server using the **VRFY** command to check if email accounts exist.

## Description

The script takes three parameters:
- A list of usernames (text file).
- An email domain (e.g., `example.com`).
- An output file to save the generated email addresses.

## Requirements

This script is written in Python 3. Make sure you have Python 3 installed on your machine.

## Usage

```bash
python SMTPbuilder.py -l <user_list.txt> -d <domain.com> -o <output_file.txt>
```
