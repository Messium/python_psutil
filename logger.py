import os.path
import textwrap
from datetime import datetime


class Logger():

    log_indent = "\t"
    folder_icon = "📁"
    alarm_icon = "󰀡"

    @staticmethod
    def logger():
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            log_path = './log.txt'
            check_file = os.path.isfile(log_path)
            if not check_file:
                with open(log_path, mode="x") as f:
                    write_string = f"log file created at: {date_time}"
                    f.write(write_string)
                print(f"log file created at {date_time}")
            if check_file:
                # Diagnostics: Avoid equality comparisons to `True`; use `if check_file:` for truth checks [E712]
                with open(log_path, mode="a") as f:
                    # TODO: Make this string an input to a class method so its can be
                    # reusable
                    write_string = f"program initialized."
                    # TODO: make this a class method
                    f.write("\n")
                    f.write(date_time)
                    f.write(" ")
                    f.write(write_string)
                print("logfile initialized")
        except Exception:
            print("error no file!")

    @staticmethod
    def logger_file_not_found(file_name):
        # TODO: use the check if file exist from Logger.logger main function here instead
        # of recreating it think DRY. Also to ensure file existance.
        # TODO: Even better just create a utility method with staticmethod that
        # check file existance and creation.
        with open("log.txt", mode="a") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            write_string = f"{Logger.folder_icon} File {file_name} not found."
            f.write("\n")
            f.write(date_time)
            f.write(" ")
            f.write(write_string)

    @staticmethod
    def logger_save_alarm_reached(alarm, value):
        with open("log.txt", mode="a") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            write_string = f"{Logger.alarm_icon} Alarm {alarm} with value {value} has been reached."
            f.write("\n")
            f.write(date_time)
            f.write(" ")
            f.write(write_string)

    @staticmethod
    def logger_json_file_created(file_name):
        with open("log.txt", mode="a") as f:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            write_string = f"Json file with name: {file_name} has been created."
            f.write("\n")
            f.write(date_time)
            f.write(" ")
            f.write(write_string)
