

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

