import subprocess
import multiprocessing
import os


#TODO

#Take distrobox input with all possible vars

#command Distrobox to create guest.

#used by GUI and start up scrips

#GUI has defauls and also custom input

#scripts install a basic image as INIT is working as hoped

# Input can be
#--init-hooks <command>
#--pre-init-hooks <command>


def distroboxCreateImage(source, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --image {source} {init} --pull --yes --name {name} {preIniteHooks} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxCreateClone(origional, name, init, preInitHooks, initHooks, volume, additionalFlags):

    subprocess.run(f"distrobox-create --clone {origional} {init} --pull --yes --name {name} {initHooks} {volume} {additionalFlags}", shell=True)

def distroboxRemoveImage(name):

    subprocess.run(f"distrobox-rm {name} --yes --force", shell=True)

def distroboxEnter(command, args):

    subprocess.run(f"distrobox-enter {args} {name}", shell=True)

def distroboxList():

    subprocess.run(f"distrobox-list", shell=True)

def distroboxList(name):

    subprocess.run(f"distrobox-stop {name} --yes", shell=True)



#distroboxCreate("docker.io/debian:latest", "debian", "","","","","")

#distroboxRemoveImage("rock")

#distroboxEnter("","debian")

