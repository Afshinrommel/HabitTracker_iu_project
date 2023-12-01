import questionary
import bcrypt
import intermediate
import initialize
# It import questionary,bcrypt libraries
# and also intermediate,initialize doccument

"""
The objective of this file is to modify the user's details, 
including the given name, surname, and password. The function 
requires a numerical value, which was retrieved from the database 
during the login process. Initially, a connection is established 
with the database by invoking the 'lunch_db()' function, which is 
located within the 'initialize' document. Subsequently, the validity
of the name, last name, and password is assessed. If they meet the
required criteria, the preceding values are replaced with the newly 
provided values.
"""
def edit_Profile(trc_number):
     conn = initialize.lunch_db()
     curr = conn.cursor()
     question = questionary.rawselect(
       "Change name or surname or password",
       choices=["name", "password","surname"],).ask()
     if question == "name":           
             first_name = questionary.text("What's your new first name").ask()
             first_name = intermediate.check_input(first_name)
             curr.execute(f"UPDATE User SET name = '{first_name}' WHERE trace_number = '{trc_number}';")
             curr.fetchall()
             conn.commit()
             conn.close()

             print(f"\n name has been updated '{first_name}'")

     if question == "surname":
             surname = questionary.text("What's your new surname").ask()
             surname = intermediate.check_input(surname)
             curr.execute(f"UPDATE User SET surname = '{surname}' WHERE trace_number = '{trc_number}';")
             curr.fetchall()
             conn.commit()
             conn.close()
             print(f"\n surname has been updated '{surname}'")
     if question == "password":
           thislist=[]
           curr.execute(f"SELECT name FROM User WHERE trace_number = '{trc_number}';")
           x1 = curr.fetchall()
           x1 =x1[0]
           x1= x1[0]
           curr.execute(f"SELECT surname FROM User WHERE trace_number = '{trc_number}';")
           x2 = curr.fetchall()
           x2=x2[0]
           x2=x2[0]
           new_password = questionary.password("What's your new password?").ask()
           new_password = intermediate.check_input(new_password)
           password = new_password.encode('utf-8')
           salt = bcrypt.gensalt()
#Hashing the password
           hashed = bcrypt.hashpw(password, salt)
           thislist.append(x1)
           thislist.append(x2)
           thislist.append(hashed)
           thislist.append(trc_number)
 
           curr.execute(f"DELETE FROM USER WHERE trace_number = '{trc_number}';")
           curr.fetchall()
           conn.commit()
           

           curr.execute("INSERT INTO USER VALUES(?, ?, ?, ?)",
                         (x1, x2,hashed,trc_number))
           conn.commit()
           conn.close()
           print(f"\n password has been updated ")

        