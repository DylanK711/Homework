class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def getArea(self):
        area = self.width * self.length
        return area
    def getPeramater(self):
        parameter = self.length*2 + self.width* 2
        return parameter
rectangle_1 = Rectangle(5,10)
print(rectangle_1.getPeramater())

rectangle_2 = Rectangle(20,30)
print(rectangle_2.getArea())




