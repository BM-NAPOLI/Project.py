GENDER = input("ENTER YOUR GENDER { MALE [M] OR FEMALE [F] } ")
AGE = int(input("ENTER YPUR AGE : "))
if GENDER == 'M':
    print("YOU ARE MALE")
    if AGE < 21:
        print("YOU ARE YOUNG BOY")
    elif AGE < 60:
        print("YOU ARE ADULT MAN")
    else:
        print("YOU ARE OLD MAN")

        
elif GENDER == 'F':
    print("YOU ARE FEMALE")   
    if AGE < 21:
        print("YOU ARE YONG GIRL")
    elif AGE < 60:
        print("YOU ARE ADULT WOMAN ")   
    else:
        print("YOU ARE OLD WOMAN ")   
    
         
else:   
    print("YOU ARE GAY") 
    if AGE < 21:
        print("YOU ARE YONG GAY")
    elif AGE < 60:
        print("YOU ARE ADULT GAY ")   
    else: 
        print("YOU ARE OLD GAY ")   
    
     