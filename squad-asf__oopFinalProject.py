#Asmaa Mohamed
from abc import abstractmethod
from cmath import sqrt,tan
from math import radians
import turtle
from numpy import size

#The Base class
class Polygon:
    def __init__(self,num_sides):
        self.num_sides = num_sides
    @abstractmethod
    def sides(self):
        return self.num_sides
    
    @abstractmethod 
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def draw(self):
        pass  
 
#Asmaa Mohamed 
#inheriting from Polygon 
class Triangle(Polygon):
    def __init__(self,x,y,z):
        Polygon.__init__(self, 3)
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        s = (self.x + self.y + self.z)/2.0
        area = sqrt(s*((s-self.x)*(s-self.y)*(s-self.z)))
        return area
 
    def perimeter(self):
        return self.x + self.y + self.z
#Asmaa Mohamed
#inheriting from Triangle 
class IsoscelesTriangle(Triangle):
  def __init__(self,x,y):
    Triangle.__init__(self, x,x,y)
  def draw(self):
      
      for i in range(0, self.x):
            # nested loop for each column
          for j in range(0, i + 1):
                # print star
              print("*", end=" ")
            # new line after each row
          print( )
        
#Asmaa Mohamed
#inheriting from Triangle  
class EquilateralTriangle(Triangle):
  def __init__(self,x):
    Triangle.__init__(self, x,x,x)
  def draw(self):
      for i in range(0 , self.x):
        for j in range(0,self.y - i -1):
            print(end=" " )
        for j in range(0 , i+1):
            print("*" , end=" ")
        print()
#Ahmed Magdy
#inheriting from Polygon
class Quadrilateral(Polygon):
    def __init__(self,x,y):
        Polygon.__init__(self, 4)
        self.x = x
        self.y = y
    def area(self):
        area = self.x * self.y
        return area
    def perimeter(self):
        return (self.x + self.y)*2
#Ahmed Magdy
#inheriting from Quadrilateral
class Square(Quadrilateral):
    def __init__(self,x):
        Polygon.__init__(self, 4)
        self.x = x
    def area(self):
        area = self.x * self.x
        return area
    def perimeter(self):
        return self.x * 4.0
    def draw(self):
        for i in range(0,self.x) :
          for j in range (0,self.x):
             print("*", end=" ")
          print( )
#Ahmed Magdy          
#inheriting from Quadrilateral
class Rectangle(Quadrilateral):
    def __init__(self,x,y):
        Polygon.__init__(self, 4)
        self.x = x
        self.y = y
    def area(self):
        area = self.x * self.y
        return area
    def perimeter(self):
        return (self.x + self.y) * 2.0
    def draw(self):
        for i in range(self.x):
          for j in range(self.y):
            print('*', end =" ")
          print() 
#Asmaa Mohamed               
#inheriting from Polygon 
class Pentagon(Polygon):
  def __init__(self, size):
    Polygon.__init__(self, 5)
    self.size = size
    
  def area(self):
    angle = radians(180/5)
    return self.size*self.size*5/(4*tan(angle)); 

  def perimeter(self):
    return self.size*5 
  def draw(self):
      t = turtle.Turtle()
      for i in range(5):
          t.forward(100) 
          t.right(72) 

#Asmaa Mohamed
#inheriting from Polygon 
class Hexagon(Polygon):
  def __init__(self, size):
    Polygon.__init__(self, 6)
    self.size = size
  
  def area(self):
    angle = radians(180/6)
    return self.size*self.size*6/(4*tan(angle))
    
    
  def perimeter(self):
    return self.size*6 
  def draw(self):
    t = turtle.Turtle()
    for i in range(6):
        t.forward(100) 
        t.right(60)
#Ahmed Magdy
#inheriting from Polygon
class Octagon(Polygon):
  def __init__(self, size):
    Polygon.__init__(self, 8)
    self.size = size
  def area(self):
    angle = radians(180/8)
    return self.size*self.size*8/(4*tan(angle))
  def perimeter(self):
    return self.size*8
  def draw(self):
    t = turtle.Turtle()
    for i in range(8):
        t.forward(100) 
        t.right(45) 
#Ahmed Nabil        
flag = True
while flag :
    n = int(input("Enter the number of sides : "))
    if n == 5 or n == 6 or n == 8 :
         x = int(input("Enter the first side : "))
    elif n == 4 :
        x = int(input("Enter the first side : "))
        y = int(input("Enter the second of side : "))
    elif n == 3 :
        x = int(input("Enter the first side : "))
        y = int(input("Enter the second of side : "))
        z = int(input("Enter the third of side : "))
    if n == 3 :
        t = Triangle(x,y,z)
        print("Triangle Area : ",t.area())
        print("Triangle perimeter :",t.perimeter())
        if (x == y and x == z):
            t = EquilateralTriangle(x)
            print("EquilateralTriangle\n")
            t.draw()
            print("EquilateralTriangle Area :",t.area())
            print("EquilateralTriangle perimeter :",t.perimeter())
        elif (x == y and x != z):
            t = IsoscelesTriangle(x,y)
            print("IsoscelesTriangle\n")
            t.draw()
            print("IsoscelesTriangle Area : ",t.area())
            print("IsoscelesTriangle Perimeter :",t.perimeter())
    elif n == 4 :
        t = Quadrilateral(x,y)
        print("Quadrilateral Area : ",t.area())
        print("Quadrilateral perimeter : ",t.perimeter())
        if (x == y):
            t = Square(x)
            print("Square\n")
            t.draw()
            print("Square Area :",t.area())
            print("Square Perimeter :",t.perimeter())
        elif (x != y):
            t = Rectangle(x,y)
            print("Rectangle\n")
            t.draw()
            print("Rectangle Area : ",t.area())
            print("Rectangle perimeter :", t.perimeter())
    elif n == 5 :
        t = Pentagon(x)
        print("Pentagon\n")
        t.draw()
        print("Pentagon Area : ",t.area())
        print("Pentagon perimeter : ",t.perimeter())
    elif n == 6 :
        t = Hexagon(x)
        print("Hexagon\n")
        t.draw()
        print("Hexagon Area : ",t.area())
        print("Hexagon perimeter : ",t.perimeter())
    elif n == 8 :
        t = Octagon(x)
        print("Octagon\n")
        t.draw()
        print("Octagon Area : ",t.area())
        print("Octagon perimeter : ",t.perimeter())
    else :
        flag = False 
                          
  