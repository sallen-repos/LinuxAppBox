import subprocess
import multiprocessing
import os
import guestAppWatchdog

#sys.argv[1] = File Source
guestAppsDir = "/usr/share/applications/"
#sys.argv[2] = File Destination
localGuestAppsDir = "/home/user/Projects/LinuxAppBox/GuestAppFiles/"
#sys.argv[3] = File Extension
fileExtenstion = ".desktop"

#TODO

#Take distrobox input with all possible vars

#command Distrobox to create guest.

#used by GUI and start up scrips

#GUI has defauls and also custom input

#scripts install a basic image as INIT is working as hoped

# Input can be
#--init-hooks <command>
#--pre-init-hooks <command>


def distroboxCreateImage(imageURI, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --image {imageURI} {init} --pull --yes --name {name} {preInitHooks} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxCreateClone(srcPath, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --clone {srcPath} {init} --pull --yes --name {name} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxRemoveImage(name):

    subprocess.run(f"distrobox-rm {name} --yes --force", shell=True)

def distroboxEnter(command, args):

    subprocess.run(f"distrobox-enter {args} {name}", shell=True)

def distroboxList():

    subprocess.run(f"distrobox-list", shell=True)

def distroboxList(name):

    subprocess.run(f"distrobox-stop {name} --yes", shell=True)

def execute(command):

    subprocess.run(f"{command}", shell=True)
   



#distroboxCreate("docker.io/debian:latest", "debian", "","","","","")

#distroboxRemoveImage("rock")

#distroboxEnter("","debian")

