import os, sys
import json
import tkinter as tk
from tkinter import messagebox

debug = True

with open("serials.json", "r") as serial_json:
    serial_list = json.load(serial_json)

root = tk.Tk()
root.title("Serial Code Checker GUI")
photo = tk.PhotoImage(file = 'icon.png')
root.wm_iconphoto(False, photo)
root.geometry("400x300")

type_serial = tk.StringVar()
serial_int = tk.StringVar() # IntVar() bad


serial_type_options = [
    "XAW1", "XAW4", "XAW7",
    "XAJ1", "XAJ4", "XAJ7",
    "XKW1", "XKJ1", "XJW1",
    "XWW1", "XAW9", "XAK"
]

drop = tk.OptionMenu( root , type_serial , *serial_type_options )

def serial_compat(serial_type, serial_code):

    skip_check = False

    usrtype = serial_type
    usrcode = serial_code

    if usrtype in serial_type_options:
        match usrtype:
            case "XKW1" | "XKJ1":
                messagebox.showerror("Serial Checker", "You have a 'Mariko' switch, which has been patched unfortunately")
            case "XAK":
                messagebox.showwarning("Serial Checker", "You own a Korean nintendo switch, not much info is known about them, so it may or may not be patched.")
            case "XAW9":
                messagebox.showwarning("Serial Checker", "You own a refurbished Nintendo Switch sold directly from Nintendo, they're probably patched if it was refurbished before the switch's \n 'Mariko' mainline switch patch, however false positives have been more likely with these versions")
            case "XWW1":
                messagebox.showerror("Serial Checker", "Your Switch is 100% Patched")
                
        skip_check = True
        serial_invalid = False

    if skip_check == False:

        unpatched_range = []
        possibly_patched_range = []
        patched_range = []

        unpatched_range.append(serial_list[usrtype]['unpatched']['min'])
        unpatched_range.append(serial_list[usrtype]['unpatched']['max'])
        unpatched_range.append(usrtype + usrcode)

        possibly_patched_range.append(serial_list[usrtype]['possibly patched']['min'])
        possibly_patched_range.append(serial_list[usrtype]['possibly patched']['max'])
        possibly_patched_range.append(usrtype + usrcode)

        patched_range.append(serial_list[usrtype]['patched']['min'])
        patched_range.append(usrtype + usrcode)

        unpatched_range.sort() 
        # sort alphanumerically, if serial is inbetween it will go as item 2 [1] and therefore verify it
        # if it is entered as item 3 [2], then we try again with 'probably patched' and 'patched'
        possibly_patched_range.sort()
        patched_range.sort()

        if debug:
            print(unpatched_range)
            print(possibly_patched_range)
            print(patched_range)

        userserial = usrtype + usrcode

        if unpatched_range[1] == userserial:
            
            if possibly_patched_range[1] == userserial:
                print("Possibly patched from check 2")
                checktwofine = False
            else:
                print("No false positives found from check 2")
                checktwofine = True
                
            if patched_range[1] == userserial: # last item, since it will always be higher than the first if 100% patched
                print("Patched from check 3")
                checkthreefine = False
            else:
                print("No false positives found from check 3")
                checkthreefine = True
            
            # what amazing code i wrote (not)
            if checktwofine and checkthreefine:
                messagebox.showinfo("Serial Checker","Congrats, your switch isn't patched!\n (No issues found with double-checks either)")
            elif checktwofine and not checkthreefine:
                messagebox.showinfo("Serial Checker", "Check 1 and 2 determined that your switch wasn't patched, by check 3 suggested otherwise.\n Maybe try again or check your Switch\'s Serial Code.")
            elif checkthreefine and not checktwofine:
                messagebox.showinfo("Serial Checker", "Check 1 and 3 determined that your switch wasn't patched, by check 2 suggested otherwise.\n Maybe try again or check your Switch\'s Serial Code.")
            elif not checktwofine and not checkthreefine:
                messagebox.showinfo("Serial Checker", "Check 1 responded with an okay on the patch-ness of your serial code, but Checks 2 and 3 said otherwise.\n Try trying again incase you misentered your Serial Code or even check your Serial Code incase you got something wrong!")
            else:
                messagebox.showinfo("Serial Checker", "Error when parsing serial number")
        else:
            if possibly_patched_range[1] == userserial:
                messagebox.showwarning("Serial Checker","Your Switch is possibly patched")
            if patched_range[1] == userserial:
                messagebox.showerror("Serial Checker","Your Switch is most-likely patched")
            else:
                messagebox.showinfo("Serial Checker","Your Switch's patchness is Unknown")

    else:
        pass


def window_submit_serials():

    serial_type_submit = type_serial.get()
    serial_int_submit = serial_int.get()

    print(serial_type_submit)
    print(serial_int_submit)

    type_serial.set("")
    serial_int.set("")

    serial_compat(serialtype=serial_type_submit, serialcode=serial_int_submit)


serial_type_name = tk.Label(root, text = 'Serial Type', font=('calibre',10, 'bold'))
serial_type_entry = tk.Entry(root, textvariable = type_serial, font=('calibre',10,'normal'))

serial_int_name = tk.Label(root, text = 'Serial Number (6-10)', font = ('calibre',10,'bold'))
serial_int_entry = tk.Entry(root, textvariable = serial_int, font = ('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = window_submit_serials)

serial_type_name.grid(row=0, column=0)
drop.grid(row=0, column=1)
serial_int_name.grid(row=1, column=0)
serial_int_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()