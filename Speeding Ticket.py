import time
import os

speeder_list = []
wanted_list = ["Srikhar Chell Hasani", "Wilco", "Scott", "Ravi", "Trisan"]

def clr():
    os.system('cls')

def selector():
    more_speeder = input("Would you like to enter another speeder? (Y/N): ").upper().strip()
    
    
    if more_speeder == "Y":
        enter_speeder()
    
    elif more_speeder == "N":
        print(speeder_list)
    
    elif more_speeder != "Y" or "N":
        print("Please enter either Y or N.")
        time.sleep(1)
        clr()
        selector()

def enter_speeder():
    new_speeder = input("Enter the first name of the speeder: ").capitalize().strip()

    if new_speeder in wanted_list:
        print("{} is wanted for arrest. Hand him over :angry_face_cus_emojis_dont_work:".format(new_speeder))
        time.sleep(5)
        exit()

    while True:
        try:
            speed_limit = int(input("What was the speed limit?: "))
            break
        except ValueError:
            print("Please enter a number.")
    
    while True:
        try:
            speeding_speed = int(input("What was the speed of the vehicle?: "))
            break
        except ValueError:
            print("Please enter a number.")
    
    over_speed = speeding_speed - speed_limit

    if over_speed >= 30:
        print("{} lose your license.".format(new_speeder))
    money_owed = over_speed * 5
    
    elif over_speed <= 30:
        print("{} is charged ${}.".format(new_speeder, money_owed))

    counter = 0
    counter += 1

    list_input = "{}) Name: {} Money charged: {}".format(counter, new_speeder, money_owed)
    
    speeder_list.append(list_input)
    selector()

selector()