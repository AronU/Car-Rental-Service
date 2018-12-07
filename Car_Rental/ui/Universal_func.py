import string
from datetime import datetime
def printer():
    # The printer function is used to make the command options more visible to the user anywhere he needs it
    print("B.  Back one window")
    print("H.  Main menu")
    print("--"*25)

def printline():
    # The printline function is used to Print a line of --- anywhere it is needs
    print("--"*25)

def Full_name_input_chack(name):
    # This function is used to chack if the full name is properly inputid in the system
    name_list = name.split()
    Tester = True

    if len(name_list) <= 1:# chacks if the input is just one word
        Tester = False
        print("\nERROR: Full name was not entered\n")
        printline()

    elif len(name_list) > 1:# chacks if the input contanes a number or a symbol
        for word in name_list:
            for letter in word:
                T_or_F = letter.isdigit()
                if T_or_F == True:
                    Tester = False
                    print("\nERROR: Number can be used in your name\n")
                    printline()
                elif letter in string.punctuation:
                    Tester = False
                    print("\nERROR: Name can not contain a symbol\n")
                    printline()

    else:# if it is a full name betar make sur it is capitalized
        name = ""
        for word in name_list:
            name = name + " " + word.capitalize()

    return Tester, name

def ssn_input_chack(ssn):
    # This function is used to chack if the ssn is properly inputid in the system
    Tester = True
    T_or_F = ssn.isdigit()
    if len(ssn) > 10 or len(ssn) < 10:
        Tester = False
        print("\nERROR: SSN contains 10 letters but you but in "+ str(len(ssn)) +"\n")
        printline()
    elif T_or_F == False:
        Tester = False
        print("\nERROR: SSN can not contain a letters\n")
        printline()
    return Tester, ssn


def address_input_chack(address):
    # This function is used to chack if the address is properly inputid in the system
    Tester = True
    return Tester, address


def phone_input_chack(phone):
    # This function is used to chack if the phone is properly inputid in the system
    Tester = True
    T_or_F = phone.isdigit()
    if T_or_F == False:
        Tester = False
        print("\nERROR: phone nuber can not contain a letters\n")
        printline()
    elif len(phone) < 7 or len(phone) > 7:
        Tester = False
        print("\nERROR: phone nuber can not contain a more or less then 7 nubers\n")
        printline()
    return Tester, phone
    
    
def birthday_input_chack(birthday):
    # This function is used to chack if the birthday is properly inputid in the system
    Tester = True
    def number_chack(day, month, year, Tester):
        birthday = day + month + year
        for number in birthday:
            T_or_F = number.isdigit()
            if T_or_F == False:
                Tester = False
        print(len(year))
        print(day)
        print(month)
        print(year)
        if len(day) != 2:
            print("ERROR: Day must be represented with 2 numbers such as this: 06 or 15")
        elif len(month) != 2:
            print("ERROR: Month must be represented with 2 numbers such as this: 06 or 12")
        elif len(year) != 4:
            print("ERROR: Year must be represented with 4 numbers such as this: 1985 or 2000")
        else:
            try:
                birthday = datetime(int(year), int(month), int(day))
            except ValueError as ex:
                print("\nERROR: "+ str(ex) + "\n")
                printline()
                Tester = False
        
        return Tester, birthday

    
    birthday_list = []
    for word in birthday:
        birthday_list.append(word)

    if len(birthday) == 10:
        day = birthday_list[0] + birthday_list[1]
        month = birthday_list[3] + birthday_list[4]
        year = birthday_list[6] + birthday_list[7] + birthday_list[8] + birthday_list[9]
        Tester, birthday = number_chack(day, month, year, Tester)

    elif len(birthday) == 8:
        day = birthday_list[0] + birthday_list[1]
        month = birthday_list[2] + birthday_list[3]
        year = birthday_list[4] + birthday_list[5] + birthday_list[6] + birthday_list[7]
        Tester, birthday = number_chack(day, month, year, Tester)


    return Tester, birthday


def paymant_input_chack(paymant):
    # This function is used to chack if the paymant is properly inputid in the system
    Tester = True
    return Tester, paymant
