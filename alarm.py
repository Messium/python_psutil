from menu import menu_startup
from utils import Utils

# import menu

main_menu = menu_startup()
# Objekt av klass metoden pointer() från Utils klassen.
pointer = Utils.pointer()


class Alarms:
    def __init__(self):
        self.alarms = {}  # instansattribut
        self.alarms["minnesanvändning"] = []  # instansattribut
        self.alarms["cpuanvändning"] = []  # instansattribut
        self.alarms["diskanvändning"] = []  # instansattribut
    pointer = Utils.pointer()
    # KEY namnet är motiverat för det är en dictionary. # klassattribut
    KEY_MIN = "minnesanvändning"
    # KEY namnet är motiverat för det är en dictionary. # klassattribut
    KEY_CPU = "cpuanvändning"
    # KEY namnet är motiverat för det är en dictionary. # klassattribut
    KEY_DISK = "diskanvändning"
    alarms_dict = {}  # intialization of alarm dictionary.
    alarms_dict[KEY_MIN] = []  # create key with empty list
    alarms_dict[KEY_CPU] = []  # create key with empty list
    alarms_dict[KEY_DISK] = []  # create key with empty list
    KEY_OPTIONS = [KEY_MIN, KEY_CPU, KEY_DISK]
    options = [KEY_MIN, KEY_CPU, KEY_DISK,
               "gå tillbaka till huvudmenyn", "exit application"]  # klassattribut
    # options = [KEY_MIN, KEY_CPU, KEY_DISK, "gå tillbaka till huvudmenyn", "exit application"] # klassattribut
    # TODO: make this the menu options as a class to be used in menu, alarms and monitor

    # @classmethod
    # def options_menu(cls):
    @classmethod  # decorator
    def options_menu(cls):
        # TODO:
        options = Alarms.options  # klassattributet options från Alarms.
        # HELP: Hur får jag instansattributet self.alarms till den här metoden?
        # alarms = Alarms.__init__ # how to get self.alarms here?
        while True:
            message = "Create an alarm for:"
            print(message)

            for num, item in enumerate(options, 1):
                print(pointer, str(num), str(item))
            user_input = input()

            if user_input == "1":
                print("start alarm för", options[0])
                print("desired %?")
                user_input = input()
                # alarms.alarms["KEY_MIN"] = user_input # options # need self.alarms first..

                if user_input in Alarms.alarms_dict[f"{Alarms.KEY_MIN}"]:
                    print("already activated")
                    continue
                if int(user_input) > 100:
                    print("please choose a number between 1-100")
                    continue
                if int(user_input) <= 0:
                    print("please choose a number between 1-100")
                    continue
                else:
                    Alarms.alarms_dict[Alarms.KEY_MIN].append(user_input)
                    print("activated:",
                          Alarms.alarms_dict[f"{Alarms.KEY_MIN}"])

            elif user_input == "2":
                print("start alarm för", options[1])
                print("desired %?")
                user_input = input()
                if user_input.isdigit():
                    print("its a digit")
                else:
                    print("is not a digit")
            elif user_input == "3":
                print("start alarm för", options[1])
                print("desired %?")
                user_input = input()
                if user_input.isdigit():
                    print("its a digit")
                else:
                    print("is not a digit")
            elif user_input == "4":
                pass
            elif user_input == "5":
                break
            else:
                print("not valid input")

            # OBS det här fungerar för att ändra klassattribut men jag borde
            # göra om det till instansattribut för att skapa ett objekt som
            # kan skickas till menu.py

    @classmethod  # decorator
    def active_alarms(cls):
        # list all alarms_dict active alarms. TODO: Hide key if list is empty.
        # 🏁 this works good enough for the moment
        if Alarms.alarms_dict[Alarms.KEY_MIN] == [] and Alarms.alarms_dict[Alarms.KEY_CPU] == [] and Alarms.alarms_dict[Alarms.KEY_DISK] == []:
            print("no active alarms")
        else:
            for key in Alarms.KEY_OPTIONS:
                Alarms.alarms_dict[key].sort()

                # print(pointer, f"{key}:", Alarms.alarms_dict[key])
                # print(pointer, f"{key}:")
                # print(', '.join(Alarms.alarms_dict[key]))

                print(pointer, f"{key}:", ', '.join(Alarms.alarms_dict[key]))
            # TODO: add % sign
            # print(', '.join(Alarms.alarms_dict[key]))
            # alarms_instance.alarms_dict[Alarms.KEY_MIN].sort()
            # alarms_instance.alarms_dict[Alarms.KEY_CPU].sort()
            # alarms_instance.alarms_dict[Alarms.KEY_DISK].sort()
        # print(pointer, f"{Alarms.KEY_MIN}: ", Alarms.alarms_dict[Alarms.KEY_MIN])
        # print(pointer, f"{Alarms.KEY_CPU}: ", Alarms.alarms_dict[Alarms.KEY_CPU])
        # print(pointer, f"{Alarms.KEY_DISK}: ", Alarms.alarms_dict[Alarms.KEY_DISK])
        # TODO: sort alarms before print.

    @classmethod  # decorator
    def add_alarm(cls):  # for testing
        pass
        # Alarms.alarms_dict[Alarms.KEY_MIN].append("10") # just for TEST
        # Alarms.alarms_dict[Alarms.KEY_CPU].append("10") # just for TEST
        # Alarms.alarms_dict[Alarms.KEY_DISK].append("10") # just for TEST

    @classmethod  # decorator
    def clear_alarm(cls):  # for testing
        # 1. clear by KEY
        # Alarms.alarms_dict[Alarms.KEY_MIN].clear() # TEST remove all alarms in the list of the key "minnesanvändning".
        # 2. clear all
        Alarms.alarms_dict.clear()  # clear whole dictionary

    @classmethod  # decorator
    def delete_alarm(cls):  # for deleting an especfic alarm in the list
        if "10" in Alarms.alarms_dict[Alarms.KEY_MIN]:
            # TEST remove all alarms in the list of the key "minnesanvändning".
            Alarms.alarms_dict[Alarms.KEY_MIN].remove("10")
            print("value 10 removed from list")
        else:
            print("10 not in list")
        # TODO: needs to check if exist before .remove()


class menu_options():
    pass  # create menu options with message: "Create an alarm for:"


# instance of Alarms object that inherit all dictionaries and alises
alarms_instance = Alarms()
# that is KEY_n that I defined earlier.
# setup alarms init end
print(alarms_instance.alarms_dict)
alarms_instance.add_alarm()
# alarms_instance.delete_alarm()
alarms_instance.active_alarms()


user_input = Alarms.options_menu()
