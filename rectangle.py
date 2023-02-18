class rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def perimeter(self):
        print("perimeter: ",2*(self.length+self.width))
        
        
    def area(self):
        print("Area: ",self.length*self.width)
