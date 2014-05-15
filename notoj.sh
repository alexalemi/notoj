#!/usr/bin/env bash

# Copyright 2014 Alex Alemi <alexalemi@gmail.com>.
# This file is licensed under an MIT license

set -o pipefail

PREFIX="${NOTOJ_DIR:-$HOME/notoj}"

# sub commands

cmd_version() {
    echo "1.0"
}

cmd_usage() {
    echo "usage"
}

cmd_init() {
    echo "init"
}

cmd_new() {
}

cmd_edit() {
}

cmd_serve() {
}

cmd_notebook() {
}

cmd_view() {
}

cmd_conf() {
}

cmd_git() {
}

cmd_make() {
}

cmd_find() {
}

cmd_show() {
}

PROGRAM="${0##*/}"
COMMAND="$1"

case "$1" in
    init) shift;                cmd_init "$@" ;;
    help|--help) shift;         cmd_usage "$@" ;;
    version|--version) shift;   cmd_version "$@" ;;
    show|ls|list) shift;        cmd_show "$@" ;;
    find|search) shift;         cmd_find "$@" ;;
    grep) shift;                cmd_grep "$@" ;;
    edit) shift;                cmd_edit "$@" ;;
    new) shift;                 cmd_new "$@" ;;
    delete|rm|remove) shift;    cmd_delete "$@" ;;
    rename|mv) shift;           cmd_copy_move "move" "$@" ;;
    copy|cp) shift;             cmd_copy_move "copy" "@" ;;
    git) shift;                 cmd_git "$@" ;;
    *) COMMAND="show";          cmd_show "$@" ;;

esac
exit 0
