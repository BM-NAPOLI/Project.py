# crate dectenir for users 
user = {}
# cretate dectenery for admin 
admin = {
    # this is fex admin
    "ahmad":{
        "user name":"ihya",
        "password":"ihya9860"
    }
    # ====================
}
# create a dectionaler for new_admins
new_admins = {}
# create welcome function

def welcome_page():
    print("welcome to the welcome page ")
    exit()
# crate mune function 
def mune():
    choses = """
    1 : sign up
    2 : login
    3 : upadat password
    4 : I'm admin
    5 : exite
    
    """
    print(choses)
    
    user_chos = int(input())
    return user_chos

# create sign up function
def sign_up():
    name = input("enetr your name  ")
    user_name = input("enetr your user name ")
    password = input("enetr your password  ")


    if name in user:
        print("sorry the name is rely found enetr a new name")
        
    elif name and user_name and password:
        user[name] = {
            "user name":user_name,
            "password":password
        }
        print("welcome to the logi syseam")
        
    else:
        print("error please enetr all the data")
    

# create  login function 
def login():
    name = input("enetr your name  ")
    user_name = input("enetr your user name ")
    password = input("enetr your password  ")

    if(name in user and user[name]["user name"] == user_name and user[name]["password"] == password):
        print("welcome to the logi syseam")
        
    else:
        print("error the name and user name and password is not found try agin ")
        print("or can you create a new account clik 1 ")


# create a update password function 
def update_password():
    name = input("enetr your name  ")
    user_name = input("enter your user name  ")
    password = input("enetr the  password  ")
    new_password = input('enetr the new password ')
    
    if (name in user and user[name]["user name"] == user_name and user[name]["password"] == password):
        user[name]["password"] = new_password
        print("update it ")

    
    else:
        print("error name or user name or password is not found ")

# ====================== for admin ========================
# create a function for admin
def choses_for_admin():
    while True:
        choses = """
        1 : schow users
        2 : delet user
        3 : celar all users
        4 : add admin
        5 : clear admins 
        7 : go back
        8 : quit
        """
        print(choses)
        admin_chose = int(input())
        
        # ========================================== functions part ===========================================
        #  this function to schow all users f
        def schow_user():
            if admin_chose == 1:
                if user:
                    for username ,info in user.items():
                        print(f"{username}:")
                        for key , value in info.items():
                            print(f"    {key:<12}:  {value}")
                        print()
                else:
                    print("dont have new users right new ")
                    
        # this function for  delet a user
        def delet_user():
            # print all users 
            schow_user()
            name = input("enetr the name of delt is ")
            
            # delte a user from dec user
            
            if name in user:
                del user[name]
                print(f"done deleting {name}")
            else:
                print("the name is not found")
            
        
        # the function to clear all user
        def clear_users():
            user.clear()
            print("clear it !!! ")
                
        
        # the function to schow new admins
        def add_admin():
            if new_admins:
                for username , info in new_admins.items():
                    print(f'{username} :')
                    for key , value in info.items():
                        print(f"{key} : {value}")
                    print()
                else:
                    print("dont have new users right new ")
                
                    chose_admin = input("enetr  name to add admens  ")  
              
                if chose_admin in new_admins:
                    print("add it")
                    admin[chose_admin] = {
                        "user name":new_admins[chose_admin]["user name"],
                        "password":new_admins[chose_admin]["password"]
                        }
                    del new_admins[chose_admin]

            
        # ========================================= condition ==================
        
        
        
        if admin_chose == 1:
            schow_user()
            
        elif admin_chose == 2:
            delet_user()
        
        elif admin_chose == 3:
            clear_users()
            
        elif admin_chose == 4:
            add_admin()  
          
        elif admin_chose == 7:
            main()
        
        elif admin_chose == 8:
            quit()
            

def admin_page():
    name = input("enetr your user name  ")
    user_name = input("enetr your name  ")
    password = input("enetr your password  ")
    
        
    if name in admin and admin["ahmad"]["user name"] == user_name and admin["ahmad"]["password"] == password:
        print(f"hello welcome {name}")
        choses_for_admin()


    else:
        print("sorroy your not admin new ")
        print("we send a message for admin if them ned give you admin ")
        # send the user for acsept original admin admin
        new_admins[name]= {
        "user name":user_name,
        "password":password
        }
        
def main():
    while True:
        
        chose = mune()
        if chose == 1:
            sign_up()
    
        elif chose == 2:
            login()
        
        elif chose == 3:
            update_password()
    
        elif chose == 4:
            admin_page()
        
        elif chose == 5:
            print("goodbye")
            exit()
    
    
main()