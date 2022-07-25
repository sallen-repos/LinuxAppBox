import os
import sys
from distroboxInterface import distroboxCreateImage


def main (guest):

    #distroboxCreateImage("docker.io/almalinux/8-base", f"{guest}", "", "", "", "", "")

    os.popen("python3 ShellScripts/configureGuestTerminal.py alma")

    #configureTerminal(f"{guest}")
   

main(sys.argv[1])


