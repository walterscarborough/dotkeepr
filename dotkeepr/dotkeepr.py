#!/usr/bin/python

# Project Imports
from parser import dotfile_config_parser

config_file = '../config/config.ini'

dotfiles = dotfile_config_parser.read_config_file_into_list(config_file)

for resource in dotfiles:
    resource.create_symlink()

print 'DotKeepr saved the day again. Enjoy!'
