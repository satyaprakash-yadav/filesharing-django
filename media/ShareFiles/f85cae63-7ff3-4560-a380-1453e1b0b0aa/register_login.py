import os
import random
import time

# survey application 
class Survey_App():
    # constructor
    def __init__(self) -> None:
        # here we create 
        try:
            os.mkdir("cand_data")
        except:
            pass

        # here we create file to store value
        with open("cand_data/all_cadid", "a") as file:
            pass

        # status 
        self.up_info = False

    # method for store value
    def candidates_info(self,name, age, dob, contact, loc):
        otp = random.randint(100000,999999)
        otp = f"20{otp}22"
        with open("cand_data/all_cadid", "a") as file:
            data = f"{otp},{name},{age},{dob},{contact},{loc},\n"
            file.write(data)
            self.up_info = True
            send_feed = [otp, self.up_info]
        return send_feed

    def show_data(self, uc):
        with open("cand_data/all_cadid", "r") as file:
            chk_special = file.readlines()
            
            for chk_val in chk_special:
                valid = chk_val.split(',')          # split method
                if uc in valid:
                    return valid
            else:
                return 0
                
        # return rnt_val

        

# class create for register and login
class RegisterLogin(Survey_App):
    def __init__(self):
        # constructor inherit
        super().__init__()

        # here we use exception handling for create an folder 
        try:
            os.mkdir("Register_user_data")    
        except:
            pass
        
        # here we create file in append mode 
        with open("Register_user_data/user_data","a") as file :
            pass

        # here create flag
        self.register_status = False
        self.login_status = False
    
    # method register for register
    def register(self,name, age, email, pass1 , pass2):

        # read all file data existing data       
        with open("Register_user_data/user_data", "r") as file:
            user_data = file.read()         # here we read all data
            if email in user_data:        
                print("\n------------------------------ email already exits -------------------------------\n")
            else:
                with open("Register_user_data/user_data", "a") as file:
                    data  = f"{name},{age},{email},{pass1},{pass2},\n"
                    file.write(data)
                    self.register_status = True        
        return self.register_status

    # login method create
    def login(self, email, pass1):
        # open file in read mode
        with open("Register_user_data/user_data", "r") as file:
            check_info = file.readlines()
            
            for chk_val in check_info:
                valid = chk_val.split(',')          # split method
                if email == valid[2] and pass1 == valid[3]: #check email and pass
                    self.login_status = True
        return self.login_status

# program start from here
if __name__ == '__main__':
    app_user = RegisterLogin()
    print("\n********************* Welcome to main manu of apps ***********************\n")

    while True: 
        print("1 --> Registration\n2 --> Login\n3 --> Exit\n")
        m_choice = input("Enter the choice :")

        if m_choice == '1':
            # take input from user 
            name = input("Enter the name :")
            age = input("Enter the age :")
            email = input("Enter email_id :")
            pass1 = input("password :")
            pass2 = input("confirm password :")

            # reduce all spaces from data
            name = name.strip()
            age = age.strip()
            email = email.strip()
            pass1 = pass1.strip()
            pass2 = pass2.strip()


            # check password length 
            if len(pass1) < 5:
                print("\n----------------- password should be minimum 5 character -------------\n")
            elif len(pass1)> 15:
                print("\n----------------- password should be maximum 15 character -------------\n")
            else:
                # check password and conform password 
                if pass1 != pass2:
                    print("\n-------------------- Enter correct password ----------------------\n")
                else:
                    r_flag =app_user.register(name, age, email, pass1 , pass2)
                    
                    if r_flag == True:
                        print("\n**************************** Register successfully *****************************\n")
                    else:
                        pass
                
        elif m_choice == '2':
            print("\n******************* Login page ************************\n")
            
            # take input from user  
            email_in = input("Enter the email id :")
            password = input("password : ")

            # stript input
            email_in.strip()
            password.strip()

            # call login method
            l_flag = app_user.login(email_in, password)

            # reply
            if l_flag == True:
                print("\n********************************* Login success ******************************\n")

                # here we create survey application
                print("\n++++++++++++++ Welcome to survey app ++++++++++++\n")
                while True:
                    print("\n-->1)For add candidate bio\n-->2)Find candidate bio\n-->3)Exit\n")
                    ser_ch = input("Enter value :")

                    # take candidate information
                    if ser_ch == "1":

                        name = input("Name :")
                        age = input("Age :")
                        dob = input("DOB 'dd/mm/yy' :")
                        contact = input("Contact no :")
                        loc = input("Location :")

                        # strip all information
                        name = name.strip()
                        age = age.strip()
                        dob = dob.strip()
                        contact = contact.strip()
                        loc = loc.strip()

                        # send info to store 
                        status = app_user.candidates_info(name, age, dob, contact, loc)
                        print(f"\n--------------\n Your special id is {status[0]}\n-------------")

                        if status[1] == True:
                            print("\n -----> upload data successfully <-----\n")
                        else:
                            print("\n------- something went wrong -------\n")
                    

                    elif ser_ch == "2":
                        
                        search = input("Enter special id.:")
                        
                        # send unique code and get info
                        candidate_show_data = app_user.show_data(search) 
                        time.sleep(2)

                        if candidate_show_data == 0:
                            print("\n------------------------------------------------\n")
                            print("****** Check special id again & try again ******")
                            print("\n------------------------------------------------\n")
                            
                        
                        else:
                            print("\n--------------------------------------------------------\n")
                            print("******* Candidate Information ******\n")
                            time.sleep(2)
                            # it print all candidate information

                            print(f"Cadidate Name : {candidate_show_data[1]}")
                            print(f"Cadidate Age : {candidate_show_data[2]}")
                            print(f"Cadidate DOB : {candidate_show_data[3]}")
                            print(f"Cadidate Contact : {candidate_show_data[4]}")
                            print(f"Cadidate Location : {candidate_show_data[5]}")
                            print("\n---------------------------------------------------------\n")

                    elif ser_ch == "3":
                        print("\n============================ Thank you exit ======================\n")
                        break
                    else:
                        print("\n---------------------------- check again ----------------------\n")

            else:
                print("\n---------------------------------- No such account -----------------------------\n")


        elif m_choice == '3':
            print("\n============> Thank You <===========\n")
            break
        else:
            print("\n--------------------- Plz enter valid choice ------------------\n")
