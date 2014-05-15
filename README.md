notoj
=====

A simple note organizer.


Design
======

The idea is to make a command line interface that generates, serves and
searches a static site of some notes both in markdown and ipython notebook
files

Use pandoc for conversion, use ack for search, git for version control

 - notoj init - create a new note directory
 - notoj new <name> - create a new note
 - notoj git ... - pass command to git in the directory
 - notoj make ... - make html / latex
 - notoj search <query> - search the notes
 - notoj serve - serve the notes
 - notoj list - list all of the notes
 - notoj notebook - start a new ipython notebook
 - notoj view - simple previewer (terminal / html / pdf)

Layout of directory

 - input - all of the input files in arbitrary directories
 - output - all of the outputs

TODO
====

The goal is to have a simple way to organize my notes, should support markdown,
and ipython notebooks to start.  

Use pandoc for the conversions, with some nice styling, and ipython notebook
handling.

With a full text search feature.


