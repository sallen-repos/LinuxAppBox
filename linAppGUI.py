import gi
import subprocess
import multiprocessing
import os
import glob
import re

from dataExtractor import extractData
from PIL import Image

gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk
from gi.repository.GdkPixbuf import Pixbuf

#TODO store globals list in a config file, perhaps use strings for keylist is they are immutable?

#list of tags used in desktop entry files, 
keyList = [ 'Name', 'Categories', 'Exec', 'Icon', 'Actions' ]

#default directory for desktop entry file location
desktopEntryDir = "/usr/share/applications/"

dictionary = {}

class WindowMain():

    def __init__(self):

        # Get GUI Glade file
        self.builder=Gtk.Builder()
        self.builder.add_from_file("linappGUI.glade")
        self.builder.connect_signals(self)
        self


        # Display main window
        self.windowMain=self.builder.get_object("window_main")
        self.windowMain.show_all()

        scrolledwindow = self.builder.get_object("scrolled_window")

        #listStore = Gtk.ListStore(Pixbuf, str, str, str) list_store
        desktopEntryData = getMetadataDictionary(desktopEntryDir, keyList)
        listStore = populateListStore(self.builder.get_object("list_store"),desktopEntryData, 0)      
        iconView = self.builder.get_object("icon_view")
        iconView.set_model(listStore)
        iconView.set_pixbuf_column(0)
        iconView.set_text_column(1)
        iconView.set_tooltip_column(2)
        iconView.set_text_column(3)    
        
    def item_activated(self,listStore, treePath):
        
        execCmd = f"nohup {listStore[treePath][1]} &"       #nohup and disown seems like overkill 
                                                             #but it isn't overkill with chromium!
        subprocess.run(f"{execCmd}", shell=True)  
        subprocess.run("disown -ah", shell=True) 
      

    def launchUbuntu():     
        subprocess.run("killall gnome-software", shell=True)
        subprocess.run("podman kill ubuntu", shell=True) 
#TODO maybe don't kill ubuntu maybe check if running and launch app w/ or w/o db-enter
        subprocess.run(""" distrobox enter ubuntu -- bash -l -c '"gnome-software"' """, shell=True)  
#for some reason `-- bash` needs the space

    def launchFedora():
        subprocess.run("killall gnome-software", shell=True)    
        subprocess.run("podman kill fedora", shell=True)
        subprocess.run(""" distrobox enter fedora -- bash -l -c '"gnome-software"' """, shell=True)

      
    
    def on_window_main_destroy(self, widget, data=None):
        print("on_window_main_destory")
        Gtk.main_quit()


    def on_ubuntu_clicked(self, widget, t1=multiprocessing.Process(target=launchUbuntu)):
        t1.daemon = True
        t1.start()

    def on_fedora_clicked(self, widget, t2=multiprocessing.Process(target=launchFedora)):
        t2.daemon = True
        t2.start() 

    def on_btn3_clicked(self, widget, data=None):
        print("btn3_clicked")  


        
    def main(self):
        Gtk.main()

#calls on the extractData module to extract desktop entry file data, this is metadata about guest apps
def getMetadataDictionary(directory, keyList):
    
    metadataDictionary = {}    
    iterator = glob.iglob(f"{directory}appbox-*.desktop")  #searches for files prefixed with appbox- with the .desktop file extention
    for path in iterator :
        
        if path not in metadataDictionary: #TODO metadataDictionary is not going to have prior data under current set up and will be empty      
            data = extractData(keyList, path)
            if data != {}:
                metadataDictionary.update( {f'{path}': data} )                

    return metadataDictionary

#populates listStore with details from application meta data
#It also stores an application icon image to the listStore which along with the details can then be displayed in the gtk iconView
def populateListStore(listStore, data, count):
    
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
                pixelBuffer = Gtk.IconTheme.get_default().load_icon(iconStr, 48, 0)

            lable = data[path]["Name"][0].replace(" (AppBox)", "")

            execCmd = re.sub(' %u','',data[path]["Exec"][0], flags=re.IGNORECASE)
                     
            listStore.append([pixelBuffer, f"{execCmd}", "tool-tip", lable]) #
                
        except:
            print (f"")

    return listStore


if __name__ == "__main__":
    application=WindowMain()
    application.main()
