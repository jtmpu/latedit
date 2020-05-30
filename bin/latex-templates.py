#!/usr/bin/env python3

import os
import sys
import json
import argparse
import subprocess

from latedit.environment import load_latedit_environment
from latedit.templates import get_jinja_environment, list_templates, get_template

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--list",
        help="List available templates",
        default=False,
        action="store_true")
    parser.add_argument(
        "-s",
        "--show",
        help="Show the specified template",
        default="")
    parser.add_argument(
        "-e",
        "--edit",
        help="Edit the specified template. If the specified templates doesn't exist, creates a new with the given name",
        default="")
    parser.add_argument(
        "-r",
        "--render",
        help="Render the specified template with the JSON data given in 'data' or 'STDIN'. Defaults to reading from STDIN.",
        default="")
    parser.add_argument(
        "-d",
        "--data",
        help="The JSON structure to use for rendering a template",
        default="")
    parser.add_argument(
        "--no-data",
        help="Dont use any data when rendering template",
        default=False,
        action="store_true")

    args = parser.parse_args()

    env = load_latedit_environment()

    if args.list:
        templates = list_templates(env)

        for t in templates:
            sys.stdout.write("{}\n".format(t))

    elif args.show != "":
        available = list_templates(env)

        if args.show in available:
            t = get_template(env, args.show)
            with open(t.filename, "r") as f:
                data = f.read()

            sys.stdout.write(data)
        else:
            print("[!] Template '{}' not found.".format(args.show))

    elif args.edit != "":
        editor = os.path.expandvars("$EDITOR")
        if editor == "$EDITOR":
            editor = "vi"

        j = get_jinja_environment(env)
        if args.edit in j.list_templates():
            t = get_template(env, args.edit)
            subprocess.call([editor, t.filename])
        else:
            folder = j.loader.searchpath[0]
            path = os.path.join(folder, args.edit) 
            subprocess.call([editor, path])
    elif args.render != "":
        j = get_jinja_environment(env)
        if args.render not in j.list_templates():
            print("[!] Template not found.")
            sys.exit(-1) 

        rawdata = ""
        if args.data == "" and not args.no_data:
            rawdata = sys.stdin.read() 
        else:
            rawdata = args.data

        t = j.get_template(args.render)
        if args.no_data:
            output = t.render()
        else:
            data = json.loads(rawdata) 
            output = t.render(data=data)

        sys.stdout.write(output)
