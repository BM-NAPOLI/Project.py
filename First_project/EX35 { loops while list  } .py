NAMES = ["RAYAN","AHMAD","ESLAM","MARWAN"]
#* FIRST METHOD 
print(NAMES[0])
print(NAMES[1])
print(NAMES[2])
print(NAMES[3])
                  #? OR 
print("\n") #! ESPASS 

#TODO SACOND METHOD 
for n in NAMES:
    print(n)

#! NEW EX 
GRADES = [35,58,49,78,46,78,98]
PASSED_STUDENTS = 0
for I in GRADES : 
    if I >= 50 : 
        PASSED_STUDENTS += 1
print("The number of students who passed is : ",PASSED_STUDENTS)   

NEW_GRADES = []
for I in GRADES:
    BONUS =I + 5 
    NEW_GRADES.append(BONUS)
print("THE NEW LIST AFTER BONUS IS : ",NEW_GRADES)

PASSED_STUDENTS_AFTER_BONUS = 0
for I in NEW_GRADES : 
    if I >= 50 : 
        PASSED_STUDENTS_AFTER_BONUS += 1
print("The number of students who passed after bonus is : ",PASSED_STUDENTS_AFTER_BONUS)   