from tkinter import sys
import os

# Handling icons and stuff from packed in .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # This allows you to get the generated TMP folder as the ./ path when you executes the built .exe
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# import resource_helper as rh
# Then set root.iconbitmap(default=rh.resource_path("icon.ico"))
# last step is packing the .exe with the following command:
#  pyinstaller --onefile --noconsole --icon=icon.ico main.py --add-data icon.ico;.
# icon source https://icon-icons.com/icon/raspberry-food/68696
########################################