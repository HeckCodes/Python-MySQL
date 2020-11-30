

# importing modules & libs
import mysql.connector
import colorama
import sys
import os
import time

# Functions


# Login
user = input("Enter user => ")
password = input("Enter password => ")
try:
    mydb = mysql.connector.connect(host='localhost', user= user, passwd= password)
    state = mydb.is_connected()
    cursor = mydb.cursor()

    # Starting
    if state == True:
        os.system('cls')
        print("Checking for user : \033[1m <{}>\033[0m".format(user))
        print("Injecting password : \033[32;1m <{}>\033[0m".format("*"*len(password)))
        print("--------------------------------")
        print("Successfully connected to DB ;) ")
        run = input("Start DB console (Y/N)? => ")

        if run == "Y":
            running = True
            print("Starting the console...")

        elif run == "N":
            running = False
            print("Exiting the console...")
            time.sleep(3)
            exit

except mysql.connector.errors.ProgrammingError:
    os.system("cls")
    running = False
    print("\033[91mPlease check user and password :/\033[0m")
    time.sleep(4)
    exit

while running:
    break
