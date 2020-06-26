

# Homework


rectangle_object = {}
rectangle_object["One"] = [34, 12, "red"] # [length, width, colour]
rectangle_object["Two"] = [45, 34, "green"]
rectangle_object["Three"] = [56, 43, "yellow"]
rectangle_object["Four"] = [12, 12, "pink"]
rectangle_object["Five"] = [15, 29, "orange"]



# Service class that controls a automobile
# park
# drive forward
# drive in reverse
# breaks
# Power On/off
# play music
# blow horn
# A/C on or off
# headlight on/off


class Animal:
    planet = "Earth"
    def eat_food(self):
        return "Eat Vegetarian Food"

    def make_sound(self):
        return "make sound"

    def sleep_night(self):
        return "sleep at night"


class Tiger(Animal):

    def type(self):
        return "I am a type of a Tiger"

    def eat_food(self):
        return "Eat Hunted-Animal Food"

class White_Tiger(Tiger):

    def type(self):
        return "I am a type of a White Tiger"

my_special_pet_white_tiger = White_Tiger()

print(my_special_pet_white_tiger.type())
print(my_special_pet_white_tiger.eat_food())
print(my_special_pet_white_tiger.planet)

print(" ")


class Dog(Animal):

    def type(self):
        return "I am a type of a Dog"

my_special_pet_tiger = Tiger()
my_special_pet_dog = Dog()

print(my_special_pet_tiger.type())
print(my_special_pet_tiger.eat_food())
print(my_special_pet_tiger.planet)

print(" ")

print(my_special_pet_dog.type())
print(my_special_pet_dog.eat_food())
print(my_special_pet_dog.planet)
