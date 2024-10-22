import os

import psutil


class Utils:

    # graphical element

    @staticmethod
    def pointer():
        return ">"

    @staticmethod
    def alarms_options():
        options = ["CPU", "MEMORY", "DISK", "gå tillbaka till huvudmenyn", "exit application", "save"]  # klassattribut
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
