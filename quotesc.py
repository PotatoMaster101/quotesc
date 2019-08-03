#!/usr/bin/env python3
###############################################################################
# Escapes inner and outer quotes based on their position, example: 
# Input:  "abc"d"e"f"abc"
# Output: "abc\"d\\\"e\\\"f\"abc"
#
# Author: PotatoMaster101
# Date:   01/08/2019
###############################################################################

import argparse
import sys
import re

def get_args():
    """
    Returns the user arguments. 
    """
    p = argparse.ArgumentParser(description="Escape quotes.")
    p.add_argument("input", type=str, help="input string or file name")
    p.add_argument("-f", "--file", action="store_true", dest="fromf", 
            help="indicates that input string is a file name")
    p.add_argument("-r", "--reset-line", action="store_true", dest="resetl", 
            help="reset escape level on newline character")
    p.add_argument("-q", "--quote", type=str, default="\"", dest="quote", 
            help="the quote character, default to \"")
    p.add_argument("-l", "--level", type=get_pos, default=0, dest="lvl", 
            help="escape level, default to 0")
    p.add_argument("-o", "--output", type=str, default="", dest="outf", 
            help="output file name")
    return p


def get_pos(val):
    """
    Ensures that the user argument is a positive integer. 
    """
    ret = 0
    try:
        ret = int(val)
    except:
        raise argparse.ArgumentTypeError("%s is not an integer" %val)

    if ret < 0:
        raise argparse.ArgumentTypeError("%s is negative" %val)
    return ret


def get_input(args):
    """
    Returns the input based on user arguments. 
    """
    if not args.fromf:
        return args.input
    with open(args.input) as f:
        return f.read()


def get_esc_str(lvl=0, quote="\""):
    """
    Returns the escape string based on the level and quote character. 
    """
    lvl = (2 ** lvl) - 1        # compute escape level using 2^n - 1
    return ("\\" * lvl) + quote


def escape(inp, quote="\"", lvl=0):
    """
    Performs escaping and returns the output string. 
    """
    ite = list(re.finditer("\\\\*" + quote, inp))
    mid = len(ite) // 2
    odd = len(ite) % 2 != 0

    for i in range(len(ite) - 1, -1, -1):
        start, end = ite[i].start(), ite[i].end()
        inp = inp[:start] + get_esc_str(lvl, quote) + inp[end:]
        if odd or i != mid:     # don't put extra escape in mid if even
            lvl = lvl + 1 if i > mid else lvl - 1
    return inp


if __name__ == "__main__":
    """
    Entry point. 
    """
    args = get_args().parse_args()
    inp = get_input(args)
    out = open(args.outf, "w") if args.outf else sys.stdout
    if args.resetl:
        for l in inp.splitlines():
            print(escape(l, args.quote, args.lvl), file=out)
    else:
        print(escape(inp, args.quote, args.lvl), file=out)

    if args.outf:
        out.close()
    exit(0)

