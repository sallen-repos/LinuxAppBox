import re
import gi
import os
 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#dataDictionary = {'Categories': '', 'Exec': '', 'Icon': '', 'Actions': '' }
# Extracts relevant data from .desktop files
# .desktop files contain app metadata on xdg conforming desktop systems 
# xdg/freedesktop: (most linux desktop environments fully comply, all most all partially comply or have compatibility modules)

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



def categoryIsUnsuitable(categoryStr):  
    categories = [ "Accessories", "Development", "Games", "Game", "Graphics", "Internet", "Multimedia", "Office", "Settings", "System", "Wine", "WebBrowser", "Email", "Calculator", "FileTransfer", "TextEditor", "DesktopSettings", "AudioVideo", ]  
    if categoryStr.find(';') > -1:        
        catList = categoryStr.split(';')
        for cat in catList:
            for category in categories:                        
                if category == cat:                            
                    return False        
    else:
        catItem = [f"{categoryStr}"] 
        for category in categories:                        
            if category == catItem:
                return False
    print(f"catList ={categoryStr}")
    return True 

def desktopEntry(keyList, filePath):
    
    with open(filePath) as desktopFile:  
        for lineNum, line in enumerate(file):   # Get line of file
            if "[Desktop Entry]" in line:
                return extractdata(keyList, filePath)

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

                    #if key == "Categories":
                    #    if categoryIsUnsuitable(newValue):
                    #        success = False
                    #else:
                    #print(line)
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
        #print (fileData)
        return data

#def extractData(keyList, filePath):
#    data = {}
#    with open(filePath) as desktopFile:       # Open file 
#        for line in desktopFile:                            # Get line of file
#            for key in keyList:                      # Get key of data dictionary
#               
#                entry = re.findall(f"^{key}=", line)           # Regex search line of file for a string that matches data dictionary key
#                # when a match is found: remove line end, and remove the key to give a newValue to record in data dictionary 
#                if entry:                                                           
#                    removeEndLine = line.replace('\n','')                
#                    newValue = re.sub(r'^.*?=', '', removeEndLine) 
#                    print(line)
#                    #check if there is a current value in data dictionary
#                    currentValue = str(data.get(key))              
#                    #if key == "Icon":
#                     #   if iconIsMissing(key): 
#                      #      newValue = "None"
#                    if newValue != "None":
#
#                        if currentValue != "None":                     
#                            #removeDoubles = re.sub(';;', ';', f'{currentValue};{newValue};')     # If there is a current value append into a ';' semi-colon separated string
#                                                                                             # replacing duplicates ';;' with single ';' while ending with a ''''; consistent with xdg format
#                            #data.update({f'{key}': f"[{removeDoubles}]"})                       # update data dictionary.
#                            data[key].append(newValue)
#                        else:    
#                            listItem = [f"{newValue}"]          
#                            data[key] = listItem 
#        print (data)
#        return data


def checkCategory(filePath):




    with open(filePath) as desktopFile:       # Open file 
        for line in desktopFile:                            # Get line of file

            # Regex search line of file for a string that matches data dictionary key
            category = re.findall("^Categories=", line)
            #print(rawValue)
            if category:                                             
# when a match is found: remove line end, and remove the key to give a newValue to record in data dictionary
                removeEndLine = line.replace('\n','') 
                newValue = re.sub(r'^.*?=', '', removeEndLine)
                values = newValue.split(';')

                        #else:
                           # print(f"{value} != {category}" )
        return False

def checkTheCategory(category):
    if not category:
                    success = False
      #fill if used




def extractIconData(key, filePath):
    #data = None
    #print ("HERE")
    data = {}
    with open(filePath) as desktopFile:       # Open file 
        for line in desktopFile:                            # Get line of file

                      # Get key of data dictionary
            entry = re.findall(f"^{key}=", line)           # Regex search line of file for a string that matches data dictionary key
            category = re.findall("^Category=", line)
                     
            if entry:                                             # when a match is found: remove line end, and remove the key to give a newValue to record in data dictionary
                removeEndLine = line.replace('\n','') 
                newValue = re.sub(r'^.*?=', '', removeEndLine)
                
                success = False
                iconName = newValue
                try:      
                    pixbuf = Gtk.IconTheme.get_default().load_icon(iconName, 48, 0)
                    success = True               
                except gi.repository.GLib.Error:
                    print("System Icon not Found")
                if not checkCategory(filePath):
                    success = False
                if success == True:
                    data[key] = newValue 
                else:
                    data[key] = "firefox"
                
        #print (data)
        return data


#print(extractedData)
