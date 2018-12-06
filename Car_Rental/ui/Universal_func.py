def printer():
    # The printer function is used to make the command options more visible to the user anywhere he needs it
    print("B.  Back one window")
    print("H.  Main menu")
    print("--"*25)

def printline():
    # The printline function is used to Print a line of --- anywhere it is needs
    print("--"*25)

def Full_name_input_chack(name):
    name_list = name.split()
    Tester = True

    if len(name_list) <= 1:
        Tester = False
        print(" \nFull name was not entered\n ")
        printline()

    elif len(name_list) > 1:
        for word in name_list:
            for letter in word:
                T_or_F = letter.isdigit()
                if T_or_F == True:
                    Tester = False
                    print("Number can be used in your name")
                    printline()

    else:
        name = ""
        for word in name_list:
            name = name + " " + word.capitalize()

    return Tester, name




#  def ssn_input_chack(ssn):
#     pass


#  def address_input_chack(address):
#     pass


#  def phone_input_chack(phone):
#     pass
    
    
# def birthday_input_chack(birthday):
#     pass


#  def paymant_input_chack(paymant):
#     pass


#  def Licence_plate_input_chack(Licence_plate):
#     pass


