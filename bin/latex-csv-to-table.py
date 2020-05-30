#!/usr/bin/env python3

import os
import sys
import argparse

from latedit.csv import parse_csv
from latedit.environment import load_latedit_environment
from latedit.templates import get_jinja_environment

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "-t",
        "--has-header",
        help="Parse the first row as the header row",
        default=False,
        action="store_true")
    parser.add_argument(
        "-f", 
        "--file", 
        help="The file to read the CSV from. If not specified, reads from STDIN.",
        default="")

    args = parser.parse_args()

    csvdata = ""
    if args.file == "":
        csvdata = sys.stdin.read()
    else:
        if not os.path.exists(args.file):
            print("[!] File not found: {}".format(args.file))
            sys.exit(-1)

        with open(args.file, "r") as f:
            csvdata = f.read()

    try:
        table = parse_csv(csvdata, args.has_header)
    except Exception as e:
        print("[!] {}".format(e))
        sys.exit(-1)

    lenv = load_latedit_environment()
    env = get_jinja_environment(lenv) 

    data = {}
    data["table"] = table
    tmpl = env.get_template("table.j2")
    output = tmpl.render(data=data)

    sys.stdout.write(output)
