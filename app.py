import mariadb
import dbcreds


conn = None
cursor = None
try:
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
    cursor = conn.cursor()
    alias = input("Please type in your alias: ")
    password = input("Please type in your password: ")
    cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [alias, password])
    user = cursor.fetchall()
    if cursor.rowcount == 1:
        print("Login successful!")
        currentUser = (user[0][0])
    elif cursor.rowcount == 0:
        print("No user found")
    else:
        print("THIS IS AN ISSUE")
except mariadb.ProgrammingError:
    print("You made an error in your code")
finally:
    if cursor != None:
        cursor.close()
    if conn != None:
        conn.rollback()
        conn.close()

def newExploit():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
        cursor = conn.cursor()
        newExploit = input("Your new exploit: ")
        cursor.execute("INSERT INTO exploits(content, user_id) VALUES(?, ?)", [newExploit, currentUser])
        conn.commit()
        if cursor.rowcount == 1:
            print("Successfully made a new exploit!")
        else:
            print("Something went wrong.")
    except mariadb.ProgrammingError:
       print("You made an error in your code")
    finally:
        if cursor != None:
           cursor.close()
        if conn != None:
           conn.rollback()
           conn.close()

def userExploits():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [currentUser])
        posts = cursor.fetchall()
        for post in posts:
            print(post[1])
    except mariadb.ProgrammingError:
        print("A coder made an error..")
    finally:
        if cursor != None:
           cursor.close()
        if conn != None:
           conn.rollback()
           conn.close()

def otherExploits():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE user_id != ?", [currentUser])
        posts = cursor.fetchall()
        for post in posts:
            print(post[1])
    except mariadb.ProgrammingError:
        print("A coder made an error..")
    finally:
        if cursor != None:
           cursor.close()
        if conn != None:
           conn.rollback()
           conn.close()









while currentUser == user[0][0]:
    print("-----------------------------------------------------------------------")
    print("Select 'a' to make a new exploit, 'b' to see your exploits, 'c' to see other user exploits or press 'd' to logout")
    selection = input("Your choice: ")
    if selection == "a":
        newExploit()
    elif selection == "b":
        userExploits()
    elif selection == "c":
        otherExploits()
    elif selection == "d":
        currentUser = None
    

