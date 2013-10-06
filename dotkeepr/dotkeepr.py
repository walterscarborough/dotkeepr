#!/usr/bin/python

# System Imports
import os

# Project Imports
from parser import dotfile_config_parser

base_path = os.path.dirname(__file__)
config_file = os.path.abspath(os.path.join(base_path, '../config/config.ini'))

dotfiles = dotfile_config_parser.read_config_file_into_list(config_file)

for resource in dotfiles:
    resource.create_symlink()

print 'DotKeepr saved the day again. Enjoy!'
