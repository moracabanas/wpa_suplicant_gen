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

# Labels and Text entry
countryLabel = Label(root, text="Country code")
countryLabel.grid(column=0, row=0, pady=6, padx=12)
country = Entry(root)
country.insert(0, "US")
country.grid(column=1, row=0, pady=6, padx=12)

ssidLabel = Label(root, text="Network SSID ")
ssidLabel.grid(column=0, row=1, pady=6, padx=12)
ssid = Entry(root)
ssid.grid(column=1, row=1, pady=6, padx=12)

passwordLabel = Label(root, text="Network password")
passwordLabel.grid(column=0, row=2, pady=6, padx=12)
password = Entry(root)
password.grid(column=1, row=2, pady=6, padx=12)
########################


genButton = Button(root, text="Generate Files", command=lambda: update_write())
genButton.grid(columnspan=2, sticky=N+S, pady=6)


def write_file(lines, filename):

    f =  open(filename, "w+")
    f.writelines(lines)
    f.close()
    createdLabel = Label(root, text=f'{filename} created')
    createdLabel.grid(columnspan=2, sticky=N+S, pady=6)


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