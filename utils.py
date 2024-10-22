import os
import json

import psutil
from logger import Logger

# HELP: posible unbound variable here aswell

class Utils:

    # graphical element

    @staticmethod
    def pointer():
        return ">"

    @staticmethod
    def alarms_options():
        options = ["CPU", "MEMORY", "DISK", "gå tillbaka till huvudmenyn",
                   "exit application", "save"]  # klassattribut
        message = "Create an alarm for:"
        print(message)
        for num, item in enumerate(options, 1):
            print(Utils.pointer(), str(num), str(item))

    @staticmethod
    def get_home_path():
        # gets user $home director
        def get_home_directory_with_expanduser():
            return os.path.expanduser("~")
        home_dir = get_home_directory_with_expanduser()
        return home_dir

    @staticmethod
    def read_alarms_json():
        try:
            json_file_name = "alarms.json"
            with open(json_file_name, mode="r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print("no json monitor file found")
            Logger.logger_file_not_found(json_file_name)

    # psutil statistics

    @classmethod
    def get_disk_usage(cls):
        return psutil.disk_usage(Utils.get_home_path())[3]  # % return

    @classmethod
    def cpu_percent(cls):
        return psutil.cpu_percent()

    @classmethod
    def memory_usage(cls):
        return psutil.virtual_memory()
