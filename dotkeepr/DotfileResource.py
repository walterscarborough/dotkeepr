#!/usr/bin/python

# System Imports
import os

class DotfileResource:

    def __init__(self, dotfilePath):
        self.symlinkPath = '~/.' + os.path.basename(dotfilePath)
        self.dotfilePath = dotfilePath

    def createSymlink(self):

        if os.path.islink(os.path.expanduser(self.symlinkPath)):
            os.unlink(os.path.expanduser(self.symlinkPath))

        os.symlink(os.path.expanduser(self.dotfilePath),  os.path.expanduser(self.symlinkPath))

        print 'Set symlink for: %s -> %s' % (self.symlinkPath, self.dotfilePath)

        return
