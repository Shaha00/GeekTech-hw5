import math
class Figure:
    def __init__(self):
        self

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius=radius
      
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value
    
    def calculate_area(self):
        return math.pi * (self.radius**2)
      
    def info(self):
        print(f"Circle radius: {self.radius}cm, area: {round(circle.calculate_area(), 2)}cm.")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a
    
    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b
    
    @side_b.setter
    def side_b(self, value):
        self.__side_b = value
        
    def calculate_area(self):
        return 1 / 2 * (self.__side_a) * (self.side_b)

    def info(self):
        print(f"RightTriangle side a: {self.side_a}cm, {self.side_b}cm, area {round(righttriangle.calculate_area(), 2)}cm")

    
circle = Circle(2)
circle1 = Circle(3)  
righttriangle = RightTriangle(6,3)
righttriangle1 = RightTriangle(6,2)
righttriangle3 = RightTriangle(5,2)

figure = [circle, circle1, righttriangle, righttriangle1, righttriangle3]
for i in figure:
    i.calculate_area()
    print(i.info())


# circle.info()
# righttriangle.info()



    
