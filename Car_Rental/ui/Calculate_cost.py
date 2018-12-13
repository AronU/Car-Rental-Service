from ui.Universal_func import printer, printline
import ui.Universal_func as un_func

from ui.calc_cost_without_extra import calculate_cost_without_extra
import ui.calc_cost_without_extra as calc_without_extra

from ui.calc_cost_with_extra import calculate_cost_with_extra
import ui.calc_cost_with_extra as calc_with_extra

from services.CarService import CarService

#Constant variable used to take in commands toru the input
Back_1 = "b"
Back_2 = "back"
Home_1 = "m"
Home_2 = "main menu"


def calculate_cost_menu():
        count = True
        while count == True:
                print("Calculate cost with or without extra insurence ?\n")
                print("1.  Without insurence\n2.  With insurence\n")
                un_func.printer()
                Choice = input("Choice: ").lower()
                un_func.printline()
                if Choice == Home_1 or Choice == Home_2 or Choice == Back_1 or Choice == Back_2:
                        count = False
                elif Choice == "1":
                        count = calc_without_extra.get_car()
                elif Choice == "2":
                        count = calc_with_extra.get_car()

        