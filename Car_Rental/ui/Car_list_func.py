from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "h"
Home_2 = "main menu"

def Carlist():
    count = True
    while count == True:
        print("1.  Available cars\n2.  Unavailable cars\n")
        un_func.printer()
        Choice = input("Choice: ").lower()
        un_func.printline()
        if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
            count = False