import sys
import subprocess
from distroboxInterface import distroboxCreateImage
from configureGuestTerminal import configureTerminal

def main (guest):


distrobox create --image docker.io/library/ubuntu:latest --pull --yes --name ubuntu

distrobox create --image docker.io/debian:latest --pull --yes --name debian

distrobox create fedora --pull --yes --name debi
   

main(sys.argv[1])


