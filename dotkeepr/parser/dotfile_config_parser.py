#!/usr/bin/python

# System Imports
import ConfigParser

# Project Imports
from model import dotfile_resource

def read_config_file_into_list(configFile):
    parser = ConfigParser.ConfigParser(allow_no_value=True)
    parser.read(configFile)

    dotfiles = []

    for section_name in parser.sections():
        #print 'Section: ', section_name
        #print 'Options: ', parser.options(section_name)
        for dotfilePath in parser.options(section_name):
            #print '%s' % (dotfilePath)
            resource = dotfile_resource.DotfileResource(dotfilePath)
            dotfiles.append(resource)

    return dotfiles
