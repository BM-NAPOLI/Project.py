# BREAK , CONTINUE

NAMES = ["RAYAN","AHMED","MOHAMED","MAHMOD","STOP","HMODI"]

 #! BREAK
for I in NAMES : 
    if I == "STOP" :
        print("Break The Loops")
        break
    print(I)

print("\n")                                        #TODO    ESPASSE

#? CONTINUE
for I in NAMES : 
    if I == "STOP" :
        print("Continue The Loops")
        continue
    print(I)

print("\n")                                       #TODO    ESPASSE

#* NEW EX 
I = 0 
while I < 10 :
    I += 1 
    if I == 3 :
        continue
    if I == 7 : 
        break
    print("I = ",I)    

if  I == 7 :
    print("I =  7")  