#! /bin/bash

# creates a temporary .desktop file

# which is the passed on to zenity-passprompt-copyfile.sh

# where the user is prompted for a password as copying to destPath is protected

# takes the guest system name and host terminal command as args


guest=$1

destPath="/usr/share/applications/${guest}-0terminal.desktop"

touch tempfile.desktop

cat > tempfile.desktop << EOL
[Desktop Entry]
Name=${guest} Terminal
Type=Application
Encoding=UTF-8
Comment=CLI Terminal Emulator
X-MultipleArgs=false
Hidden=true
Exec=sh $HOME/Projects/LinuxAppBox/ShellScripts/Guest-Terminal ${guest} %U
Icon=utilities-terminal
Categories=System;TerminalEmulator;
Terminal=true
GenericName=${guest} Terminal"
EOL

sh passprompt-movefile.sh tempfile.desktop $destPath
