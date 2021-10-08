"""
# -----------------------------
# File : lab.py
# Created :  08-10-2021
# Author : Rohit Mishra
# Version : v1.0.0
# Py Version : 2021.2.2
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : data variables lab
# -----------------------------
"""



if __name__ == '__main__':
    '''
    Main method of application
    Linear programming only presented here wrt demo of lists, tuples and dictionaries.
    Parameters:
    Student L Numbers.
    
    Returns:
    Prints Module and Marks Obtained of the given L numbers.
    '''


    l_numbers = ('L12345', 'L54321')
    module_list = ['Java_programming', 'Python_Scripting']
    java_grade_dictionary = {'L12345':40, 'L54321':70}
    python_grade_dictionary = {'L12345':69, 'L54321':58}

    input_l_number = input("Enter Student's L number")
    if input_l_number not in l_numbers:
        print("Invalid Entry")
    else:
        print(module_list[0], "Marks Obtained = ", java_grade_dictionary[input_l_number])
        print(module_list[1], "Marks Obtained = ", python_grade_dictionary[input_l_number])
