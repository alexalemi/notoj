#! /usr/bin/env python
"""
A simple note organizer, taker

 - notoj init - create a new note directory

    * can optionally handle notebooks
 - notoj new <name> - create a new note
 - notoj copy
 - notoj move
 - notoj delete
 - notoj edit - edits an existing thing

 - notoj serve - serve the notes
 - notoj view - simple previewer (terminal / html / pdf)
 - notoj search <query> - search the notes
 - notoj list - list all of the notes

 - notoj git ... - pass command to git in the directory
 - notoj make ... - make html / latex
 - notoj grep ... - run grep

 - notoj conf - edit configuration
 - notoj --version
 - notoj --help
"""

import os
import argparse
import subprocess
from config import settings


def usage(args):
    parser.print_usage()

# FUNCTIONS
def init(args):
    """ Initialize the repo, create the directory and populate with
    a skeleton, make a git repository and do the first commit """
    print "init"


def git(args):
    """ Run git commands in the appropriate directory """
    print "git"
    print args.git_args

# PARSERS
parser = argparse.ArgumentParser(prog='notoj')
parser.set_defaults(**settings)
parser.add_argument('--path',type=str)
parser.add_argument('--version',action='version',version='%(prog)s 0.1')
# parser.set_defaults(func=usage)

subparsers = parser.add_subparsers(title='subcommands')

parser_init = subparsers.add_parser('init', help='initialize note repo')
parser_init.set_defaults(func=init)

parser_git = subparsers.add_parser('git', help='run git commands in repo dir')
parser_git.add_argument('git_args', metavar='git-args', nargs=argparse.REMAINDER)
parser_git.set_defaults(func=git)



# MAIN
if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)

