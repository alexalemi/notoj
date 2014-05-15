#! /usr/bin/env python
"""
A simple note organizer, taker

 - notoj init - create a new note directory
 - notoj new <name> - create a new note
 - notoj git ... - pass command to git in the directory
 - notoj make ... - make html / latex
 - notoj search <query> - search the notes
 - notoj serve - serve the notes
 - notoj list - list all of the notes
 - notoj notebook - start a new ipython notebook
 - notoj view - simple previewer (terminal / html / pdf)
"""

import os
import click
from config import settings

class Config(object):
    def __init__(self, **kwargs):
        self.__dict__.update(settings)
        self.__dict__.update(kwargs)

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.pass_context
def notoj(ctx, **kwargs):
    ctx.obj = Config(**kwargs)

# show configuration
@notoj.command()
@pass_config
def conf(config):
    click.echo(config.__dict__)

# initialize the directory
@notoj.command()
@pass_config
def init(config):
    click.echo(config.path)
    click.echo("INIT")

# Create a new note
@notoj.command()
@pass_config
def new(config):
    click.echo("New")

# edit existing note
@notoj.command()
@pass_config
def edit(config):
    click.echo("edit")

# run a git command
@notoj.command()
@pass_config
def git(config):
    click.echo("git")

# make the output
@notoj.command()
@pass_config
def make(config):
    click.echo("make")

# search for a note
@notoj.command()
@pass_config
def search(config):
    click.echo("search")

# serve the static site
@notoj.command()
@pass_config
def serve(config):
    click.echo("serve")

# list all of the notes
@notoj.command()
@pass_config
def ls(config):
    click.echo("ls")

# create a new ipython notebook
@notoj.command()
@pass_config
def notebook(config):
    click.echo("notebook")

# view a note in the browser
@notoj.command()
@pass_config
def view(config):
    click.echo("view")

if __name__ == "__main__":
    notoj()
