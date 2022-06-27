import os
import time
import sys
import re
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#sys.argv[1] = File Source
#sys.argv[2] = File Destination
#sys.argv[3] = File Extension

from dataExtractor import getDataString

def onCreated(event):
    
    srcPath = event.src_path
    if os.path.isfile(srcPath):
        if sys.argv[3] in srcPath: 
            srcSplit = os.path.split(event.src_path)  
            #print (srcPath)
            
            #srcSplit[0] = path
            #srcSplit[0] = fileName

            os.popen(f"cp {srcPath} {sys.argv[2]}appbox-{srcSplit[1]}")


            #execStr = getDataString(srcPath, 'Exec') 
           # print (f"Name={execStr}")
           # subprocess.run(f"distrobox-export --app {execStr}  --export-path {sys.argv[2]}", shell=True) 


        # ToDo create appbox-Data file
        # check appbox-Data if app is exported
        # export app [ distrobox-export --app <AppName> --export-path sys.argv[2] ]
        #subprocess.run(f"distrobox-export --app {appName}  --export-path {sys.argv[2]}", shell=True)  
        #distrobox-export --app firefox -ep /home/user/Downloads/Main/

def onDeleted(event):
    if sys.argv[3] in event.src_path:   
        srcPath = os.path.split(event.src_path)
        print(f"File Deleted: {srcPath[1]}")
        # ToDo create appbox-Data file
        # check appbox-Data if app exists on host
        # delete appData file on host! [ distrobox-export --app <AppName> --delete  -ep sys.argv[2] ]


def onMoved(event):    
    destPath = os.path.split(event.dest_path)
    if sys.argv[3] in event.src_path:
        #print(f"{event.src_path}\n{event.dest_path}")         
        srcPath = os.path.split(event.src_path)
        destPath = os.path.split(event.dest_path)
        if srcPath[0] != destPath[0]:
            print(f"File {srcPath[1]} Moved \n From: {srcPath[0]} To: {destPath[0]}")
        if srcPath[1] != destPath[1]:
            print(f"File Renamed\nFrom: {srcPath[1]} To: {destPath[1]}")            
    elif ".txt" in destPath[1]:
         print(f"File Updated: {destPath[1]}")


def getWatchedDir():

    return sys.argv[1] # "/home/user/Downloads/Main/"

def getDestDir():

    return sys.argv[2] # "/home/user/Downloads/Main/"

def getFileExtension():

    return sys.argv[3] # "/home/user/Downloads/Main/"

if __name__ == "__main__":

    patterns = ["*"]
    ignorePatterns = None
    ignoreDirs = True
    caseSensitive = True
    handler = PatternMatchingEventHandler(patterns, ignorePatterns, ignoreDirs, caseSensitive)

    handler.on_created = onCreated
    handler.on_deleted = onDeleted
    handler.on_moved = onMoved

    
    
    

    watchedDir = getWatchedDir()

    observer = Observer()
    observer.schedule(handler, watchedDir, recursive=True)

    observer.start()

    #subprocess.run(f"sudo apt-get install gtkterm -y", shell=True) 

    try:
        if len(sys.argv) < 3:
            print("Missing file extention argument\n")
            exit(0)
        print(f"Python Watchdog Running in {watchedDir}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting!")
        observer.stop()
        observer.join()




