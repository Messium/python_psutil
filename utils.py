import os

import psutil


class Utils:

    # graphical element

    @staticmethod
    def pointer():
        return ">"

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
