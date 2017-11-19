#Code Created by: Nicholas Brean ans Justin Bronson
#Code created on: November 2017
#Code finds the average of an array of ints

import ui
import random

array = []	
	
def array_list(counter):
    while counter < 10:
        #generating a number between 1,100
        arraynumber = (random.randint(1, 100))
        #adding array_number to array
        array.append(arraynumber)
        counter = counter + 1
    
    view['array_textview'].text = str(array)
    
    return array
def adding_up_array_func(sender):
    #pulling array from function
    array_total = array_list(0)
    
    #calcukating the max vaule of array
    sum_of_array = sum(array)
    #calculating how many numbers are in the array
    length_array = len(array)
    #calculating the average of array
    average_array = sum_of_array / length_array
    
    view['average_label'].text = str(average_array)


view = ui.load_view()
view.present('sheet')

