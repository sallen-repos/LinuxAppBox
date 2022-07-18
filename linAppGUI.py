import gi
import subprocess
import multiprocessing
import os
import glob
import re
import sys

from subprocess import Popen, PIPE
from dataExtractor import extractData
from PIL import Image

gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk
from gi.repository.GdkPixbuf import Pixbuf

#TODO store globals list in a config file, perhaps use strings for keylist is they are immutable?

#https://askubuntu.com/questions/342950/how-do-i-create-a-desktop-entry-to-launch-a-python-script do /bin/ suggestion
#list of tags used in desktop entry files, 
keyList = [ 'Name', 'Categories', 'Exec', 'Icon', 'Actions' ]

#default directory for desktop entry file location

defaultAppDir =  "/usr/share/applications/"

#subprocess.call(['sh', './hide-terminal.sh', '{terminalWindowId}', '&']) #("nohup  sh /home/user/Projects/LinuxAppBox/hide-terminal.sh {terminalWindowId} &") #(['sh', './hide-terminal.sh', '{terminalWindowId}'])

dictionary = {}

def fillIconView(windowMain, desktopEntryData, listStore):
    scrolledwindow = windowMain.builder.get_object("scrolled_window")

    #listStore = Gtk.ListStore(Pixbuf, str, str, str) list_store   
    fullListStore = populateListStore(listStore,desktopEntryData, 0)      
    iconView = windowMain.builder.get_object("icon_view")
    iconView.set_model(fullListStore)
    iconView.set_pixbuf_column(0)
    iconView.set_text_column(1)
    iconView.set_tooltip_column(2)
    iconView.set_text_column(3)   



def getUserTerminal(line):
    
    #string = re.findall(r'^[^ ]+', line)

    print ( line )


def onButtonClicked(self):

    label = self.get_label()
    print (f"{label}") 
    return "done"    

def addButton(windowMain,num, name, command):

    grid = windowMain.builder.get_object("button_grid")

    button = Gtk.Button(label=f"{name}")
    button.connect("clicked", onButtonClicked)
    grid.add(button)
    grid.insert_row(num)
    grid.attach(button, 0, num, 1, 1)

def initButtons(windowMain):


        
    addButton(windowMain, 1, "Debian", "")
    addButton(windowMain, 2, "OpenSuse", "")
    addButton(windowMain, 3, "Arch", "")


class WindowMain():

    def __init__(self):

        #proc = Popen("xdotool getactivewindow", stdout=PIPE, stderr=PIPE, shell=True) 
        #out, err = proc.communicate()
        #exitcode = proc.returncode
        #out = subprocess.call("xdotool getactivewindow", shell=True)
        #print (err)
       # print (out)
       # print (exitcode)
        #subprocess.call("xdotool windowunmap {out}", shell=True)

        # Get GUI Glade file
        self.builder=Gtk.Builder()
        self.builder.add_from_file("linappGUI.glade")
        self.builder.connect_signals(self)
                
        # Display main window
        self.windowMain=self.builder.get_object("window_main")
        self.windowMain.show_all()
        


        guestOneAppData = getMetadataDictionary(defaultAppDir, "appbox", keyList)

        listStore = self.builder.get_object("list_store")
        fillIconView(self, guestOneAppData, listStore)
        
        grid = self.builder.get_object("button_grid")
        num = 0
        name = "Ubuntu"
        button = Gtk.Button(label=f"{name}")
        #button.connect("clicked", onButtonClicked)
        grid.add(button)
        #grid.insert_row(num)
        #grid.attach(button, 0, num, 1, 1)
         
        #initButtons(self)


        print (getIconThemePath("firefox"))
        
    def item_activated(self,listStore, treePath):
        
        execCmd = f"{listStore[treePath][1]}"       #nohup and disown seems like overkill 
                                                             #but it isn't overkill with chromium!
        os.popen(f"{execCmd}")  
        #subprocess.run("disown -ah", shell=True) 
      

#    def launchUbuntu():     
 #       subprocess.run("killall gnome-software", shell=True)
  #      subprocess.run("podman kill ubuntu", shell=True) 
#TODO maybe don't kill ubuntu maybe check if running and launch app w/ or w/o db-enter
#        subprocess.run(""" distrobox enter ubuntu -- bash -l -c '"gnome-software"' """, shell=True)  
#for some reason `-- bash` needs the space

#    def launchFedora():
 #       subprocess.run("killall gnome-software", shell=True)    
  #      subprocess.run("podman kill fedora", shell=True)
   #     subprocess.run(""" distrobox enter fedora -- bash -l -c '"gnome-software"' """, shell=True)

      
    
    def on_window_main_destroy(self, widget, data=None):
        print("on_window_main_destory")
        Gtk.main_quit()


#    def on_ubuntu_clicked(self, widget):
#        guestAppData = getMetadataDictionary(defaultAppDir, "ubuntu", keyList)
#        listStore =  self.builder.get_object("list_store")
#        listStore.clear()
#        fillIconView(self, guestAppData, listStore)


#    def on_fedora_clicked(self, widget):
#        guestAppData = getMetadataDictionary(defaultAppDir, "fedora", keyList)
#        listStore =  self.builder.get_object("list_store")
#        listStore.clear()
#        fillIconView(self, guestAppData, listStore)

#    def on_btn3_clicked(self, widget):
#        listStore =  self.builder.get_object("list_store")
#        listStore.clear()

#        guestAppData = getMetadataDictionary(defaultAppDir, "ubuntu", keyList)        
#        fillIconView(self, guestAppData, listStore)

#        guestAppData = getMetadataDictionary(defaultAppDir, "fedora", keyList)        
#        fillIconView(self, guestAppData, listStore)

        #print (terminalName)
        #subprocess.Popen([terminalName, '-e', 'sh /usr/local/bin/ello'])
        #subprocess.call("xdotool key ctrl+shift+n; sh /usr/local/bin/ello; xdotool key Return", shell=True)
        #subprocess.Popen([sys.executable, "/usr/local/bin/ello"], shell=True)
        
        #os.system("xdotool key ctrl+shift+n; sh /usr/local/bin/ello; xdotool key Return")
        #subprocess.call("sh /usr/local/bin/ello", shell=True) #xdotool key "ctrl+shift+t"; xdotool type "ls"; xdotool key Return



#xdotool key "ctrl+shift+t"; xdotool type "ls"; xdotool key Return

        #os.popen("/usr/local/bin/ello")
        #guestAppData = getMetadataDictionary(defaultAppDir,"appbox", keyList)
        #fillIconView(self, guestAppData) `

#    def on_ubuntu_clicked(self, widget, t1=multiprocessing.Process(target=launchUbuntu)):
#        t1.daemon = True
#        t1.start()

#    def on_fedora_clicked(self, widget, t2=multiprocessing.Process(target=launchFedora)):
#        t2.daemon = True
#        t2.start() 

#    def on_btn3_clicked(self, widget, data=None):
#        print("btn3_clicked")  
        
    def main(self):
        Gtk.main()

#calls on the extractData module to extract desktop entry file data, this is metadata about guest apps
def getMetadataDictionary(directory, prefix, keyList):
    
    metadataDictionary = {}    
    iterator = glob.iglob(f"{directory}{prefix}-*.desktop")  #searches for files prefixed with appbox- with the .desktop file extention
    for path in iterator :
        
        if path not in metadataDictionary: #TODO metadataDictionary is not going to have prior data under current set up and will be empty      
            data = extractData(keyList, path)
            if data != {}:
                metadataDictionary.update( {f'{path}': data} )                

    return metadataDictionary

#populates listStore with details from application meta data
#It also stores an application icon image to the listStore which along with the details can then be displayed in the gtk iconView
def populateListStore(listStore, data, count):
    listStore.clear()
    
    for path in data:
        count += 1
        if count > 24:
           break
            
        try:
            iconStr = data[path]["Icon"][0]
            if iconStr[0] == '/':
                if os.path.isfile(iconStr):                    
                    pixelBuffer = Image.open(iconStr)

            else:    
                print (iconStr)
                pixelBuffer = Gtk.IconTheme.get_default().load_icon(iconStr, 48, 0)

            lable = data[path]["Name"][0].replace(" (AppBox)", "")  #remove the (appBox) tag from app name

            execCmd = re.sub(' %u','',data[path]["Exec"][0], flags=re.IGNORECASE)
                     
            listStore.append([pixelBuffer, f"{execCmd}", "tool-tip", lable]) #
                
        except:
            print (f"")

    return listStore

def getIconThemePath(iconName):

    iconTheme = Gtk.IconTheme.get_default()
    iconInfo = iconTheme.lookup_icon(iconName, 48, 0)
    
    #if iconInfo != None:
        #filePath, filename = os.path.split(iconInfo.get_filename())
    return iconInfo.get_filename()

if __name__ == "__main__":
    application=WindowMain()
    application.main()
