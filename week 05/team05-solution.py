# *******************************************************************
# 05: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
#
# This team activity is on Boolean Expressions and if statements
# *******************************************************************

# -------------------------------------------------------------------
# Convert Fahrenheit to Celsius
#
# Write a program to request Fahrenheit and convert it to Celsius.
# You will be using functions to write this program.  Below is what
# the main "function" will be do, your task to the write the functions
# that main requires.
#
# You should not change any of the code in main.
#
# Example output of your program
#
# Run 1:
#
# Welcome to this program that will Convert Fahrenheit to Celsius
#
# Enter Fahrenheit: 212
# 212 Fahrenheit is 100.0 Celsius
# 
#
# Run 2:
#
# Welcome to this program that will Convert Fahrenheit to Celsius
#
# Enter Fahrenheit: -40
# (-40) Fahrenheit is (-40) Celsius
# -------------------------------------------------------------------

# TODO Add your functions before the main code

# ====================================================================
# Display a welcome message on the screen
# ====================================================================
def displayWelcome():
    print('Welcome to this program that will Convert Fahrenheit to Celsius')

# ====================================================================
# Get Fahrenheit from the user and return it as a float
# ====================================================================
def getFahrenheit():
    return float(input('Enter Fahrenheit: '))

# ====================================================================
# Convert fahrenheit to celsius and return the results
# ====================================================================
def convertFtoC(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0

# ====================================================================
# This function is used by displayResults() to add () around negative
# values.  Positive values are just returned.
# ====================================================================
def formatValue(value):
    if (value >= 0):
        return value
    else:
        return '({})'.format(value)

# ====================================================================
# Display the converted celsius to the screen
# ====================================================================
def displayResults(fahrenheit, celsius):
    print('{} Fahrenheit is {} Celsius'.format(formatValue(fahrenheit), 
    				    	       formatValue(celsius)))

# ====================================================================
# Main function code
# ====================================================================
displayWelcome()
fahrenheit = getFahrenheit()
celsius = convertFtoC(fahrenheit)
displayResults(fahrenheit, celsius)
