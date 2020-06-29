
class Area_Service:

    PI = 3.142

    def area_Circle(self, radius):
        area = self.PI * (radius * radius)
        return area


    def area_Rectangle(self, width, height):
        area = width * height
        return area

    def area_Triangle(self, a, b, c, s):
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

    def area_Rhombus(self, d1, d2):
        area = (d1 * d2) / 2
        return area
