import os
import sys

import guiTextEditor as edit

def leave():
    sys.exit()

def read(filename):
    try:
        file = open(filename, "r")
        readfile = file.read()
        print(readfile)
    except Exception as e:
        print("There was an problem: %s" % (e))

def delete(filename):
    try:
        os.remove(filename)
        print(filename + " has been deleted!")
    except Exception as e:
        print("There was a problem: %s" % (e))


def rename(filename, new):
    try:
        os.rename(filename, new)
    except Exception as e:
        print("There was a problem: %s" % (e))
        
def write(filename):
    try:
        file = open(filename, "a")
        while True:
            append = input()
            if append.lower() == "save":
                break
            file.write(append)
            file.write("\n")
    except Exception as e:
        print("There was a problem: %s" % (e))

def cd(directory):
    try:
        current = os.getcwd()
        os.chdir(current + "\\" + directory)
    except Exception as e:
        print("There was a problem %s" % (e))

def cwd():
    print(os.getcwd())

def ls():
    print(os.listdir())

def findExtension(filename):
    atPeriod = False
    i = 0
    while i < len(filename):
        if filename[i] == ".":
            atPeriod = True
        if atPeriod:
            if filename[i] == " ":
                break
        i += 1
    return i

while True:
    do = input("What would you like to do? ")
    if do.startswith("cd"):
        cd(do[3:])
    elif do.startswith("read"):
        read(do[5:])
    elif do.startswith("aedit"):
        root = edit.Tk()
        app = edit.TextEditor(root)
        if "." in do:
            app.openFile(None, do[6:])
        app.mainloop()
    elif do.startswith("write"):
        write(do[6:])
    elif do.startswith("rename"):
        endOfFileName = findExtension(do)
        rename(do[7:endOfFileName], do[endOfFileName + 1:])
    elif do.startswith("delete"):
        delete(do[7:])
    elif do == "cwd":
        cwd()
    elif do == "ls":
        ls()
    elif do == "exit":
        leave()
    else:
        print("That is not a recognized command, please try again.")
