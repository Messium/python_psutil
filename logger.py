import os.path
from datetime import datetime

# log icons (require https://github.com/ryanoasis/nerd-fonts):

class Logger():

    '''Logger class with configuration'''

    log_indent = "\t" # not used yet

    # ICONS
    folder_icon = "📁"
    alarm_icon = "󰀡"
    icon_initalize = ""

    # DATE
    date_format = "%d/%m/%Y %H:%M:%S"
    # TODO: Can you merge these two into a oneliner?
    now = datetime.now()
    date_time = now.strftime(date_format)
    log_name = "./log3.txt"

    @staticmethod
    # creates the logger or loggit as loaded at startup.
    def logger():
        # DONE: make this class attribute better for reusablity.
        try:
            check_file = os.path.isfile(Logger.log_name)
            if not check_file:
                # DONE: make the logger not create a \n newline for this
                # method.
                Logger.logger_write(f"{Logger.icon_initalize} log file created.", mode="w", newline="")
                print(f"log file created at {Logger.date_time}")
            if check_file:
                Logger.logger_write(f"{Logger.icon_initalize} logger loaded.")
                print("logger works")
        except Exception:
            print("error no file!")

    @staticmethod
    def logger_write(write_string, mode="a", newline="\n"): # default set to append optional param set to append
        log_name = Logger.log_name
        with open(log_name, mode=f"{mode}", encoding="utf-8") as f:
            f.write(f"{newline}")
            f.write(Logger.date_time)
            f.write(" ")
            f.write(write_string)

    @staticmethod
    def logger_file_not_found(file_name):
        Logger.logger_write(f"{Logger.folder_icon} File {file_name} not found.")

    @staticmethod
    def logger_save_alarm_reached(alarm, value):
        Logger.logger_write(f"{Logger.alarm_icon} Alarm {alarm} with value {value} has been reached.")

    @staticmethod
    def logger_json_file_created(file_name):
        Logger.logger_write(f"Json file with name: {file_name} has been created.")

    # tester method:
    @staticmethod
    def test_logger():
        Logger.logger()
        Logger.logger_file_not_found("test.json")
        Logger.logger_save_alarm_reached("CPU TEST", "50")
        Logger.logger_json_file_created("test.json")

Logger.test_logger()
