#!/usr/bin/env python3

"""
Web Recon Tool
Author: AngelDragon999
Description: Simple tool for reconnaissance web
"""

# Libraries
import argparse
import sys
import dns.resolver


def dns_recon(domain):
    print(f"\n[+] Recon for {domain}\n")

    records = ["A", "NS", "MX", "TXT"]

    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            for rdata in answers:
                print(f"{record}: {rdata}")
        except Exception:
            pass


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
    print(f"[+] Starting reconnaissance on: {domain}")

    # Call my method for dns recon
    dns_recon(domain)

# Starting main method

if __name__ == "__main__":
    main()     