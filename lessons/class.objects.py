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

    radius=20

    def area_Circle(self,radius):
        PI = 3.142
        return PI * (radius*radius)
        print("the area of circle is")


    def area_Rectangle(self,width,height):
        area = width * height
        print("the area of rectangle is")

    def area_Triangle(self,a,b,c,s):
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("the area of triangle is")

    def area_Rhombus(self,d1,d2):
        area = (d1 * d2) / 2
        print("the area of rhombus is")


total_Area_Circle = calculate_Area()
total_Area_Circle.area_Circle(20)

total_Area_Rectangle = calculate_Area()
total_Area_Rectangle.area_Rectangle(20,40)

total_Area_Triangle = calculate_Area()
total_Area_Triangle.area_Triangle(10,50,30,90)

total_Area_rhombus = calculate_Area()
total_Area_rhombus.area_Rhombus(50,30)


