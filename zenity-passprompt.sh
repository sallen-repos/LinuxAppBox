#!/bin/bash


SUDO_ASKPASS="zenity-askpass.sh" sudo -A rm $1

SUDO_ASKPASS="zenity-askpass.sh" sudo -A touch $1

SUDO_ASKPASS="zenity-askpass.sh" sudo -A sh -c "echo "$2" | sudo tee -a "$1" >/dev/null"

exit 0
