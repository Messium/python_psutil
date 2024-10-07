from utils import Utils
from menu import menu_startup

pointer = Utils.pointer() # Objekt av klass metoden pointer() från Utils klassen.

class Alarms:
    def __init__(self):
        self.alarms = {} # instansattribut
        self.alarms["minnesanvändning"] = [] # instansattribut
        self.alarms["cpuanvändning"] = [] # instansattribut
        self.alarms["diskanvändning"] = [] # instansattribut
    KEY_MIN = "minnesanvändning" # KEY namnet är motiverat för det är en dictionary. # klassattribut
    KEY_CPU = "cpuanvändning" # KEY namnet är motiverat för det är en dictionary. # klassattribut
    KEY_DISK = "diskanvändning" # KEY namnet är motiverat för det är en dictionary. # klassattribut
    options = [KEY_MIN, KEY_CPU, KEY_DISK, "gå tillbaka till huvudmenyn"] # klassattribut
    # TODO: make this the menu options as a class to be used in menu, alarms and monitor

    @classmethod
    def options_menu(cls):
        # TODO:
        options = Alarms.options
        message = "Create an alarm for:"
        print(message)
        for num, item in enumerate(options, 1):
            print(pointer, str(num), str(item))
        user_input = input()

class menu_options():
    pass # create menu options with message: "Create an alarm for:"

alarms = Alarms() # instance of Alarms object that inherit all dictionaries and alises
# that is KEY_n that I defined earlier.
# setup alarms init end
print(alarms.alarms)


def alarm_create():
    while True:
        user_input = Alarms.options_menu()
        if user_input == "1":
            print("start alarm för", options[0])
            print("desired %?")
            user_input = input()
            alarms[options[0]] = user_input # options
        elif user_input == "2":
            # print("start alarm för", options[1])
            # print("desired %?")
            user_input = input()
            ## REVIEW:
            # try:
            #     val = int(user_input)
            # except ValueError:
            #     print("That's not an int!")
            # if user_input in alarms["minnesanvändning"]:
            if user_input in alarms.alarms[alarms.KEY_MIN]:
                print("already activated")
                continue
            if int(user_input) > 100:
                print("please choose a number between 1-100")
                continue
            if int(user_input) <= 0:
                print("please choose a number between 1-100")
            else:
                alarms.alarms[alarms.KEY_MIN].append(user_input)
                print("activated:", alarms.alarms[alarms.KEY_MIN])
            # if not alarms["minnesanvändning"]:
            #     print("empty list")

            # if "minnesanvändning" in alarms.keys():
            #     print(alarms["minnesanvändning"])
            #
            #     for x in alarms["minnesanvändning"]:
            #         if x == user_input:
            #             print("value already added")
            #         else:
            #             alarms["minnesanvändning"].append(user_input)
            # 1. check for existing alarm if yes append to a list in the
            # dictionary key named "minnesanvändning".
            # alarms[options[1]] = [user_input]
        elif user_input == "3":
            print("start alarm för", options[2])
            print("desired %?")
            user_input = input()
            alarms[options[2]] = user_input
        elif user_input == "4":
            print("start alarm för", options[3])
        elif user_input == "return":
            menu_startup()
        # else:
        #     print("do something else")
            # return to main meny

def alarm_remove():
    pass

def alarm_list_active():
    for monitor_category_name, value in alarms.items():
        print(monitor_category_name, value)

    pass


user_input = Alarms.options_menu()
# alarm_create()
