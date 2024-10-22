import os.path
import textwrap
from datetime import datetime


class Logger():

    log_indent = "\t" # not used yet
    # log icons (require https://github.com/ryanoasis/nerd-fonts):
    folder_icon = "📁"
    alarm_icon = "󰀡"
    icon_initalize = ""
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    # creates the logger or loggit as loaded at startup.
    def logger():
        # DONE: make this class attribute better for reusablity.
        try:
            log_path = './log.txt'
            check_file = os.path.isfile(log_path)
            if not check_file:
                # TODO: make the logger not create a \n newline for this
                # method.
                Logger.logger_write(f"{Logger.icon_initalize} log file created.")
                print(f"log file created at {Logger.date_time}")
            if check_file:
                Logger.logger_write(f"{Logger.icon_initalize} logger loaded.")
                print("logger works")
        except Exception:
            print("error no file!")

    @staticmethod
    def logger_write(write_string):
        with open("log.txt", mode="a") as f:
            f.write("\n")
            f.write(Logger.date_time)
            f.write(" ")
            f.write(write_string)

    @staticmethod
    def logger_file_not_found(file_name):
        Logger.logger_write(f"{Logger.folder_icon} File {file_name} not found.")

    @staticmethod
    def logger_save_alarm_reached(alarm, value):
        with open("log.txt", mode="a") as f:
            write_string = f"{Logger.alarm_icon} Alarm {alarm} with value {value} has been reached."
            f.write("\n")
            f.write(Logger.date_time)
            f.write(" ")
            f.write(write_string)

    @staticmethod
    def logger_json_file_created(file_name):
        with open("log.txt", mode="a") as f:
            write_string = f"Json file with name: {file_name} has been created."
            f.write("\n")
            f.write(Logger.date_time)
            f.write(" ")
            f.write(write_string)

    # tester method:
    @staticmethod
    def test_logger():
        Logger.logger()
        Logger.logger_file_not_found("test.json")
        Logger.logger_save_alarm_reached("CPU TEST", "50")
        Logger.logger_json_file_created("test.json")

Logger.test_logger()
