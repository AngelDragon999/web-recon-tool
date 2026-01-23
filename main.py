#!/usr/bin/env python3

"""
Web Recon Tool
Author: AngelDragon999
Description: Simple tool for reconnaissance web
"""

# Libraries
import argparse
from  utils import info, section, item, warn
from dns_recon import dns_recon
from subdomain_enum import enumerate_subdomains

def main():
    
    # Parsers for imput command from command line
    parser = argparse.ArgumentParser(
        description="Simple Web Recon Tool"
    )

    # Arguments that SW accetps -d / --domain
    parser.add_argument(
        "-d",
        "--domain",
        required=True,
        help="Target domain (example.com)"
    )

    # Read arguments
    args = parser.parse_args()

    # Save domain in input
    domain = args.domain

    # Starting message
    info(f"\n[+] Starting reconnaissance on: {domain}\n")

    # Print title of this program
    section("DNS RECORDS")

    # Call my method for dns recon
    dns_recon(domain)

    # Control for subdomains
    section("SUBDOMAINS")

    with open("subdomains.txt") as file:
        words = [line.strip() for line in file]

    subdomains = enumerate_subdomains(domain, words)

    if subdomains:
        for subdomain in subdomains:
            item(subdomain)
    else:
        warn("Mamma mia! No subdomains found!")

# Starting main method

if __name__ == "__main__":
    main()     