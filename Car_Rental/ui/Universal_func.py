import string
from datetime import date, datetime
# the os is used in cls() to clear the screen 
import os 
from services.CustomerService import CustomerService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"

def printer():
    # The printer function is used to make the command options more visible to the user anywhere he needs it
    print("B.  Back one window")
    print("M.  Main menu")
    print("--"*25)

def printline():
    # The printline function is used to Print a line of --- anywhere it is needs
    print("--"*25)

def Full_name_input_chack(name):
    # This function is used to chack if the full name is properly inputid in the system
    name_list = name.split()
    Tester = True

    if len(name_list) <= 1:# checks if the input is just one word
        Tester = False
        print("\nERROR: Full name was not entered\n")
        printline()

    elif len(name_list) > 1:# checks if the input contanes a number or a symbol
        for word in name_list:
            for letter in word:
                T_or_F = letter.isdigit()
                if T_or_F == True:
                    Tester = False
                    print("\nERROR: Number can't be used in your name\n")
                    printline()
                elif letter in string.punctuation:
                    Tester = False
                    print("\nERROR: Name can not contain a symbol\n")
                    printline()


    else:# if it is a full name this code make sures it is capitalized.
        name = ""
        for word in name_list:
            name = name + " " + word.capitalize()

    return Tester, name

def ssn_input_chack(ssn, Not_user=0):
    # This function is used to check if the ssn is properly inputid in the system
    customer_service = CustomerService()
    Tester = True
    T_or_F = ssn.isdigit()
    if len(ssn) > 10 or len(ssn) < 10:
        Tester = False
        print("\nERROR: SSN contains 10 letters but you put in "+ str(len(ssn)) +"\n")
        printline()
    elif T_or_F == False:
        Tester = False
        print("\nERROR: SSN can not contain letters\n")
        printline()
    if Not_user == 0:
        F_OR_T = customer_service.valid_customer_check(ssn)
        if F_OR_T == True:
            Tester = False
            print("\nERROR: SSN already exists in the system\n")
            printline()

    return Tester, ssn


def address_input_chack(address):
    # This function is used to chack if the address is properly inputid in the system
    Tester = False
    address_list = []
    try:
        address_list = address.split()
        for i in range(len(address_list)):
            if address_list[i].isdigit() == True and len(address_list) != 1:
                Tester = True
        if Tester == False:
            print("\nERROR: Street must have a name and a number\n")
            printline()
    except ValueError:
        print("\nERROR: Street must have a name and a number\n")
        printline()
    return Tester, address

def phone_input_chack(phone):
    # This function is used to check if the phone is properly input in the system.
    Tester = True
    T_or_F = phone.isdigit()
    if T_or_F == False:
        Tester = False
        print("\nERROR: phone number can not contain letters\n")
        printline()
    elif len(phone) < 7 or len(phone) > 7:
        Tester = False
        print("\nERROR: phone number can not contain a more or less then 7 numbers\n")
        printline()
    return Tester, phone
    
def birthday_input_chack(birthday):
    # This function is used to check if the birthday is properly input in the system.
    present = datetime.now().date()
    newYear = present.year-20
    minimum_age = present.replace(year=newYear)

    Tester = False

    if len(birthday) == 10:
        try:
            day, month, year = birthday.replace("/", " ").split()
            Tester = True
            Tester, birthday = date_chack(day, month, year, Tester)
            if Tester == True:
                Tested_birthday = date(int(year), int(month), int(day))
                if Tested_birthday > minimum_age:
                    print("\nERROR: This age is not allowed to rent a car\n")
                    printline()
                    Tester = False
        except ValueError:
            Tester = False
            print("\nERROR: Something went wrong with your input please try again\n")
            printline()
    else:
        print("\nERROR: Something went wrong with your input please try again\n")
        printline()

    return Tester, birthday

def date_chack(day, month, year, Tester=True):
    date_time = day + month + year
    for number in date_time:
        T_or_F = number.isdigit()
        if T_or_F == False:
            Tester = False
    if len(day) != 2:
        print("ERROR: Day must be represented with 2 numbers such as this: 06 or 15")
    elif len(month) != 2:
        print("ERROR: Month must be represented with 2 numbers such as this: 06 or 12")
    elif len(year) != 4:
        print("ERROR: Year must be represented with 4 numbers such as this: 1985 or 2000")
    else:
        try:
            date_time = date(int(year), int(month), int(day))
        except ValueError as ex:
            print("\nERROR: "+ str(ex) + "\n")
            printline()
            Tester = False
    return Tester, date_time

# get start date function
def Start_date():
    present = datetime.now().date()
    print("Example: DD/MM/YYYY\nEnter in the date you want to pick up a car\n")
    printer()
    Choice = input("Choice: ").lower()
    printline()
    if Choice == Home_1 or Choice == Home_2:
        return False
    elif Choice == Back_1 or Choice == Back_2:
        return True
    elif len(Choice) == 10:
        try:
            day, month, year = Choice.replace("/", " ").split()
            Tester, start_date = date_chack(day, month, year)
            if Tester == True:
                return start_date
            else:
                message = "ERROR"
                return message
        except ValueError:
            Tester = False
            print("\nERROR: Something went wrong with your input please try again\n")
            printline()
            if present < start_date:
                return True
            else:
                print("\nYou can't rent a car in the past\n")
                printline()

# Get end date function
def End_date(start_date):
    print("Example: DD/MM/YYYY\nEnter in the date you want to return a car\n")
    printer()
    Choice = input("Choice: ").lower()
    printline()
    if Choice == Home_1 or Choice == Home_2:
        return False
    elif Choice == Back_1 or Choice == Back_2:
        return True
    elif len(Choice) == 10:
        try:
            Tester = True
            day, month, year = Choice.replace("/", " ").split()
            Tester, end_date = date_chack(day, month, year, Tester)
            if start_date > end_date:
                print("\nYou can't return a car you don't have\n")
                printline()
                return True
            else:
                return end_date
        except:
            Tester = False
            print("\nERROR: Something went wrong with your input please try again\n")
            printline()

def cls():
    # This fucsun is used to clear the screen 
    os.system('cls' if os.name=='nt' else 'clear')