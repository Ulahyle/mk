from abc import ABC, abstractmethod
class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __add__(self, other: 'Vector'):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y) 
        return False
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y) 
        return False
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y) 
        return False        
           
class Shape(ABC):
    def __init__(self, position:Vector):
        super().__init__()
        self.position = position
    
    @abstractmethod
    def area(self):
        pass 
    @abstractmethod
    def perimeter(self):
        pass  
   
    def move(self, vector: Vector):
        return self.position + vector  
      
class  Circle(Shape):
    def __init__(self, position, radius):
        super().__init__(position) 
        self.radius = radius
    
    def area(self):
        return self.x * 3.14 
    
    def perimeter(self): 
        return self.x*2 + 3.14 
    
class Rectangle(Shape):
    def __init__(self, position, width, height):
        super().__init__(position) 
        self.width = width
        self.height = height
    
    def area(self):
        return (self.width * self.height) * 2
    
    def perimeter(self): 
        return self.width * self.height
    
v = Vector(2, 3)   
v2 = Vector(2, 3)   
r = Rectangle(v, 5, 6) 
print(r.area())
print(r.move(v2))  
print(r.position - v2)
               
               