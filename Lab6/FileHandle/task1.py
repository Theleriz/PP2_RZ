import os

def listContents(path):
   
    all_items = os.listdir(path)
    full_paths = [os.path.join(path, item) for item in all_items]
        
    directories = [item for item in full_paths if os.path.isdir(item)]
    files = [item for item in full_paths if os.path.isfile(item)]
        
    print("Directories:")
    for directory in directories:
        print(directory)
        
    print("Files:")
    for file in files:
        print(file)


listContents('C:\projects')



