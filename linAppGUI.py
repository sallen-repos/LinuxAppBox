import gi
import glob
import os
import re
import subprocess
from dataExtractor import extractData
from PIL import Image

 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf


keyList = [ 'Name', 'Categories', 'Exec', 'Icon', 'Actions' ]

desktopEntryDir = "/usr/share/applications/"

dictionary = {}


def getMetadataDictionary(directory, keyList):
    
    metadataDictionary = {}    
    iterator = glob.iglob(f"{directory}appbox-*.desktop")
    for path in iterator :
        
        if path not in metadataDictionary: #print(path) #TODO metadataDictionary is not going to have prior data anymore)            
            data = extractData(keyList, path)
            if data != {}:
                metadataDictionary.update( {f'{path}': data} )                


    return metadataDictionary

def getIconDictionary(key, directory):

    iconDictionary = {}
    iterator = glob.iglob("/usr/share/applications/*.desktop")
    for path in iterator :       

        iconData = extractIconData(key, path)
        if iconData != {}:
            iconDictionary.update( {f'{path}': extractIconData(key, path)} )

    return iconDictionary

data = getMetadataDictionary(desktopEntryDir, keyList)


class IconViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title ="AppBox")
        self.set_default_size(800, 100)

        
        scrolledwindow = Gtk.ScrolledWindow()

        listStore = Gtk.ListStore(Pixbuf, str, str, str)
        iconView = Gtk.IconView(model=listStore)
        iconView.set_model(listStore)
        iconView.set_pixbuf_column(0)
        iconView.set_text_column(1)
        iconView.set_tooltip_column(2)
        iconView.set_text_column(3)


        scrolledwindow.add(iconView)
        # scrolledwindow.set_policy(Gtk.POLICY_NEVER, Gtk.POLICY_AUTOMATIC)


        c = 0
        for fname in data:
            c += 1
            if c > 24:
               break
            
            try:
                iconStr = data[fname]["Icon"][0]
                #cat = data[fname]["Categories"][0]
                if iconStr[0] == '/':
                    if os.path.isfile(iconStr):                    
                        pixelBuffer = Image.open(iconStr)

                else:    
                    pixelBuffer = Gtk.IconTheme.get_default().load_icon(iconStr, 48, 0)

                lable = data[fname]["Name"][0].replace(" (AppBox)", "")
                execCmd = re.sub(' %u','',data[fname]["Exec"][0], flags=re.IGNORECASE)
                #print(f"{execute}")          
                listStore.append([pixelBuffer, f"{execCmd}", "tool-tip", lable])
                
            except:
                print (f"")
           
        self.add(scrolledwindow)

        

    def item_activated(iconV, listStore):
        i = iconV.get_selected_items()[0]  #note the subscript to get list item 0, to return index of selcted item

        execCmd = f"nohup {listStore[i][1]} &"       #nohup and disown seems like overkill 
                                                             #but it isn't overkill with chromium!
        subprocess.run(f"{execCmd}", shell=True)  
        subprocess.run("disown -ah", shell=True) 
      
      

win = IconViewWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
