import sys; #For sys.exit
import MySQLdb; #MySQL as the Database
import getpass; #To take password input
from warnings import filterwarnings #To remove warnings of existing databases and tables in MySQL
def enter():
        count = 0;
        print("Hello and Welcome\n");
        a = raw_input("What would you like to do?\n");
        if(Lexi(a) == "login"):
            Database()
            while(count < 5): #No more than 5 Login Attempts
              username = raw_input("Enter username \n")
              password = getpass.getpass("enter password\n")
              print("\n processing... ")
              if(Login_check(username, password) == True):
                loggedin();
              else:
                  print("Wrong user name or password")
                  count = count + 1;
def Database(): # initialise the databse and checks if a database already exists
     db = MySQLdb.connect(host = "localhost",user = "root",passwd = "Be761ran091*")
     cursor = db.cursor()
     filterwarnings('ignore', category = MySQLdb.Warning)
     cursor.execute("CREATE DATABASE IF NOT EXISTS data")
     db = MySQLdb.connect(host = "localhost",user = "root",passwd = "Be761ran091*",db = "data")
     cursor = db.cursor()
     cursor.execute("CREATE TABLE IF NOT EXISTS main(USERNAME VARCHAR(20), PASSWORD VARCHAR(20))")
     cursor.execute("Select * FROM main")
     dat = cursor.fetchall() 
     db.close()
     if len(dat)==0 : #If there is no existing user creates a new super user
       print("Seems like a user does not exist. Creating a useer");
       createSuper();


def Lexi(text): #Advanced user input 
        arr = text.split();
        arr2 = []
        for word in arr:
          word = word.lower();  
          arr2.append(word);
        if "login" in arr:
            print ("logging in")
            return "login";
        if "superuser" in arr or "create" in arr:
            return "superuser"
        if "different" in arr and "user" in arr:
            return "dif_user"



def Login_check(username, password): #Authenticates the Login
    db = MySQLdb.connect(host = "localhost",user = "root",passwd = "Be761ran091*",db = "data")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM main")
    data = cursor.fetchall()
    for row in data:
        user = row[0]
        passk = row[1] 
        if(user == username and passk == password):
          return True;
    return False;

def createSuper():
    name = raw_input("Enter Username")
    passk = getpass.getpass("Enter Password")
    passk2 = getpass.getpass("Enter Password Again")
    if(passk != passk2):
        print("Passwords don't match")
        createSuper()
    else:
        db = MySQLdb.connect(host = "localhost",user = "root",passwd = "Be761ran091*",db = "data")
        cursor = db.cursor() 
        cursor.execute("INSERT INTO main (USERNAME,PASSWORD) VALUES ('%s','%s')"%(name,passk))
        cursor.execute("SELECT * FROM main")
        data = cursor.fetchall()
        db.commit()
        db.close()
        return True


def loggedin():
    while(True):
     print("You are now Logged in")
     ins = raw_input("What would you like to do?\n")
     if ins == "exit": #Exit 
         sys.exit(0)
     elif Lexi(ins) == "superuser": #Create a new SuperUser
         createSuper()
     elif Lexi(ins) == "dif_user":  #Login as a different User
        enter()
if __name__ =="__main__":
    enter();
else:
    enter();
