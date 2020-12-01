# importing modules & libs
import mysql.connector
import colorama
import sys
import os
import time

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
        print("\033[32;22mSuccessfully connected to DB ;) \033[0m")
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

# Functions

def createDB():
    newDB = input("Enter new DB name => ")
    string = "CREATING DATABASE {}...\n".format(newDB)
    for char in string:
        time.sleep(0.1)
        print(char,end="")
    cursor.execute("CREATE DATABASE {}".format(newDB))
    print(cursor.fetchall())
    print("\033[32;1mDATABASE : {} created successfully :)\033[0m ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def useDB():
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print(databases)

    wantedDB = input("Enter database name => ")
    cursor.execute("USE {}".format(wantedDB))
    print(cursor.fetchall())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def newtable():

    wanttable = input("Want to show all tables (Y/N)? => ")
    if wanttable=="Y":
        string = "GETTING ALL TABLES...\n"
        for char in string:
            time.sleep(0.1)
            print(char,end="")
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())

    newtablename = input("Enter new table name => ")
    fieldcount = int(input("Number of fields desired? => "))
    tablestructure = {}
    fieldaddedcount = 0

    # Get table structure info
    for i in range(fieldcount):
        field = input("Field name => ")
        parameter = input("Enter parameters for {} :".format(field))
        fieldstructure[field] = parameter

    # Make table
    fields = tablestructure.keys()
    tablestring = """"""
    tablestring += "CREATE TABLE {} (\n".format(newtablename)
    for field in fields:
        if fieldaddedcount < len(fields)-1:
            tablestring += "{} {},\n".format(field,tablestructure[field])

        else:
            tablestring += "{} {})".format(field, tablestructure[field])
        fieldaddedcount += 1
    
    # execute
    for char in (tablestring + "\n"):
        time.sleep(0.08)
        print(char,end="")
    cursor.execute(tablestring)
    print(cursor.fetchall())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def customcmd():
    cmd = input("Your query => ")
    for char in cmd + "\n":
        time.sleep(0.1)
        print(char,end="")
    cursor.execute(cmd)
    print(cursor.fetchall())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


while running:
    
    opt ="""
    1. Create Database
    2. Use Database
    3. Create Table
    4. Custom Query
    5. Exit Console
    """
    print(opt)


    break
