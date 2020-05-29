#!/usr/bin/env python3

import os
import argparse
import subprocess

from latedit.environment import generate_default_config, config_exists, DEFAULT_CONFIG_PATH


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g", 
        "--generate", 
        help="Generate a default environment configuration", 
        default=False, 
        action="store_true")
    parser.add_argument(
        "-f",
        "--force",
        help="Overwrites existing configuration when generating",
        default=False,
        action="store_true")
    parser.add_argument(
        "-s",
        "--show",
        help="Show the current environment configuration",
        default=False,
        action="store_true")
    parser.add_argument(
        "-e", 
        "--edit",
        help="Edit the current environment configuration",
        default=False,
        action="store_true")

    args = parser.parse_args()

    if args.generate:
        if config_exists() and not args.force:
            print("[!] Environment configuration already exists, and force overwrite not specified. Aborting.")
        else:
            generate_default_config() 
    elif args.show:
        if config_exists():
            with open(DEFAULT_CONFIG_PATH, "r") as f:
                data = f.read()
            print(data)
        else:
            print("[!] Environment configuration doesn't exist.")
    elif args.edit:
        if not config_exists():
            print("[!] Environment configuration doesn't exist.")
        else:
            editor = os.path.expandvars("$EDITOR")
            if editor == "$EDITOR":
                editor = "vi"
            subprocess.call([editor, DEFAULT_CONFIG_PATH]) 
