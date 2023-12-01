import bcrypt
from os.path import join, dirname, abspath
import sqlite3
from sqlite3 import Error
import questionary
import intermediate


"""This document organizes the core functionalities of our database and
 generates it if it is not already present. Moreover, this piece of code
manages the creation of tables in sqlite3. 
It also includes the importation of the questionary, sqlite3, bcrypt, and os.path libraries.
"""

""" Create a file called "test.db" if it does not already exist, 
and connect it to the SQLite database.
    :return: Connection object or None
"""
def lunch_dbx():
    dp_Path_Filex = join(dirname(abspath(__file__)), 'test.db')
    connx = None
    try:
        connx = sqlite3.connect(dp_Path_Filex)
        return connx
    except Error as e:
        print(e)
    return connx
# Create a "testtable" table within the database file.
def create_tablex(connx):
    if connx is not None:
        curx = connx.cursor()
        curx.execute('''CREATE TABLE IF NOT EXISTS testtable(
                     chaxarray text)''')
        print("Second database is activated!")
        connx.commit()
        connx.close()

""" Create a file databaseFile.db if it does not already exist, and connect 
it to the SQLite database.
    :return: Connection object or None
"""
def lunch_db():
    dp_Path_File = join(dirname(abspath(__file__)), 'databaseFile.db')
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(dp_Path_File)
        return conn
    except Error as e:
        print(e)
    return conn
    

# Create a "User" and "Habit" table within the database file.
def create_table(conn):
    
    if conn is not None:
        cur = conn.cursor()
        cur.execute('''
           CREATE TABLE IF NOT EXISTS User(
           name text, 
           surname text, 
           password text,
           trace_number Integer 
   )''')
        cur.execute('''
           CREATE TABLE IF NOT EXISTS Habit(
           habit_name text, 
           period text, 
           practice_time text,                  
           datetime_of_creation text,
           trace_number Integer,
           status text,
           datetime_of_completion text, 
           total_practice_time text,
           last_alter_date text,
           last_practice_time text                           
   )''')
        print("First database is activated!")
        conn.commit()
#        conn.close()
    else:
        print("Error! cannot create the database connection.") 
# Get the necessary information from the user in order to register user and return an array
def user_registeraion():
 thislist = []
 first_name = questionary.text("What's your first name?").ask()
 first_name = intermediate.check_input(first_name)
 surname = questionary.text("What's your surname?").ask()
 surname = intermediate.check_input(surname)
 password = questionary.password("What's your password?").ask()  
 password  = intermediate.check_input(password)
 password = password.encode('utf-8')
 salt = bcrypt.gensalt()
 hashed = bcrypt.hashpw(password, salt)
 thislist.append(first_name)
 thislist.append(surname)
 thislist.append(hashed)
 return(thislist)



    