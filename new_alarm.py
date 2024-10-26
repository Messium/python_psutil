import json

from logger import Logger
from new_monitor import Monitor
from utils import Utils

# TODO: make a branch that implement this but as a more OOP paradigm.

# TODO: need to add a appending method for new alarms to be added to already
# existing json file. First add a method that initialize an already exisiting json file, that is
# read the file into memory and give warning if no alarms.json file exists.
pointer = Utils.pointer()

# TODO: add previous json_data to Alarm.alarms so that I can do an update()
# appending to it.

json_data = Utils.read_alarms_json()

class Alarm:
    def __init__(self, alarm_level, alarm_type):
        self.alarm_level = alarm_level
        self.alarm_type = alarm_type

    alarms = []

    def __str__(self):
        return f"Alarm level: {self.alarm_level}, alarm type: {self.alarm_type}"

    # TODO: this function is dupplicated also present in 4. Visa larm
    # test_create_objects_and_sort.py
    @staticmethod
    def add_json_to_alarms():
        for key in json_data.keys():
            for value in json_data.get(key):
                Alarm.alarms.append(Alarm(value, key))

    @staticmethod
    def sorted_list():
        json_data = Utils.read_alarms_json()
        alarm_list = []
        for key in json_data.keys():
            for value in json_data.get(key):
                alarm_list.append(Alarm(value, key))
        sorted_list = sorted(alarm_list, key=lambda alarm: (alarm.alarm_type, alarm.alarm_level))

        for item in sorted_list:
            print(item)


    @staticmethod
    def active_alarms():
        if Monitor.monitor:
            print("Montior active can proceed")
            json_data = Utils.read_alarms_json()
            for key, value in json_data.items():
                print(pointer, key, value)
            while True:
                try:
                    print("please press C-c or yes to return to main menu")
                    user_input = input()
                    if user_input == "yes":
                        break
                    else:
                        print("please write yes or C-c")

                except KeyboardInterrupt:
                    break
        else:
            print("please activate monitor before continue")

    @staticmethod
    # Take a decorator from sort as input?
    # get them from json then sort!
    def print_all():
        json_data = Utils.read_alarms_json()
        print(json_data)
        Alarm.sort()
        for x in Alarm.alarms:
            print(x)
        # Tryck valfri tangent för att gå tillbaka till huvudmeny

    @staticmethod
    def check_existing():
        pass
        # check for existing values in Alarm.alarms to avoid duplicates.

    # TODO: create a new structure that save a completly new strcuture if there
    # is no existing alarms.json file.

    @staticmethod
    def save_json():
        Utils.read_alarms_json()
        # TODO: check if already existing alarm before initialization of new
        # alarm.
        alarms_dict = {}  # intialization of alarm dictionary.
        alarms_dict["CPU"] = []  # create key with empty list
        alarms_dict["MEMORY"] = []  # create key with empty list
        alarms_dict["DISK"] = []  # create key with empty list
        # TODO: Needs sorting before saving.
        for x, y in enumerate(Alarm.alarms):
            print("saving", x)
            alarms_dict[f"{y.alarm_type}"].append(f"{y.alarm_level}")

        # This will overwrite on every save create a append to alarms.json
        file_name = "alarms.json"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(alarms_dict, indent=4))
        # DONE: Create a logg entry for json file created
        Logger.logger_json_file_created(file_name)

    @staticmethod
    def alarm_menu():
        while True:
            try:
                Utils.alarms_options()
                user_input = input()

                # DONE: this dosn't deal with text input!
                if user_input == "1":
                    while True:
                        print("start alarm for", "CPU")
                        try:
                            user_input = int(input())
                        except ValueError:
                            print("That's not a valid option!")
                        if int(user_input) > 100 or int(user_input) <= 0:
                            print("please choose a number between 1-100")
                        else:
                            Alarm.alarms.append(Alarm(user_input, "CPU"))
                            break

                if user_input == "2":
                    while True:
                        print("start alarm for", "MEMORY")
                        try:
                            user_input = int(input())
                        except ValueError:
                            print("That's not a valid option!")
                        if int(user_input) > 100 or int(user_input) <= 0:
                            print("please choose a number between 1-100")
                        else:
                            Alarm.alarms.append(Alarm(user_input, "MEMORY"))
                            break

                if user_input == "3":
                    while True:
                        print("start alarm for", "DISK")
                        try:
                            user_input = int(input())
                        except ValueError:
                            print("That's not a valid option!")
                        if int(user_input) > 100 or int(user_input) <= 0:
                            print("please choose a number between 1-100")
                        else:
                            Alarm.alarms.append(Alarm(user_input, "DISK"))
                            break

                if user_input == "save" or user_input == "4":
                    Alarm.save_json()

                if user_input == "return" or user_input == "5":
                    break
            except KeyboardInterrupt:
                break

Alarm.add_json_to_alarms()
