#!/usr/bin/env python3

import sys
import argparse

from latedit.encode import latex_encode

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Data to encode, otherwise reads from STDIN.", default="") 
    args = parser.parse_args()

    data = ""
    if args.data != "":
        data = args.data
    else:
        data = sys.stdin.read()

    encoded = latex_encode(data)
    sys.stdout.write(encoded)
