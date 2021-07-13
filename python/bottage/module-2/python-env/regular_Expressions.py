import fnmatch
import os

def list_files():
    for file in os.listdir('.'): 
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: ", file)

list_files()