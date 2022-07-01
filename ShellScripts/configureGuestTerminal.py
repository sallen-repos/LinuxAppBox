import subprocess
import sys
import os

# configure a desktop entry file that launches a host system terminal and launches a guest

# the guest terminal will dispay a welcome message for the users

# runs script to get host

# runs scripts to prompt user for password and copy files to restricted location

# most code was implemented in shell scripts as getting sudo priviledges was easier



from sudo import run_as_sudo

def main (guest):

    hostTerminal = subprocess.Popen(['sh Host-Terminal'],
 stdout=subprocess.PIPE,
 stderr=subprocess.PIPE,
 shell=True).communicate()[0].decode('utf-8').strip()

 # string the desktop file is built on was moved to shell scripts to avoid passing a python to sh 
 # (predictably painfull) especially didn't help that .desktop files requires line breaks
 # line breaks require carefull consideration in shell scripts 

    subprocess.Popen([f'sh createDesktopGuestTerminal.sh {guest} {hostTerminal}'],
 stdout=subprocess.PIPE,
 stderr=subprocess.PIPE,
 shell=True)

main(sys.argv[1])
