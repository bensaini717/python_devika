

from area_service import Area_Service
from paint_service import Paint_Service


# Work assigned by Boss in JIRA 2567
area_svc_obj = Area_Service()
paint_svc_obj = Paint_Service()

circle_area = area_svc_obj.area_Circle(radius=20)
paint_task_resp = paint_svc_obj.paint_Circle(area=circle_area, color="Red")

print(paint_task_resp)

# Homework
circle_object = {}
circle_object["One"] = [34, "red"]
circle_object["Two"] = [45, "green"]
circle_object["Three"] = [56, "yellow"]
circle_object["Four"] = [12, "pink"]
circle_object["Five"] = [15, "orange"]

print(len(circle_object))

list_of_keys = list(circle_object.keys())
print(list_of_keys[0])
print(list_of_keys)

counter = 0

while counter < len(list_of_keys):
    key = list_of_keys[counter]
    print(key)
    value = circle_object[key]
    radius = value[0]
    colour = value[1]
    circle_area = area_svc_obj.area_Circle(radius = radius)
    paint_task_resp = paint_svc_obj.paint_Circle(area=circle_area, color=colour)
    print(paint_task_resp)


    # print("Key is {} and radius is {} and colour is {}".format(key,radius,colour))
    counter = counter + 1

print("thanks")