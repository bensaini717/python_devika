#practice for class and objects

# class toaster:
#     time=5
#     def pop_toaster(self):
#         print("the toast is ready")
#
#     def toast_in_making(self):
#         print("the toast is still getting cooked")
#
# phillips_toaster = toaster()
# phillips_toaster.pop_toaster()
# phillips_toaster.toast_in_making()
# # print(phillips_toaster.time)
#
# samsung_toaster = toaster()
# print(samsung_toaster.time)

#homework
# make a class through which we create a object to calculate area of rectangle,square,triangle,circle,rhombus,hexagon,radius?


class calculate_Area:

    PI = 3.142

    def area_Circle(self, radius):
        area = self.PI * (radius * radius)
        return area


    def area_Rectangle(self, width, height):
        area = self.PI * width * height
        return area

    def area_Triangle(self, a, b, c, s):
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area

    def area_Rhombus(self, d1, d2):
        area = (d1 * d2) / 2
        return area


# my_area_calculator = calculate_Area()
# areaOfMyCircle = my_area_calculator.area_Circle(radius=20)
# print("The area of my circle is {}".format(areaOfMyCircle))
#
# areaOfMyRectangle = my_area_calculator.area_Rectangle(width=20, height=40)
# print("The area of my Rectangle is {}".format(areaOfMyRectangle))
#
# areaOfMyTriangle = my_area_calculator.area_Triangle(a=10, b=50, c=30, s=90)
# print("The area of my Triangle is {}".format(areaOfMyTriangle))

# total_Area_rhombus = calculate_Area()
# total_Area_rhombus.area_Rhombus(50,30)


