class Man():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __add__(self,other):
        names = self.__name + " and " + other.__name
        ages = self.__age + other.__age
        return f"Names combined are {names} and sum ages is {ages}"
    
    def __lt__(self,other):
        return self.__age < other.__age
    
    def display(self):
        return f"Name is {self.name} and age is {self.age}"
    

man1 = Man('Rayan',15)
man2 = Man('Rachid',54)

print(man1+man2)
print(man1<man2)

# print(dir(Man))
