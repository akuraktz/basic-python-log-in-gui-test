import easygui

users = {}
status = ""

def displayMenu():
    status = easygui.enterbox(msg="Are you registered user? (y)/(n)? Press q to quit", title="Log In")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = easygui.enterbox(msg="Create login name:" , title="Log In")

    if createLogin in users:
        easygui.msgbox(msg="Login name already exist!", title="Log In")
    else:
        createPassw = easygui.passwordbox(msg="Introduce your password :", title="Log In")
        users[createLogin] = createPassw
        easygui.msgbox(msg="User created" , title="Log In")
 
def oldUser():
    login = easygui.enterbox(msg="Enter log-in name:" , title="Log In")
    passw = easygui.passwordbox(msg="Enter password:" , title="Log In")
 
    if login in users and users[login] == passw:
        easygui.msgbox(msg="Login successful!", title="Log In")
    else:
        easygui.msgbox(msg="That username doesn't exist or wrong pasword.", title="Log In")
 
while status != "q":
    displayMenu()
    oldUser()