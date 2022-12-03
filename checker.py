import json
import os, sys

types = [
    "XAW1", "XAW4", "XAW7",
    "XAJ1", "XAJ4", "XAJ7",
    "XKW1", "XKJ1", "XJW1",
    "XWW1"
]

c = True

with open("serials.json", "r") as serial_json:
    serial_list = json.load(serial_json)




print("Valid First letters")
for i in types:
    print(i)

serial_invalid = True

while serial_invalid:
    usrtype = input("Enter the first four letters/numbers of your Nintendo Switch's serial code: ")

    if usrtype.isupper():
        pass
    else:
        usrtype = usrtype.upper()

    print("Entered:", usrtype)

    if usrtype in types:
        serial_invalid = False
    else:
        print("Invalid Serial Code")


print("Enter the first 6 digits of your Switch's serial code following the first four letters/numbers ")
print("This does not include the first four numbers/letters, such as XAJ4 or XAW1")
sixdig = input()


unpatched_l = []
probpatch_l = []
patch_l = []
unpatched_l.append(serial_list[usrtype]['unpatched']['min'])
unpatched_l.append(serial_list[usrtype]['unpatched']['max'])
unpatched_l.append(usrtype + sixdig)

probpatch_l.append(serial_list[usrtype]['possibly patched']['min'])
probpatch_l.append(serial_list[usrtype]['possibly patched']['max'])
probpatch_l.append(usrtype + sixdig)

patch_l.append(serial_list[usrtype]['patched']['min'])
patch_l.append(usrtype + sixdig)

unpatched_l.sort() # sort alphanumerically, if serial is inbetween it will go as item 2 [1] and therefore verify it
# if it is entered as item 3 [2], then we try again with 'probably patched' and 'patched'
probpatch_l.sort()
patch_l.sort()

if c:
    print(unpatched_l)
    print(probpatch_l)
    print(patch_l)

n = usrtype + sixdig

if unpatched_l[1] == n:
    print("Congrats, your switch isn't patched!")
    x = input("Want to double check? (Y/N)")
    if x == "Y":
        if probpatch_l[1] == n:
            print("Possibly patched from check 2")
        else:
            print("No false positives found from check 2")
        
        if patch_l[1] == n: # last item, since it will always be higher than the first if 100% patched
            print("Patched from check 3")
        else:
            print("No false positives found from check 3")
else:
    if probpatch_l[1] == n:
        print("Your Switch is possibly patched")
    if patch_l[1] == n:
        print("Your Switch is most-likely patched")
    
