#!/usr/bin/env python3

import argparse

from latedit.environment import load_document_environment
from latedit.document import list_texfiles

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l", 
        "--list", 
        help="List files in document.",
        default=False,
        action="store_true")

    args = parser.parse_args()

    if args.list:
        env = load_document_environment()
        print(list_texfiles(env)) 
