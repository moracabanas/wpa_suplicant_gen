from tkinter import *

root = Tk()

country = "es"
ssid = "2.4Ghz"
password = "4058520201"


supplicant = [
    f'country={country}\n',
    'update_config=1\n',
    'ctrl_interface=/var/run/wpa_supplicant\n',
    '\n'
    'network{\n',
    'scan_ssid=1\n',
    f'ssid="{ssid}"\n',
    f'psk="{password}"\n',
    '}'
]

def fileWrite():

    f =  open("wpa_supplicant.conf", "w+")
    f.writelines(supplicant)
    f.close()
    myLabel = Label(root, text="File created!")
    myLabel.pack()

myButton = Button(root, text="Generate", command=fileWrite)
myButton.pack()

root.mainloop()
