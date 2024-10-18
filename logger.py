import os.path
from datetime import datetime


class Logger():

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
                    write_string = f"program initialized: {date_time}"
                    f.write("\n")
                    f.write(write_string)
                print("logfile initialized")
        except Exception:
            print("error no file!")
