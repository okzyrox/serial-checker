import json
import os, sys

serial_types = [
    "XAW1", "XAW4", "XAW7",
    "XAJ1", "XAJ4", "XAJ7",
]
serial_extra_types = [
    "XKW1", "XKJ1", "XJW1",
    "XWW1", "XAW9", "XAK"
]
#XKW and XKJ - Mariko switch's - patched
#XAK - korean only - unknown
#XAW9 - sold from nintendo directly via refurbishment - possibly patched, but mostly unpatched from data recorded

debug = True
skip_check = False

with open("serials.json", "r") as serial_json:
    serial_list = json.load(serial_json)


print("Valid First types")
for i in serial_types:
    print(i)
print("Other types")
for i in serial_extra_types:
    print(i)

serial_invalid = True

while serial_invalid:
    usrtype = input("Enter the first four letters/numbers of your Nintendo Switch's serial code: ")

    if usrtype.isupper():
        pass
    else:
        usrtype = usrtype.upper()

    print("Entered:", usrtype)

    if usrtype in serial_types:
        serial_invalid = False
    elif usrtype in serial_extra_types:
        match usrtype:
            case "XKW1" | "XKJ1":
                print("You have a 'Mariko' switch, which has been patched unfortunately")
            case "XAK":
                print("You own a Korean nintendo switch, not much info is known about them, so it may or may not be patched.")
            case "XAW9":
                print("You own a refurbished Nintendo Switch sold directly from Nintendo, they're probably patched if it was refurbished before the switch's \n 'Mariko' mainline switch patch, however false positives have been more likely with these versions")
            case "XWW1":
                print("Your Switch is 100% Patched")

        skip_check = True
        serial_invalid = False       
    else:
        print("Invalid Serial Code")

if skip_check == False:
    print("Enter the remaining digits of your Switch's serial code following the first four letters/numbers ")
    print("This does not include the first four numbers/letters, such as XAJ4 or XAW1")
    sixdig = input()


    unpatched_range = []
    possibly_patched_range = []
    patched_range = []

    unpatched_range.append(serial_list[usrtype]['unpatched']['min'])
    unpatched_range.append(serial_list[usrtype]['unpatched']['max'])
    unpatched_range.append(usrtype + sixdig)

    possibly_patched_range.append(serial_list[usrtype]['possibly patched']['min'])
    possibly_patched_range.append(serial_list[usrtype]['possibly patched']['max'])
    possibly_patched_range.append(usrtype + sixdig)

    patched_range.append(serial_list[usrtype]['patched']['min'])
    patched_range.append(usrtype + sixdig)

    unpatched_range.sort() 
    # sort alphanumerically, if serial is inbetween it will go as item 2 [1] and therefore verify it
    # if it is entered as item 3 [2], then we try again with 'probably patched' and 'patched'
    possibly_patched_range.sort()
    patched_range.sort()

    if debug:
        print(unpatched_range)
        print(possibly_patched_range)
        print(unpatched_range)

    userserial = usrtype + sixdig

    # if its in the middle of unpatched, then its certain to be unpatched
    if unpatched_range[1] == userserial:
        print("Congrats, your switch isn't patched!")
        x = input("Want to double check? (Y/N)")
        if x.upper() == "Y":
            if possibly_patched_range[1] == userserial:
                print("Possibly patched from check 2")
            else:
                print("No false positives found from check 2")
            
            if patched_range[1] == userserial: # last item, since it will always be higher than the first if 100% patched
                print("Patched from check 3")
            else:
                print("No false positives found from check 3")
    else:
        if possibly_patched_range[1] == userserial:
            print("Your Switch is possibly patched")
        if patched_range[1] == userserial:
            print("Your Switch is most-likely patched")
        else:
            print("Your Switch's patchness is Unknown")

else:
    print("Finished execution")
