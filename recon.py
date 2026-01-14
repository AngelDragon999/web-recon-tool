#!/usr/bin/env python3

"""
Web Recon Tool - Skeleton
Author: AngelDragon999
Description: Simple tool for reconnaissance web
"""

# Libraries
import argparse
import sys

def main ():
    
    # Parsers for imput command from command line
    parser = argparse.ArgumentDefaultsHelpFormatter(
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

# Starting main method

if __name__ == "__main__":
    main()     