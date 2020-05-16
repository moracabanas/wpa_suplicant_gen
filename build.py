import os
import platform

ico_cmd = "icon.ico;." if platform.system() == "Windows" else "icon.ico:."

os.system(f"pyinstaller --onefile --noconsole --name=HeadlessGenerator --icon=icon.ico main.py --add-data {ico_cmd}")