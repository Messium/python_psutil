from utils import Utils
import json
from logger import Logger

# TODO: make a branch that implement this but as a more OOP paradigm.

# TODO: need to add a appending method for new alarms to be added to already
# existing json file. First add a method that initialize an already exisiting json file, that is
# read the file into memory and give warning if no alarms.json file exists.

class Alarm:
    def __init__(self, alarm_level, alarm_type):
        self.alarm_level = alarm_level
        self.alarm_type = alarm_type

    alarms = []
    alarms_dict = {}  # intialization of alarm dictionary. WARNING: NOT IN USE
    # JUST A REMINDER

    def __str__(self):
        return f"Alarm level: {self.alarm_level}, alarm type: {self.alarm_type}"

    @classmethod
    def sort(cls):
        cls.alarms.sort(key=lambda alarm: (alarm.alarm_type, alarm.alarm_level))
        cls.sorted_alarms = cls.alarms.copy()
        #copy.copy(obj)                                      *copy()..copy.pyx*
        #    Return a shallow copy of _obj_.

    @staticmethod
    # Take a decorator from sort as input?
    def print_all():
        Alarm.sort()
        for x in Alarm.alarms:
            print(x)

    @staticmethod
    def check_existing():
        pass
        # check for existing values in Alarm.alarms to avoid duplicates.

    @staticmethod
    def delete_alarm():
        data = Utils.read_alarms_json()
        print(data)
        # så här ska listan se ut för valbara alternativ:
        # Välj ett konfigurerat larm att ta bort:
        # 5. CPU larm 70%
        # 6. Minneslarm 80%
        # 7. Minneslarm 90%

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



while True:
    Utils.alarms_options()
    user_input = input()

    if user_input == "1":
        while True:
            print("start alarm for", "CPU")
            user_input = input()
            if int(user_input) > 100 or int(user_input) <= 0:
                print("please choose a number between 1-100")
            else:
                Alarm.alarms.append(Alarm(user_input, "CPU"))
                break

    if user_input == "2":
        while True:
            print("start alarm for", "MEMORY")
            user_input = input()
            if int(user_input) > 100 or int(user_input) <= 0:
                print("please choose a number between 1-100")
            else:
                Alarm.alarms.append(Alarm(user_input, "MEMORY"))
                break

    if user_input == "3":
        while True:
            print("start alarm for", "DISK")
            user_input = input()
            if int(user_input) > 100 or int(user_input) <= 0:
                print("please choose a number between 1-100")
            else:
                Alarm.alarms.append(Alarm(user_input, "DISK"))
                break

    if user_input == "menu" or user_input == "4":
        # Before leaving to menu save to json.
        break
    if user_input == "exit" or user_input == "5":
        break
    if user_input == "save" or user_input == "6":
        Alarm.save_json()
    if user_input == "delete" or user_input == "7":
        Alarm.save_json()

Alarm.print_all()
