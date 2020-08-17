
def square(input_number):
    return input_number * input_number

def add20(input_number):
    return input_number + 20

user_provided_list = [5, 3, 6, 8 ,9]

def on_all(function_name, input_list):
    for element in input_list:
        response_from_custom_function = function_name(element)
        print(response_from_custom_function)


on_all(add20, user_provided_list)

print("  ")

on_all(square, user_provided_list)
