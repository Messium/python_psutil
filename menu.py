from logger import logger_setup
import monitor
import psutil
import os

# HOME PATH
def get_home_path():
    # gets user $HOME director
    def get_home_directory_with_expanduser():
        return os.path.expanduser("~")
    home_dir = get_home_directory_with_expanduser()
    return home_dir
# END HOME PATH

def get_disk_usage():
    return psutil.disk_usage(get_home_path())

def menu():
    while True:
        print("> choose one alternative: cpu, disk, memor, memory")
        user_input = input()
        if user_input == "cpu":
            user_input = input("> choose: cpu_percent, cpu_count")
            if user_input == "cpu_percent":
                print(psutil.cpu_percent(1))
            if user_input == "cores":
                print(psutil.cpu_count(), "cores")
        elif user_input == "disk":
            disk_usage_params = input("> choose: 1. total, 2. used or 3. free")
            if disk_usage_params == "total":
                print(psutil.disk_usage(get_home_path())[1])
            elif disk_usage_params == "used":
                print(get_disk_usage()[2])
            elif disk_usage_params == "free":
                print(get_disk_usage()[3], "%")
        elif user_input == "memory":
                print(psutil.virtual_memory()[2], "%")
        elif user_input == "exit":
            break
        else:
            print("felaktig input error försök igen")

logger_setup()
menu()
