class Math:

    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def add5(num):
        return num+5
    
    @staticmethod
    def add10(num):
        return num+10
    
    @staticmethod 
    def pi():
        return 3,14
    

x = Math.add(5,5)
y = Math.add5(5)
w = Math.add10(0)

print(x,y,w)