
"""
This function recives random number. Subsequently, 
the system searches the this nubmber in the database. In the event that 
the this number is present in User database, it return 'True' and 
subsequently program will generetae new random number.
"""


import initialize

# It imports document of Initialize
def chk_trace_number(trace_number):
    conn = initialize.lunch_db()
    curr = conn.cursor()
    curr.execute(f"SELECT * FROM User WHERE trace_number = '{trace_number}';")
    items = curr.fetchall()
    found_trace_number = []
    for item in items:
        found_trace_number.append(item[3])
    if len(found_trace_number)!= 0:
        print("!!This trace number already exists in db, So program try to generate new number!!")
        return True
    else:
        return False