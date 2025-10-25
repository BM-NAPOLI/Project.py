NB1 = int(input("ENTER THE FIRST NUMBER : "))
NB2 = int(input("ENTER THE SECOND NUMBER : "))

if NB2 == 0:
    print("DIV / 0 [ERROR] ")

else:  
    ADD = NB1 + NB2
    MIN = NB1 - NB2
    MUL = NB1 * NB2
    DIV = NB1 / NB2
    MOD = NB1 % NB2

    print(f"ADDING = {ADD}")
    print(f"SUBTRACTING = {MIN}")
    print(f"MULTIPLYING = {MUL}")
    print(f"DIVIDING = {DIV}")
    print(f"MODULO = {MOD}")
