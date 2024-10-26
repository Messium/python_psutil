import os
import json

import psutil
from logger import Logger
import tomllib

with open("configuration.toml", "rb") as f:
    toml_data = tomllib.load(f)

menu_elems = toml_data.get("menu")
# HELP: posible unbound variable here aswell

class Utils:


    @staticmethod
    def welcome_message():
        welcome_message = menu_elems.get("welcome_message")
        if welcome_message:
            return welcome_message
        else:
            return "Hello and welcome choose an optioN:"

    @staticmethod
    def pointer():
        config_pointer = menu_elems.get("pointer")
        if config_pointer:
            return config_pointer
        else: # toml return None if no value is specified so default to this:
            return ">"

    @staticmethod
    def alarms_options():
        options = ["CPU", "MEMORY", "DISK", "save", "return"]  # klassattribut
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
                print("loading previously configured alarms...")
                return data
        except FileNotFoundError:
            print("no json monitor file found")
            Logger.logger_file_not_found(json_file_name)

    @staticmethod
    def save_alarm_json():
        try:
            json_file_name = "alarms.json"
            with open(json_file_name, mode="w", encoding="utf-8") as f:
                json.dump(Delete_alarm.data, f)
        except FileNotFoundError:
            pass


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
