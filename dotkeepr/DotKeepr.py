#!/usr/bin/python

# Project Imports
import DotfileConfigParser

configFile = 'config.ini'

dotfiles = DotfileConfigParser.readConfigFileIntoList('config.ini')

for resource in dotfiles:
    resource.createSymlink()

print 'DotKeepr saved the day again. Enjoy!'
