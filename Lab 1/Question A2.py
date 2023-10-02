class Shape:
    def __init__(self, length):
        self.length = length


class Square(Shape):
    
    def __init__(self, length):
        super().__init__(length)
        
    
    def computeArea(self):
        return self.length * 2

class Circle(Shape):
    def __init__(self, length):
        super().__init__(length)
        self.radius = self.length / 2
    
    def computeArea(self):
        return self.radius * self.radius * 3.142
    

class SemiCircle(Circle):
    def __init__(self, length):
        super().__init__(length)
    
    def computeArea(self):
        return Circle.computeArea(self) / 2

class Triangle(Shape):
    
    def __init__(self, length):
        super().__init__(length)
        
    def computeArea(self):
        return 0.5 * self.length * self.length


def main():
    
    length = 10
    
    sq = Square(length)
    semiC = SemiCircle(length)
    triA = Triangle(length)
    
    CompositeShapeAlpha = sq.computeArea() + (semiC.computeArea() * 2)
    CompositeShapeBeta = sq.computeArea() + semiC.computeArea() + triA.computeArea()
    

if __name__ == '__main__':
    main()