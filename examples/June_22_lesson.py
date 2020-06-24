

class Calculator:

    nameClassVariable = 10

    author = "Devika"

    def addition(self, inputNumber):
        print("Hi, I am a function named Addition")


    def subtraction(self, inputNumbr):
        print("Hi, I am a function named Subtraction")



class WaterHeater:

    location_in_appartment = "Master Br"

    def startHeatingWater(self):
        print("Hi, I am a function to heat water!")

    def stopHeatingWater(self):
        print("Hi, I am aa function to stop heating water!")



# Object

object_of_calculator = Calculator()
object_of_water_heater = WaterHeater() #default Constructor method

object_of_calculator.addition(inputNumber=22)

object_of_water_heater.startHeatingWater()
