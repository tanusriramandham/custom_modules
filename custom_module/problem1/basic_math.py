class Calculte:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        

    def add(self):
        return f"addition is: {self.a+self.b}"
    
    def subtract(self):
        return f"subtraction is: {abs(self.a-self.b)}"
        
    def multiply(self):
        return f"multiplication is: {self.a*self.b}"
    
    def divide(self):
        try:
            return f"division is: {self.a/self.b}"
        except ZeroDivisionError:
            print("error: cannot be divided by zero")
if __name__=="__main__":       
    cal=Calculte(2,3)
    print(cal.add())
    print(cal.subtract())
    print(cal.multiply())
    print(cal.divide())

