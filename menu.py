import os

# import color_codes
import alarm
import monitor
import psutil
from logger import logger_setup
from utils import Utils

pointer = Utils.pointer() # Objekt av klass metoden pointer från Utils klassen.


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

def menu_startup():
    while True:
        options = [
            "Starta övervakning",
            "Lista aktiv övervakning",
            "Skapa larm",
            "Visa larm",
            "Starta övervakningsläge"
        ]
        welcome_message = "hello and welcome choose an option:"
        print(pointer, welcome_message)
        for num, item in enumerate(options, 1):
            print(pointer, str(num), str(item))
        user_input = input()
        if user_input == "1":
            monitor.monitor_start()
        elif user_input == "2":
            monitor.monitor_list_active()
        elif user_input == "3":
            alarm.alarm_create()
        elif user_input == "4":
            alarm.alarm_list_active()
        elif user_input == "5":
            monitor.monitor_monitorize()
        elif user_input == "exit":
            break
        else:
            print("bad input")


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
menu_startup()
