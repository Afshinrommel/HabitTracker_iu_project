import initialize
# It imports document of Initialize
"""
This function recives first and surname. Subsequently, in the initial stage,
the system searches the provided name against the database. In the event that
the name is present, it proceeds to examine the surname in the database as well. 
In the event that both names are already present in the database and it return 'True' 
then it prevents the registration of those names in the database. Conversely, 
if the aforementioned names are not duplicated, the system accepts them from the user.
"""
def chkUser(user,surname):
    conn = initialize.lunch_db()
    curr = conn.cursor()
    
    curr.execute(f"SELECT name FROM User WHERE name = '{user}';")
    items = curr.fetchall()
    users = []
    for item in items:
        users.append(item[0])
    if len(users)!= 0:
        curr.execute(f"SELECT surname FROM User WHERE surname = '{surname}';")
        itemsx = curr.fetchall()
        surnames = []
        for i in itemsx:
            surnames.append(i)
        if len(surnames)!= 0:
             print("!!The name already exists in db, So you must choose another name!!")
             return True
        else:
            return False
    else:
        return False






