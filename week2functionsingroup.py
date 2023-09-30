#variable_name = function_name(arg1, arg2, … argN)
#
#import module_name
#
#variable_name = module_name.function_name(arg1, arg2, … argN)
#variable_name = object_name.method_name(arg1, arg2, … argN)

import math
number_of_items = int(input("Please provide a number of items: "))
number_of_items_per_box = int (input ("Please write a number of items per box: "))

number_of_boxes_that_i_need = math.ceil (number_of_items/number_of_items_per_box)

#roundnumber= round (number_of_boxes_that_i_need)

print (f"I need: {number_of_boxes_that_i_need} ")


