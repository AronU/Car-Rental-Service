# Gets acces to the printline funcson in the Universal_func named un_func in the code
# All over the place in the ui
from ui.Universal_func import printer, printline, Full_name_input_chack
import ui.Universal_func as un_func
from services.CarService import CarService

#Constant variable used to take in commands toru the input
Back_1 = "B"
Back_2 = "BACK"
Home_1 = "M"
Home_2 = "MAIN MENU"
def Dontreturncar():
    # The Dontreturncar function is used to make sure that when the user want to go back to the 
    # mane menu that the system does not return the car.
    count = 3
    licence_plate = "0"
    return count, licence_plate

def returncar():
    # This function is used to return a car after it is rented out 
    car_service = CarService()
    count = 1
    while count != 3:
        if count == 1:
            print("Enter in the licence plate of the car you want to return.\n")
            un_func.printer()
            licence_plate = input("Licence plate: ").upper()
            un_func.printline()
            if licence_plate == Home_1 or licence_plate == Home_2 or licence_plate == Back_1 or licence_plate == Back_2:
                count, licence_plate = Dontreturncar()
            #If the check is True then we know if the licence plate is in the system and rented out
            elif car_service.valid_check_licence_plate(licence_plate) == True and car_service.check_if_car_is_rented(licence_plate) == True:
                count += 1
            else:
                print("\nERROR: The licence plate you entered is not in the system or not currently rented out\n")
                un_func.printline()

        elif count == 2:
            print("Are you sure you what to return the car (Y/N): " + licence_plate +" ?\n")
            un_func.printer()
            Y_or_N = input("Choice: ").upper()
            un_func.printline()
            if Y_or_N == Home_1 or Y_or_N == Home_2:
                count, licence_plate = Dontreturncar()
            elif Y_or_N == Back_1 or Y_or_N == Back_2 or Y_or_N == "N":
                count -= 1
            elif Y_or_N == "Y":
                count += 1
    return licence_plate