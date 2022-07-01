import subprocess
import sys


#writes a desktop entry file that launches a host system terminal and launches a guest

#a fast fetch command will be launched by guest terminal script

def main (guest):


    hostTerminal = subprocess.Popen(['sh Host-Terminal'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0].decode('utf-8').strip()

    template = f"[Desktop Entry]\n\
Version=1.0\n\
Name={guest} Terminal\n\
Type=Application\n\
Encoding=UTF-8\n\
Comment=CLI Terminal Emulator\n\
X-MultipleArgs=false\n\
Hidden=true\n\
Exec={hostTerminal} -e 'sh /home/user/Projects/LinuxAppBox/Guest-Terminal {guest}' %U\n\
Icon=utilities-terminal\n\
Categories=System;TerminalEmulator;\n\
Terminal=true\n\
GenericName={guest} Terminal"

    print (template)

   #TODO complete by implementing write to file
   #TODO capitalise first letter of guest for Name={name}

main(sys.argv[1])
