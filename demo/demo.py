"""
Script: demo.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/2/2026

Description:
This script performs [brief description of purpose].

Usage:
python demo.py [--options]

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
    print("Running demo.py")


if __name__ == "__main__":
    main()
