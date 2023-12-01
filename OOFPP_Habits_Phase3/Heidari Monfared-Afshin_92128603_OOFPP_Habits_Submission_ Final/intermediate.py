import string
import questionary
from InquirerPy import inquirer

#It imports the libraries string, sqlite3,questionary,InquirerPy.
"""This file contains the following functions.
make_array():  This function creates a raw array that contains only a random number.
check_input(): This function examines the input string to ensure that it has
 a minimum of four characters. Additionally, it ensures that the string is 
 free of any numerical digits or spaces. Furthermore, the function capitalizes
 the first letter of the string.
dig_input():   This function verifies that the input number has a value
 greater than zero and does not contain any strings or spaces.
habit_name()
This function asks the user for the name of a habit and then ensures that the
string is free of any numerical digits or spaces. The function capitalizes
the first letter of the string.
"""


def make_array(trc_number):
     thislist = []
     thislist.append("*")
     thislist.append("*")
     thislist.append("*") 
     thislist.append("*") 
     thislist.append(trc_number)
     thislist.append("*") 
     thislist.append("*")
     thislist.append("*") 
     thislist.append("*")
     thislist.append("*") 
     return(thislist)

def check_input(input_string):
      already = False
      while already == False:
            try:
             if len(input_string) >= 4 and input_string.isalpha() == True:   
                input_string = string.capwords(input_string)
                already = True
             else:
              print("string must have at least 4 character without numbers and spaces")
              input_string = questionary.text("Input string again:").ask()
            except:
               pass 
      return(input_string)

def habit_name()-> str:
             habit_name = inquirer.text(
                       message="habit_name:",
                       validate=lambda result: len(result) > 0 and result.isalpha(),
                       invalid_message="Input cannot be empty or number inside the strings or space.",
                       ).execute()
             habit_name = string.capwords(habit_name) 
             return(habit_name)
def dig_input():
               digital = inquirer.text(
                       message="input_number:",
                       validate=lambda result: len(result) > 0 and result.isdigit(),
                       invalid_message="Input cannot be empty or string or space.",
                       ).execute()
               return(digital)
     
             