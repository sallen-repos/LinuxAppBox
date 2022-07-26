import sys
import subprocess
from distroboxInterface import distroboxCreateImage
from configureGuestTerminal import configureTerminal

def main (guest):



#distrobox create --image docker.io/debian:latest --pull --yes --name debian

#distrobox create fedora --pull --yes --name fedora

#distrobox create --image docker.io/library/archlinux:latest --pull --yes --name arch
#distrobox enter arch -e 'pacman -syu zenity'
   

main(sys.argv[1])


