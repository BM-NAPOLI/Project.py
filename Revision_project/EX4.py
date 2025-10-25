def STUDENT():
    NOTES = []

    for i in range(1, 31):
        note = float(input(f"Enter NT{i}: "))
        NOTES.append(note)

    print()  
    
    for j in range(4):
        if NOTES[j] < 10:
            print(f"NT{j+1}  --->  SA9T")
        else:
            print(f"NT{j+1}  --->  NAJE7")

    return NOTES



print()
NT = STUDENT()

print("\n-------------------------------")
print(f"The NOTES of student: {NT}")

average = sum(NT) / len(NT)
print(f"AVERAGE = {average:.2f}")
print("-------------------------------")

