
#*IF
#!AND
#?OR

HASE_INVITATION = input("Do you have an invitation ? [Y/N] : ")
IS_FORMAL = input("ARE WARING FORMAL ? [Y/N] : ")

if HASE_INVITATION == "Y" and  IS_FORMAL == "Y":
    print("WELCOM")
elif HASE_INVITATION == "Y" or  IS_FORMAL == "Y":
    print("Okay we well let you in")
else:
    print("Soery") 




