#!/usr/bin/env python
# coding: utf-8

# ## Problem 1 - Simple temperature calculator (*3 points*)
# 
# In the first problem your aim is to create a function that converts the input temperature from degrees Fahrenheit to degrees Celsius. The conversion formula from Fahrenheit to Celsius can be found below.
# 
#   T_{Celsius} = ( T_{Fahrenheit} - 32 ) / 1.8
# 
# Notice: Closely follow the instructions! 
# 
# Your score on this problem will be based on following criteria:
# 
# - Creating a function called `fahr_to_celsius`
# - Defining the function to have one input parameter called `temp_fahrenheit`
# - Creating a variable called `converted_temp` inside the function to which you should assign the conversion result (i.e., the input Fahrenheit temperature converted to Celsius)
# - Returning the converted value from the function back to the user
# - Answering some questions about functions at the end of this problem
# - Adding comments in your code and a docstring that explains how to use your `fahr_to_celsius` function (i.e., you should write the purpose of the function, parameters, and returned values)

# YOUR CODE HERE
""" Prints information about Simple temperature calculator. 
Author:
    Masataka Ohta - 28.4.2020
"""
#I created the function to convert the input temperature from degrees Fahrenheit to degrees Celsius.
def fahr_to_celsius(temp_fahrenheit):

#We can describe that  T{Celsius} = ( T{Fahrenheit} - 32 ) / 1.8. That is why I defined the parameter and the return statement.
    return (temp_fahrenheit - 32)/1.8
 
#Creating a variable  
converted_temp = fahr_to_celsius(48)

#Print formulated value from Fahrenheit to Celsius
print("48 degrees Fahrenheit in Celsius is:",converted_temp )

#Creating a variable 
converted_temp = fahr_to_celsius(71)

#Print formulated value from Fahrenheit to Celsius
print("71 degrees Fahrenheit in Celsius is:", converted_temp)


# ### Problem 1 tests
# 
# Check that the function produces correct answers for:
# 1. What is 48° Fahrenheit in Celsius? 
# 2. What about 71° Fahrenheit in Celsius?

# ### Check your code
# 
# - Make sure you used the given variable names
# - Check that you have added necessary comments to your code
# - Check that your function has a docstring that describes what it does
# 
# ### Questions
# 
# We would like you to think about and answer the following questions based on the materials and ideas that you learned during the lecture:
# 
#   1. Is the concept of function clear to you? If not, what do you not understand?
#   2. What are some of the benefits of using functions?
#   
# Write your answers below:

# YOUR ANSWER HERE. Write your answers as comments
#1. Yes, it is.
#2. When we repeat the same process, we can easily write the code by using functions.
#
#
#

# #### Done!
# 
# That's it! Now you are ready to continue with Problem 2.
