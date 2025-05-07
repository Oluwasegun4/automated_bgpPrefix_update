# Automated BGP Prefix Update

This script automates the generation and application of prefix-lists on Cisco routers using the `bgpq4` utility. It is particularly useful for service providers or network engineers who need to regularly update router prefix-lists based on registered AS-SETs from IRR databases such as RADB.

## ✨ Features

- Uses `bgpq4` to query IRR databases and generate prefix-lists.
- Automatically connects to Cisco devices using SSH (via Netmiko).
- Applies the updated prefix-list configuration.
- Can be integrated into scheduled jobs or CI/CD pipelines for network automation.

## 🛠 Use Case

Automating the process of updating prefix-lists from an AS-SET:
- Keeps routing filters up to date.
- Reduces manual errors.
- Ensures compliance with IRR-registered objects.

Example:
- AS-SET: `AS-GOOGLE-FIBER`
- Output: Cisco-compatible prefix-list
- Applied directly to the router

## 📋 Requirements

- Python 3.x
- [Netmiko](https://pypi.org/project/netmiko/)
- `bgpq4` installed on the system

Install dependencies:

```bash
pip install netmiko
sudo apt install bgpq4  # or brew install bgpq4 on macOS
