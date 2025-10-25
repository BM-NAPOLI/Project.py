class Dates:
    def __init__(self,date):
        self.__date = date

    def getDate(self):
        return self.__date 

    @staticmethod
    def toDashDate(date):
        return date.replace("/","-") 

date = Dates("01-03-2010")  
daterombd = "01/03/2010"
datewithdash = Dates.toDashDate(daterombd)


if (date.getDate() == datewithdash):
    print("Equal")
else:
    print("Not E²quale")    

#? print(datewithdash)