# importing modules & libs
import mysql.connector
import colorama
import sys
import os
import time

# Login
user = input("Enter user => ")
password = input("Enter password => ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
mydb = mysql.connector.connect(host='localhost', user= user, passwd= password)
state = mydb.is_connected()
cursor = mydb.cursor()

# Starting
if state == True:
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
else:
    print("Please check user and password :/ ")



while running:
    break
