'''
NOTE:
    Windows defender, or other anti-virus programs may prevent you from running a
    uncertified executable.
    Make sure pip and pyinstaller are installed and updated
    otherwise make sure to activate the venv of the project, and use pip to install pyinstaller.
    The process is somewhat messy, so try to contain all the things needed in a folder on the desktop.
    The files are here for easy reference and copy-pasta

To convert a .py to a .exe
go to terminal/cmd
cd to directory that contains your .py file(copied the gui clock from GUI experiments
pyinstaller ...
    -F (all in 1 file)
    -w (removes terminal window)
    -i icon.ico (adds custom icon to .exe)
    clock.py (name of your main python file)
.exe is located in the dist folder

'''