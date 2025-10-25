from datetime import date
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        return f"My name is {self.__name} and my age is {self.__age} "
    
class Man(Person):
    gender = 'male'
    no_of_male = 0

    def __init__(self, name, age, voice=""):  # voice اختياري
        super().__init__(name, age)
        self.__voice = voice
        Man.no_of_male += 1
    
    @classmethod 
    def initFromBirthYear(cls,name,birthYear,voice=""):
         age = date.today().year-birthYear
         return cls(name,age,voice)
                  

    def display(self):
        base = super().display()
        return base + f"and voice {self.__voice} and my gender is {self.gender}"

class Woman(Person):
    gender = 'female'
    no_of_female = 0

    def __init__(self, name, age, her=""):  # her اختياري
        super().__init__(name, age)
        self.__her = her
        Woman.no_of_female += 1

    @classmethod 
    def initFromBirthYear(cls,name,birthYear,her=""):
         age = date.today().year-birthYear
         return cls(name,age,her)

    def display(self):
        base = super().display()
        return base + f", my her character is {self.__her}, and my gender is {self.gender}"

# إنشاء كائنات من كلاسي Man
Man1 = Man.initFromBirthYear("Rachid", 1971, "hard")
Man2 = Man.initFromBirthYear("Rayan", 2010, "hard")
Man3 = Man.initFromBirthYear("Himin", 2019, "child voice")

# إنشاء كائنات من كلاسي Woman
Woman1 = Woman.initFromBirthYear("Jamila", 1981, "short")
Woman2 = Woman.initFromBirthYear("Sara", 2013, "soft")
Woman3 = Woman.initFromBirthYear("Laila", 2008 , "Hijab")  

# طباعة بيانات كل الأشخاص
print(Man1.display())
print(Man2.display())
print(Man3.display())

print(Woman1.display())
print(Woman2.display())
print(Woman3.display())

# طباعة عدد الذكور والإناث
print(f"Number of men created: {Man.no_of_male}")
print(f"Number of women created: {Woman.no_of_female}")