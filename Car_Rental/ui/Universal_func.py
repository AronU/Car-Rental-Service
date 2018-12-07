import string
from datetime import date
def printer():
    # The printer function is used to make the command options more visible to the user anywhere he needs it
    print("B.  Back one window")
    print("H.  Main menu")
    print("--"*25)

def printline():
    # The printline function is used to Print a line of --- anywhere it is needs
    print("--"*25)

<<<<<<< HEAD
<<<<<<< HEAD
def name_input_chack(name):
=======
def name_input_check(name):
>>>>>>> f797c372741cecdef646eea97cd35ba6a2a24d49
    name_list = []
    name_list = name.split()
    print(name_list)


def ssn_input_check(ssn):
    pass

def address_input_check(address):
    pass

def phone_input_check(phone):
    pass
    
def birthday_input_check(birthday):
    pass

def paymant_input_check(paymant):
    pass

def Licence_plate_input_check(Licence_plate):
    pass

=======
def Full_name_input_chack(name):
    # This function is used to chack if the full name is properly inputid in the system
    name_list = name.split()
    Tester = True

    if len(name_list) <= 1:# chacks if the input is just one word
        Tester = False
        print("\nFull name was not entered\n")
        printline()

    elif len(name_list) > 1:# chacks if the input contanes a number or a symbol
        for word in name_list:
            for letter in word:
                T_or_F = letter.isdigit()
                if T_or_F == True:
                    Tester = False
                    print("\nNumber can be used in your name\n")
                    printline()
                elif letter in string.punctuation:
                    Tester = False
                    print("\nname can not contain a symbol\n")
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
        print("\nSSN contains 10 letters but you but in "+ str(len(ssn)) +"\n")
        printline()
    elif T_or_F == False:
        Tester = False
        print("\nSSN can not contain a letters\n")
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
        print("\nphone nuber can not contain a letters\n")
        printline()
    elif len(phone) < 7 or len(phone) > 7:
        Tester = False
        print("\nphone nuber can not contain a more or less then 7 nubers\n")
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
        birthday = date(int(year), int(month), int(day))
        print(birthday)
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


def Licence_plate_input_chack(Licence_plate):
    # This function is used to chack if the Licence_plate is properly inputid in the system
    Tester = True
    return Tester, Licence_plate
>>>>>>> cb895adc30df585f8ffefe6de3938aaee3a1ebd9
