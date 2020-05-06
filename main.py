from tkinter import *
import os
# Handling icon from packed icon in .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Then set root.iconbitmap(default=resource_path("icon.ico"))
# last step is packing with the following command:
#  pyinstaller --onefile --noconsole --icon=icon.ico main.py --add-data icon.ico;.

########################################

root = Tk() 
root.title("Headless Generator")
root.iconbitmap(default=resource_path("icon.ico"))

Label(root, text="Insert your country code ie: US").pack()
country = Entry(root)
country.pack()
ssid = "2.4Ghz"
password = "4058520201"

def write_file(lines, filename):

    f =  open(filename, "w+")
    f.writelines(lines)
    f.close()
    myLabel = Label(root, text=f'{filename} created')
    myLabel.pack()


def update_write():
    #first update array
    supplicant = [
        f'country={country.get()}\n',
        'update_config=1\n',
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n',
        '\n'
        'network={\n',
        #'scan_ssid=1\n',
        f'  ssid="{ssid}"\n',
        f'  psk="{password}"\n',
        '}'
    ]

    #call the write function
    write_file(supplicant, "wpa_supplicant.conf")


genButton = Button(root, text="Generate Files", command=lambda: update_write())
genButton.pack()

root.mainloop()