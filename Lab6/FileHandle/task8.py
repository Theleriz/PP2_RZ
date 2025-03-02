import os

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted.")
        else:
            print(f"Cannot delete '{path}'.")


