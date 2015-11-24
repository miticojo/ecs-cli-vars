#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import os.path
import argparse

__author__ = "Giorgio Crivellari <miticojo@gmail.com>"
__version__ = "1.0"

def compose_replace(filePath):
    with open(filePath, "r") as composeFile:
        str = composeFile.read()
    for key, val in os.environ.iteritems():
        try:
            str = str.replace("${%s}" % key, val)
        except: pass
    return str


def main():
    if len(sys.argv) == 1:
        print("WARNING: \n",
              "This script substitutes ${VARIABLE} in Docker compose file with OS environment variables.\n" \
              "Usage: ecs-cli-vars.py -f <docker-compose.yml>" \
              "Version: %s" % __version__,
              file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--compose-file", help="pass docker-compose.yml")
    args = parser.parse_args()
    if not os.path.isfile(args.compose_file):
        print("ERROR: \n",
              "Docker compose file %s, doesn't exist." % args.compose_file,
              file=sys.stderr)
        sys.exit(2)

    print(compose_replace(args.compose_file))


if __name__ == "__main__":
    main()
