N = int(input("ENTREZ LA VALEUR DE N : "))
SUM_FOR = 0

for I in range(N+1): 
    SUM_FOR += I
print(f"SUM_FOR = {SUM_FOR} ")     

I = 1 
SUM_WHILE = 0
while I <= N : 
    SUM_WHILE  += I
    I += 1
print(f"SUM_WHILE = {SUM_WHILE} ")      
