from datetime import date
class Student:
    def __init__(self, name, age=0):
        self.__name = name        # private attribute
        self.__age = age            # private attribute
        

    def descrabe(self):
        print(f"  _MY NAME IS {self.__name} I AM {self.__age} YEARS OLD ")        

    @classmethod 
    def initFromBirthYear(cls,name,birthYear):
        return cls(name,date.today().year-birthYear)

Student1 = Student("NADIA",17)
Student2 = Student.initFromBirthYear("NADIA",2004)
Student1.descrabe()
print("AFTER 4 YEARS ")
Student2.descrabe()