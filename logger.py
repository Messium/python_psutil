import os.path
from datetime import datetime


def logger_setup():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    log_path = './log.txt'

    check_file = os.path.isfile(log_path)

    if check_file == False:
        with open(log_path, mode="x") as file:
            write_string = f"log file created at: {date_time}"
            file.write(write_string)
    if check_file == True:
        with open(log_path, mode="a") as file:
            write_string = f"program initialized: {date_time}"
            file.write("\n")
            file.write(write_string)
        print("logfile initialized")


