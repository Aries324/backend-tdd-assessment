#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Tiffany McLean"

import argparse
import sys
import subprocess


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def func_no_args(text):
    output = subprocess.check_output(['python', 'echo.py', text])
    return output.rstrip()


def main(args):

    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(3)

    namespace = parser.parse_args(args)
    text = namespace.text

    if namespace.upper:
        text = text.upper()
    if namespace.lower:
        text = text.lower()
    if namespace.title:
        text = text.title()

    return text


if __name__ == "__main__":
    result = main(sys.argv[1:])
    print(result)
