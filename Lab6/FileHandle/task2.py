import os

def checkPathAccess(path):
    if os.path.exists(path):
        print("Exists:    ","|", os.path.exists(path))
        print("Readable:  ",'|', os.access(path, os.R_OK))
        print("Writable:  ",'|', os.access(path, os.W_OK))
        print("Executable:",'|', os.access(path, os.X_OK))
    else:
        print("Path is not exist.")

checkPathAccess("c:\projects")
        
    
    