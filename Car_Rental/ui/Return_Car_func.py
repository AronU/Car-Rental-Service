# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, Full_name_input_chack
import ui.Universal_func as un_func
from services.CarService import CarService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"


count = 1
while count != 3:
    if count == 1:
        print("Enter in the licence plate of the car you want to return.")
        un_func.printer()
        licence_plate = input("Choice: ").lower()
        un_func.printline()
        count += 1
        if licence_plate == Home_1 or licence_plate == Home_2:
            # count, name, ssn, address, phone, birthday = DontMakeUser()
        elif licence_plate == Back_1 or licence_plate == Back_2:
            # count, name, ssn, address, phone, birthday = DontMakeUser()
        else:

            #Tester, name = un_func.Full_name_input_chack(name)
            
            #if Tester == False:
                #count = 1
    elif count == 2:
        print("Are you sure you what to return car: " + licence_plate +"?")
        un_func.printer()
        name = input("Choice: ").lower()
        un_func.printline()