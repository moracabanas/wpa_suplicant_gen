import os
import platform

oper = platform.system()

if(oper == "Windows"):
    ico_cmd = "icon.ico;."
else:
    ico_cmd = "icon.ico:."


os.system(f"pyinstaller --onefile --noconsole --name=HeadlessGenerator --icon=icon.ico main.py --add-data {ico_cmd}")