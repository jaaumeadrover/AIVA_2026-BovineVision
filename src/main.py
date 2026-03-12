"""
Script: main.py
Author: Jaume Adrover
Date: 3/11/2026

Description:
This script performs [brief description of purpose].

Usage:
python main.py [--options]

Dependencies:
- argparse
- 
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="[script description]")
    # parser.add_argument('--example', type=str, help='Example argument')
    args = parser.parse_args()

    # Your code here
    print("Hello world!")


if __name__ == "__main__":
    main()
