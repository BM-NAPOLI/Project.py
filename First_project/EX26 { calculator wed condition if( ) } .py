
#! CALCULATOR WED CONDITION IF ( ) 
print('                                                                                        § WELCOM TO MY CALCULATOR §')
print('\n\n')

N1 = float (input("ENTER FIRST NUMBER : "))
OP = input ("CHOOSE AN OPERATION[ + , - , * , / ] : ")
N2 = float (input("ENTER SOCAND NUMBER : "))

if OP == '+': 
    RESULT = N1 + N2
    print(N1,'+',N2,'=',RESULT)
elif OP == '-':  
    RESULT = N1 - N2
    print(N1,'-',N2,'=',RESULT) 
elif OP == '*': 
    RESULT = N1 * N2
    print(N1,'*',N2,'=',RESULT )
elif OP == '/': 
    if N2 != 0 : 
        RESULT = N1 / N2
        print(N1,'/',N2,'=',RESULT )
    else :
        print("ERROR [ DIV / 0 ]")   
elif OP == '%':  
    RESULT = N1 % N2
    print(N1,'%',N2,'=',RESULT )
else:
    print("ERROR [ OPERATOR ", str(OP) ,"]" )

print('GOOD BYE! ')


