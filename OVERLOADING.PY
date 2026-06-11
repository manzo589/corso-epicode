class Frazione:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,altro):
        return Frazione(self.x + altro.x , self.y + altro.y)
    
    def __eq__(self,altro):
        return self.x / altro.x ==self.y / altro.y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
f1 = Frazione (1,2)

f2 = Frazione (2,4)

f3=f1+f2

print(f3.x,f3.y)

f3 = (f1==f2)

print(f3)

print(f1.x,"/",f1.y)

print(f2.x,"/",f2.y)