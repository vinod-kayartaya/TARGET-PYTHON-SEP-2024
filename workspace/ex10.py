#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

from myutils import csv2json
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="A utitlity for converting CSV file to JSON file.")

    parser.add_argument("--input", required=True, help="an existing CSV filename")
    parser.add_argument("--output", default=None, help="a new JSON filename; existing file will be overwritten")

    # args = vars(parser.parse_args())
    # csv2json(args['input'], args['output'])

    args = parser.parse_args()
    csv2json(args.input, args.output)


if __name__ == '__main__':
    main()
