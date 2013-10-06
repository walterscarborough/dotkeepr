        ____        __  __
       / __ \____  / /_/ /_____  ___  ____  _____
      / / / / __ \/ __/ //_/ _ \/ _ \/ __ \/ ___/
     / /_/ / /_/ / /_/ ,< /  __/  __/ /_/ / /
    /_____/\____/\__/_/|_|\___/\___/ .___/_/
                                  /_/


Dotkeepr helps manage dotfiles that are kept under revision control. It will automagically create symlinks for all specified files in your dotfiles folder so that they link up to your home directory.

## Setup
First, you'll need to specify where your dotfiles are located and which ones you'd like dotkeepr to link.

    vim <dotkeepr repo location>/config/config.ini

The config file is a simple python configuration file. Make sure to enter a section header and the dotfile location. Using relative paths? No problem! Here's an example:

    [Bash]
    ~/.dotfiles/bash/bashrc
    ~/.dotfiles/bash/bash_profile

    [Vim]
    ~/.dotfiles/vim/vimrc
    ~/.dotfiles/vim

## Usage
Assuming that you're in the dotkeepr repo directory, just run the following:

    python dotkeepr.py

## License
Copyright (c) 2013 Walter Scarborough. Licensed under the GPL v3 license.
