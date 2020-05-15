from tkinter import *
import os
from resources_helper import *


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

# SSH checkbox
ssh_state = BooleanVar()
ssh_checkbox = Checkbutton(root, text="Enable SSH", variable=ssh_state)
ssh_checkbox.grid(columnspan=2, sticky=N+S, pady=6)

# Button
genButton = Button(root, text="Generate Files", command=lambda: write_files())
genButton.grid(columnspan=2, sticky=N+S, pady=6)

def getSupplicant():
    # Array should be initialized at write file calling
    # to get it properly filled with fext fields
    supplicant = f"""\
country={country.get()}
update_config=1
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

network={{
    ssid="{ssid.get()}"
    psk="{password.get()}"
}}
"""
    return supplicant


def write_file(lines, filename):

    f =  open(filename, "w+")
    f.writelines(lines) if type(list) == list else f.write(lines) # Compatible with \n formated array or multiline f-string
    f.close()
    createdLabel = Label(root, text=f'{filename} created')
    createdLabel.grid(columnspan=2, sticky=N+S, pady=6)


def write_files():
    # call the write function for all files
    write_file(getSupplicant(), "wpa_supplicant.conf")
    write_file('', "SSH") if (ssh_state.get()) else None # Create SSH file if checkbox enabled

root.mainloop()