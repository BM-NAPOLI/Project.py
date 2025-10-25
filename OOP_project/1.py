class Student
    nb_of_students = 0 
    def __init__(self, name, age=0, courses='none'):
        self.__name = name        # private attribute
        self.__age = age            # public attribute
        self.__courses = courses    # public attribute
        Student.nb_of_students += 1

    def descrabe(self):
        print(f"  _MY NAME IS {self.__name} I AM {self.__age} YEARS OLD AND MY COURSES ARE {self.__courses}")        


    def IS_MINOR(self, LEGAL_AGE=18):
        if self.__age >= LEGAL_AGE:
            print("  I AM MAJOR ")
        else:
            print("  I AM MINOR")


    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    
    def get_courses(self):
        return self.__courses

    def set_courses(self, new_corses):
        self.__courses = new_corses



Student_1 = Student("Rayan", 11, ['TKF', 'FF', 'MR'])      
Student_2 = Student("Meryem", 12, ['BT_NS', '9R', 'AS_9L'])
Student_3 = Student("MOHAMED", 16, ['PAT5NA', '7G', 'MR'])


Student_1.descrabe()
Student_1.IS_MINOR()
Student_2.descrabe()
Student_2.IS_MINOR()
Student_3.descrabe()
Student_3.IS_MINOR()


print("\n                       A F T E R    4    Y E A R S    !  \n")


Student_1.set_age(+4)
Student_1.set_courses( ['LAS', 'SL', 'Py'] )

Student_2.set_age(+4)
Student_2.set_courses( ['TIT', 'ç"èb&', 'T5'] )

Student_3.set_age(+4)
Student_3.set_courses( ['BL', 'AG_OT', '?'] )

Student_1.set_name('BM NAPOLI')
Student_1.descrabe()
Student_1.IS_MINOR()

Student_2.set_name('9ORAYDA')
Student_2.descrabe()
Student_2.IS_MINOR()

Student_3.set_name('PAT5NA')
Student_3.descrabe()
Student_3.IS_MINOR()


print("\n")


print(f"THE NUMBER OF STUDENTS IS : {Student.nb_of_students}")
                                                                            