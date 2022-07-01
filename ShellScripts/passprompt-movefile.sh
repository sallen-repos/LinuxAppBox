#!/bin/bash

# moves a file using sudo users priviledges

# takes the srcpath and the destPath of the file as args

srcPath=$1 

desPath=$2

SUDO_ASKPASS="zenity-askpass.sh" sudo -A mv $srcPath $desPath

# not sure why .desktop files is executable without chmod +x

# but there is no need to implement such a command 

exit 0

# this is achieved using zenity

# zenity provides a gui interface for command line applications and scripts

# linappbox is not a CLI program but it's privileged tasks are scripts
