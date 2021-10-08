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
    Linear programming only presented here wrt demo of tuple
    Parameters:
    none
    
    Returns:
    none
    '''


    l_numbers = ('L12345', 'L54321')
    module_list = ['Java_programming', 'Python_Scripting']
    java_grade_dictionary = {'L12345':40, 'L54321':70}
    python_grade_dictionary = {'L12345':69, 'L54321':58}

    input_l_number = input("Enter Student's L number")
    if input_l_number == 'L12345':
        index_l_number = 0
    elif input_l_number == 'L54321':
        index_l_number = 1

    print(module_list[index_l_number])


