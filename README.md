

==============================================================
                                                    IMPORTANT!
==============================================================
The program is in "early alpha" and needs very specific 
==============================================================
ENVIRONMENT
==============================================================

The Application needs preconfiguration to work.

The Application requires a Linux environment to run

The Projects folder must be cloned directly into the users HOME DIRECTORY!
If this is not done the expected file paths will be incorrect.

so use 'cd $HOME' before cloning!

The contents of the folder urs/share/applications must be copied into the host machines
 $HOME/.local/share/applications/ 

If this does not happen, the tools to install new applications will not be available.

The user must have read and write permissions to this file and all its contents

==============================================================
DEPENDENCIES
==============================================================

It has downstream dependencies in distrobox, podman 
These must me pre installed on the guest system to run!!

Distrobox is available from here

https://github.com/89luca89/distrobox

Podman must be installed and is supported by most linux repositories

Podman must be in rootless mode!

Instructions on this are placed at the bottom of this page


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





To run correctly the Application must be executed from the desktop, it cannot be executed from the terminal
To run the application outside of a terminal double click on the linux-appbox.desktop file!

If the guest app files have been correctly extracted they should be displayed in the iconview

==============================================================
Running AppHub on Host systems
==============================================================

AppHub-Apt can also be ran and tested on ubuntu host systems, without being launched in an AppBox guest

Enter its directory and type ./AppBox-Apt.sh to run on a ubuntu host.




==============================================================
ROOTLESS PODMAN
==============================================================
Rootless Podman
Warning: Rootless Podman relies on the unprivileged user namespace usage (CONFIG_USER_NS_UNPRIVILEGED) which has some serious security implications, see Security#Sandboxing applications for details.
By default only root is allowed to run containers (or namespaces in kernelspeak). Running rootless Podman improves security as an attacker will not have root privileges over your system, and also allows multiple unprivileged users to run containers on the same machine. See also podman(1) § Rootless mode.

Additional dependencies
The following packages are required to run Podman in a rootless environment:

fuse-overlayfs
slirp4netns
Enable kernel.unprivileged_userns_clone
First, check the value of kernel.unprivileged_userns_clone by running:

$ sysctl kernel.unprivileged_userns_clone
If it is currently set to 0, enable it by setting 1 via sysctl or kernel parameter.

Note: linux-hardened has kernel.unprivileged_userns_clone set to 0 by default.
Set subuid and subgid
In order for users to run rootless Podman, a subuid(5) and subgid(5) must be set for each user that wants to use it. These information must, ultimately, be stored in /etc/subuid and /etc/subgid which lists the UIDs for their user namespace.

/etc/subuid and /etc/subgid do not exist by default. If they do not exist yet in your system, create them by running:

# touch /etc/subuid /etc/subgid
Note: The above command is required, because the usermod used below do not create them.
The following command enables the username user and group to run Podman containers (or other types of containers in that case). It allocates a given range of UIDs and GIDs to the given user and group.

# usermod --add-subuids 100000-165535 --add-subgids 100000-165535 username
Tip: Instead of using usermod command, this could be achieved either by editing /etc/subuid and /etc/subgid directly.
Now, you should have the following content (replacing username with the given username):

/etc/subuid
username:100000:65536
/etc/subgid
username:100000:65536


