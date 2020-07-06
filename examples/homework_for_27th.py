from area_service import Area_Service
from paint_service import Paint_Service
from car_class import Mercedes_Cla_Template
from Mercedes_Cla_AMG_Template import Mercedes_Cla_AMG_Template


area_svc_obj = Area_Service()
paint_svc_obj = Paint_Service()
devika_red_mercedes = Mercedes_Cla_Template()

stuti_yellow_amg = Mercedes_Cla_AMG_Template()

devika_red_mercedes.drive_forward()
devika_red_mercedes.turn_headlight_on()
print(" ")
stuti_yellow_amg.drive_forward()
stuti_yellow_amg.turn_headlight_on()



rectangle_object = {}
rectangle_object["One"] = [34, 12, "red"] # [length, width, colour]
rectangle_object["Two"] = [45, 34, "green"]
rectangle_object["Three"] = [56, 43, "yellow"]
rectangle_object["Four"] = [12, 12, "pink"]
rectangle_object["Five"] = [15, 29, "orange"]


print(len(rectangle_object))

list_of_keys = list(rectangle_object.keys())
print(list_of_keys[0])
print(list_of_keys)

counter = 0
#
# while counter < len(list_of_keys):
#     key = list_of_keys[counter]
#     print(key)
#     value = rectangle_object[key]
#     width = value[0]
#     height = value[1]
#     colour = value[2]
#     rectangle_area = area_svc_obj.area_Rectangle(width = width,height=height)
#     paint_task_resp = paint_svc_obj.paint_rectangle(area=rectangle_area, color=colour)
#     print(paint_task_resp)
#     #print("Key is {} and area is {} and colour is {}".format(key, rectangle_area, colour))
#     counter = counter + 1

#homework-2

