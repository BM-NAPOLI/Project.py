from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Squar (shape):
    def __init__(self,side):
      self.__side = side
    
    def area(self):
        return self.__side * self.__side

    def parameter(self):
        return self.__side * 4 
    

class Rect  (shape):
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def parameter(self):
        return  (self.__length + self.__width) * 2
    

squar = Squar(10)
rect = Rect(5,3)


print(f"Squar erea = {squar.area()} / Squar parameter = {squar.parameter()}")
print(f"Rect erea = {rect.area()} / Rect parameter = {rect.parameter()}")

        