import os

from conversion import conversion
from leap_year import is_leap_year

# clearing terminal to make it look better
os.system('cls||clear')

# checking for desired function
input = input ("type 'leap_year' for finding which years are leap years and 'conversion' for finding converting units ")

if input == "conversion":
    
    # getting inputs for conversion
    input_unit = input ("is your unit 'centimeters', 'inches', or 'feet'? ")
    val_input = int (input ("what is your value? "))
    
    # running conversion function with the given inputs
    conversion (input_unit, val_input)
    
if input == "leap_year":
    
    # getting the desired year input for the function
    year_input = int (input ("enter to check if it's a leap year"))
    
    # running the function with the given year input
    is_leap_year (year_input)