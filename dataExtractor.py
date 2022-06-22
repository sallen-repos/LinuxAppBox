import re
import gi
import os
 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Extracts relevant data from .desktop files
# .desktop files contain app metadata on xdg conforming desktop systems 
# xdg/freedesktop: (most linux desktop environments fully comply, all most all partially comply or have compatibility modules)
# on systems that do not comply LinuxAppBox still makes use of these files for its own purposes
# on non-conforming systems guest apps may not be discoverable by the host operating system

#checks if icon is present on system
def iconIsMissing(iconName):
    if iconName[0] == '/':
        if os.path.isfile(iconName):
            print(f"System Icon {iconName} was Found") 
            return False
    try:
        pixbuf = Gtk.IconTheme.get_default().load_icon(iconName, 48, 0)
        if not pixbuf:
             print(f"System Icon {iconName} not Found") 
             return True
        return False               
    except gi.repository.GLib.Error:
        print(f"System Icon {iconName} not Found") 
        return True

#extracts data from desktop entry files
def extractData(keyList, filePath):
    data = {}
    with open(filePath) as desktopFile:       # Open file
        #check if there is a current value in data dictionary 
        if data.get(filePath) == None:
            pass  #If value exists there's no reason anything but identical data should be expected so pass to skip this file
        fileData = {}
        for line in desktopFile:   # Get line of file
            if "[Desktop Action" in line:
                return data

            for key in keyList:    # Get key of data dictionary
                success = False

                entry = re.findall(f"^{key}=", line)           # Regex search line of file for a string that matches data dictionary key

                if entry:                                        # when a match is found: remove line end, and remove the key to give a newValue to record in data dictionary
                    success = True
                    removeEndLine = line.replace('\n','')                
                    newValue = re.sub(r'^.*?=', '', removeEndLine)

                    if key == "Icon":
                        if iconIsMissing(newValue): 
                            success = False
           
                if success:
                         
                    if newValue != "None":
                        if newValue.find(';') > -1:
                            listItem = newValue.split(';')
                        else:
                            listItem = [f"{newValue}"]          
                        fileData[key] = listItem

                    data.update(fileData)

        return data


