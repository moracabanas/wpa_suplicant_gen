from tkinter import sys
import os

# Handling icons and stuff from packed in .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # This allows you to get the generated TMP folder as the ./ path when you executes the built .exe
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Easy usage example:
# from resources_helper import *    <-- Use this import on your main
# Then set root.iconbitmap(default=resource_path("icon.ico")) /// on this excample root = Tk()
# Pack the .exe with the following command on your terminal:
# 'python build.py' it reads your os platform to run the adecuate build script for yout system

# ### More info ###
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/44352931#44352931
# icon source https://icon-icons.com/icon/raspberry-food/68696