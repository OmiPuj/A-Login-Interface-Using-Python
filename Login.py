import time;
import sys;
def enter():
        count = 0;
        print("Hello and Welcome\n");
        time.sleep(1);
        a = raw_input("What would you like to do?\n");
        time.sleep(1.2);
        if(Lexi(a) == "login"):
            while(count < 5):
              username = raw_input("Enter username \n")
              time.sleep(0.5);
              password = raw_input("enter password\n")
              print("\n processing... ")
              time.sleep(0.5);
              if(Login_check(username, password) == True):
                loggedin();
              else:
                  print("Wrong user name or password")
                  count = count + 1;
def Lexi(text):
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

def Login_check(username, password):
    f = open("Passkey.txt","r");
    credentials = f.read();
    f.close();
    print(credentials)
    if credentials == "":
        print("Seems like a user does not exist")
        a = raw_input("Would you like to create one?(Yes||No)\n")
        a = a.lower()
        if a == "yes":
            createSuper()
            return True
        else:
            sys.exit(0)

    else:
        if username in credentials and password in credentials:
            return True
        else:
            return False
def createSuper():
    name = raw_input("Enter Username")
    passk = raw_input("Enter Password")
    passk2 = raw_input("Enter Password Again")
    if(passk != passk2):
        print("Passwords don't match")
        createSuper()
    else:
       f = open("Passkey.txt","w") 
       f.write("\n"name+" "+passk+"  ")
       f.close()
       return True
def loggedin():
    while(True):
     print("You are now Logged in")
     ins = raw_input("What would you like to do?\n")
     if ins == "exit":
         sys.exit(0)
     elif Lexi(ins) == "superuser":
         createSuper()
    

enter();
    
