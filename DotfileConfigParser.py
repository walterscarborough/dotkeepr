#!/usr/bin/python

# System Imports
import ConfigParser

# Project Imports
#from DotfileResource import DotfileResource
import DotfileResource

def readConfigFileIntoList(configFile):
    parser = ConfigParser.ConfigParser(allow_no_value=True)
    parser.read(configFile)

    dotfiles = []

    for section_name in parser.sections():
        #print 'Section: ', section_name
        #print 'Options: ', parser.options(section_name)
        for dotfilePath in parser.options(section_name):
            #print '%s' % (dotfilePath)
            resource = DotfileResource.DotfileResource(dotfilePath)
            dotfiles.append(resource)

    return dotfiles
