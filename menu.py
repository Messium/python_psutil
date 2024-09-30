from logger import logger_setup
import psutil
import os

# HOME PATH
def get_home_path():
    path = "$HOME"
    # gets user $HOME director
    def get_home_directory_with_expanduser():
        return os.path.expanduser("~")
    home_dir = get_home_directory_with_expanduser()
    return home_dir

# END HOME PATH

def get_cpu_percent():
    print(psutil.cpu_percent(1))

def get_disk_usage():
    return psutil.disk_usage(get_home_path())


def menu():
    while True:
        print("->choose one alternative: cpu_percent, disk_usage")
        user_input = input()
        if user_input == "cpu_percent":
            get_cpu_percent()
        elif user_input == "disk_usage":
            disk_usage_params = input("välj ett alternativ 1. total, 2. used or 3. free")
            if disk_usage_params == "total":
                print(get_disk_usage()[1])
            elif disk_usage_params == "used":
                print(get_disk_usage()[2])
            elif disk_usage_params == "free":
                print(get_disk_usage()[3], "%")
        elif user_input == "exit":
            break
        else:
            print("felaktig input error försök igen")

logger_setup()
menu()
