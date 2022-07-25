IMPORTANT!!

==============================================================
                       APPHUB IS ONLY WORKING ON ARCH GUESTS 
                            ON VERSIONS ADAPTED FOR EXPORT 
                              WE AIM TO FIX THIS ISSUE SHORTLY
==============================================================

==============================================================
ENVIRONMENT
==============================================================

The Application needs preconfiguration to work.

The Application requires a Linux environment to run

The Projects folder must be cloned directly into the users home directory!

use cd $HOME before cloning!

==============================================================
DEPENDENCIES
==============================================================

It has downstream dependencies such as distrobox, podman and fastfetch
These must me pre installed on the guest system to run!!

Podman must be in rootless mode!

==============================================================
SETUP
==============================================================

The following configuration steps must be taken

using distrobox the user must create some guests via a distrobox using the following commands

distrobox create --image docker.io/library/ubuntu:latest --pull --yes --name ubuntu

distrobox create --image docker.io/debian:latest --pull --yes --name debian

distrobox create fedora --pull --yes --name fedora

==============================================================
EXECUTION
==============================================================


The contents of the folder urs/share/applications must be extracted into the  
/urs/share/applications on the users host machine for the application to view isntalled files!!


To run correctly the Application must be executed from the desktop, it cannot be executed from the terminal
To run the application outside of a terminal double click on the linux-appbox.desktop file!

If the guest app files have been correctly extracted they should be displayed in the iconview

==============================================================
Running AppHub on Host systems
==============================================================

AppHub-Apt can also be ran and tested on ubuntu host systems, without being launched in an AppBox guest

Enter its directory and type ./AppBox-Apt.sh to run on a ubuntu host.
