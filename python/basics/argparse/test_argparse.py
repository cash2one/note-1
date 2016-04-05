#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


# Optional arguments

parser = argparse.ArgumentParser()

parser.add_argument("--verbosity", help="increase output verbosity")

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")


args = parser.parse_args()
if args.verbosity:
    print args.verbosity
    print "verbosity turned on"
if args.verbose:
    print args.verbose
    print "verbosity turned on"
