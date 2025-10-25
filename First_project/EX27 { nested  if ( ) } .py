print("                                                                   ! WELCOM TO BM COFFEE !" )
print("\n\n")
DRINK = input("What would you like to drink ? [ Coffee [1] / Tea [2] ] ")

if DRINK == "1":
    SUGAR = input ("Do u want it Black [3] or with Sugar [4] ? ")
    if SUGAR == "3":
       print("Nice Black")
    elif SUGAR == "4":
       print("Nice Sugar")
    else:
       print("Sory")
elif DRINK == "2":
    SUGAR = input ("Do u want it Grin [5] or Read [6] ? ")
    if SUGAR == "5":
       print("Nice Grin")
    elif SUGAR == "6":
       print("Nice Read")
    else:
       print("Sory")

