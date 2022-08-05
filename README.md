

==============================================================
                                                    IMPORTANT!
==============================================================
IF THE DEPENDENCIES ARE NOT SET UP ON YOUR MACHINE, DOWNLOAD
 A VIRTUAL MACHINE FROM MEDIAFIRE LINK

https://www.mediafire.com/folder/8rmmuixyppms4/Virtual_Machines

The qcow2 image can be launched using qemu/kvm the VHDK is converted from the qcow2
and hopefully can be run in VMware or VirtualBox (though I haven't been able to test this)

Inside the virtual machine navigate to /home/guest/Projects/Project/LinuxAppBox

open terminal and pull latest version of the project

Double click on the .desktop file in the LinuxAppBox folder to launch the application

When the application starts a guests applications should be displayed

Click on a guest, debian, arch to display applications (though the fedora guest image has no
applications currently and the content delivery system is a work in progress)

Double click on the AppHub app icon to launch AppHub to install and remove
applications
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

It has downstream dependencies in distrobox, podman, and zenity
These must be pre installed on the HOST system to run!!

Distrobox is available from here

https://github.com/89luca89/distrobox

zenity can be installed from most official repositories

Podman can be installed and is supported by most linux repositories

Podman must be in rootless mode!

Instructions on this are placed at the bottom of this page

==============================================================
                                                               SETUP
==============================================================

To set up AppBox on you machine, (without using a virtual machine)

The following configuration steps must be taken

using distrobox the user must create some guests via a distrobox using the following commands

distrobox create --image docker.io/debian:latest --pull --yes --name debian

distrobox create --image docker.io/library/archlinux:latest --pull --yes --name arch

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
Installing Podman

https://podman.io/getting-started/installation

Rootless Podman

Warning: Rootless Podman relies on the unprivileged user namespace usage (CONFIG_USER_NS_UNPRIVILEGED) which has some serious security implications, see Security#Sandboxing applications for details.
By default only root is allowed to run containers (or namespaces in kernelspeak). Running rootless Podman improves security as an attacker will not have root privileges over your system, and also allows multiple unprivileged users to run containers on the same machine. See also podman(1) § Rootless mode.

Additional dependencies
The following packages are required to run Podman in a rootless environment:

fuse-overlayfs
slirp4netns
Enable kernel.unprivileged_userns_clone
First, check the value of kernel.unprivileged_userns_clone by running:

The slirp4netns package provides user-mode networking for unprivileged network namespaces and must be installed on the machine in order for Podman to run in a rootless environment. The package is available on most Linux distributions via their package distribution software such as yum, dnf, apt, zypper, etc. If the package is not available, you can build and install slirp4netns from GitHub.
Ensure fuse-overlayfs is installed

When using Podman in a rootless environment, it is recommended to use fuse-overlayfs rather than the VFS file system. For that you need the fuse-overlayfs executable available in $PATH.

Your distribution might already provide it in the fuse-overlayfs package, but be aware that you need at least version 0.7.6. This especially needs to be checked on Ubuntu distributions as fuse-overlayfs is not generally installed by default and the 0.7.6 version is not available natively on Ubuntu releases prior to 20.04.

The fuse-overlayfs project is available from GitHub, and provides instructions for easily building a static fuse-overlayfs executable.

If Podman is used before fuse-overlayfs is installed, it may be necessary to adjust the storage.conf file (see "User Configuration Files" below) to change the driver option under [storage] to "overlay" and point the mount_program option in [storage.options] to the path of the fuse-overlayfs executable:

[storage]
  driver = "overlay"

  (...)

[storage.options]

  (...)

  mount_program = "/usr/bin/fuse-overlayfs"

Enable user namespaces (on RHEL7 machines)

The number of user namespaces that are allowed on the system is specified in the file /proc/sys/user/max_user_namespaces. On most Linux platforms this is preset by default and no adjustment is necessary. However, on RHEL7 machines, a user with root privileges may need to set that to a reasonable value by using this command: sysctl user.max_user_namespaces=15000.
/etc/subuid and /etc/subgid configuration

Rootless Podman requires the user running it to have a range of UIDs listed in the files /etc/subuid and /etc/subgid. The shadow-utils or newuid package provides these files on different distributions and they must be installed on the system. Root privileges are required to add or update entries within these files. The following is a summary from the How does rootless Podman work? article by Dan Walsh on opensource.com

For each user that will be allowed to create containers, update /etc/subuid and /etc/subgid for the user with fields that look like the following. Note that the values for each user must be unique. If there is overlap, there is a potential for a user to use another user's namespace and they could corrupt it.

cat /etc/subuid
<username>:100000:65536
<test>:165536:65536

The format of this file is USERNAME:UID:RANGE

    username as listed in /etc/passwd or in the output of getpwent.
    The initial UID allocated for the user.
    The size of the range of UIDs allocated for the user.

This means the user johndoe is allocated UIDs 100000-165535 as well as their standard UID in the /etc/passwd file. NOTE: this is not currently supported with network installs; these files must be available locally to the host machine. It is not possible to configure this with LDAP or Active Directory.

If you update either /etc/subuid or /etc/subgid, you need to stop all the running containers owned by the user and kill the pause process that is running on the system for that user. This can be done automatically by using the podman system migrate command which will stop all the containers for the user and will kill the pause process.

Rather than updating the files directly, the usermod program can be used to assign UIDs and GIDs to a user.

usermod --add-subuids 100000-165535 --add-subgids 100000-165535 <username>
grep <username> /etc/subuid /etc/subgid
/etc/subuid:<usernema>:100000:65536
/etc/subgid:<username>:100000:65536

# touch /etc/subuid /etc/subgid
Note: The above command is required, because the usermod used below do not create them.
The following command enables the username user and group to run Podman containers (or other types of containers in that case). It allocates a given range of UIDs and GIDs to the given user and group.

# usermod --add-subuids 100000-165535 --add-subgids 100000-165535 username
Tip: Instead of using usermod command, this could be achieved either by editing /etc/subuid and /etc/subgid directly.
Now, you should have the following content (replacing username with the given username):

/etc/subuid
<username>:100000:65536
/etc/subgid
<username>:100000:65536


