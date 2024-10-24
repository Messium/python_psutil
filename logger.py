import os.path
from datetime import datetime

# log icons (require https://github.com/ryanoasis/nerd-fonts):

class Logger():

    '''Logger class with configuration'''

    log_write_spacing = " --- "

    # ICONS
    folder_icon = "📁"
    alarm_icon = "󰀡"
    json_icon = ""
    icon_initalize = ""

    # DATE
    date_format = "%d/%m/%Y %H:%M:%S"
    # TODO: Can you merge these two into a oneliner?
    now = datetime.now()
    date_time = now.strftime(date_format)
    log_save_path = "./" # REVIEW: need to be able to handle ""?.
    log_name = "log.txt"
    log_full_save = log_save_path + log_name

    @staticmethod
    # REVIEW: WIP no support for log_save_path = "" handeling
    # Check if path exist or not else create it.
    def logger_path():
        # try catch here instead
        isExist = os.path.exists(Logger.log_save_path)
        if isExist is None:
            # ERROR handling for none correctly formated path
            print("error this is no path name")
        elif not isExist:
            os.makedirs(Logger.log_save_path)
            print("The new directory is created!")
            # TODO: create a log entry again for the folder created
            # Make filepath a new method

    @staticmethod
    # creates the logger or loggit as loaded at startup.
    def logger():
        Logger.logger_path()
        try:
            check_file = os.path.isfile(Logger.log_full_save)
            if not check_file:
                Logger.logger_write(f"{Logger.icon_initalize} log file created.", mode="w", newline="")
                print(f"log file created at {Logger.date_time}")
            if check_file:
                Logger.logger_write(f"{Logger.icon_initalize} logger loaded.")
                print("logger loaded")
        # except Exception:
        except FileNotFoundError:
            print("error no file!")

    @staticmethod
    def logger_write(write_string, mode="a", newline="\n"): # default set to append optional param set to append
        with open(Logger.log_full_save, mode=f"{mode}", encoding="utf-8") as f:
            f.write(f"{newline}")
            f.write(Logger.date_time)
            f.write(Logger.log_write_spacing)
            f.write(write_string)

    # TODO: make it absolute path instead
    @staticmethod
    def logger_file_not_found(file_name):
        Logger.logger_write(f"{Logger.folder_icon} File {file_name} not found.")

    @staticmethod
    def logger_save_alarm_reached(alarm, value):
        Logger.logger_write(f"{Logger.alarm_icon} Alarm {alarm} with value {value} has been reached.")

    @staticmethod
    def logger_json_file_created(file_name):
        Logger.logger_write(f"{Logger.json_icon} Json file with name: {file_name} has been created.")

    # tester method:
    @staticmethod
    def test_logger():
        Logger.logger()
        Logger.logger_file_not_found("test.json")
        Logger.logger_save_alarm_reached("CPU TEST", "50")
        Logger.logger_json_file_created("test.json")

Logger.test_logger()
