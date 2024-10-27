import psutil
from utils import Utils
from logger import Logger
from sys import platform
import subprocess

json_data = Utils.read_alarms_json()

class Monitor():
    monitor = False
    update_freq = 1

    @staticmethod
    # @classmethod
    def monitor_start():
        # Check if already started
        if Monitor.monitor:
            print("monitor already started")
        # cls.monitor = Monitor.monitor
        # Startar övervakning av CPU användning, minnesanvändning och diskanvändning.
        # Notera alltså att ingen övervakning ska starta automatiskt vid programstart
        else:
            print("monitor started")
            Monitor.monitor = True
            Logger.logger_write("Monitor started")
            # return print(Monitor.monitor)

    @staticmethod
    def MEMORY():
        return psutil.virtual_memory()[2]

    @staticmethod
    def DISK():
        return psutil.disk_usage('/')[3]

    @staticmethod
    def CPU():
        return psutil.cpu_percent(interval=1)

    # TODO: compare class monitor_mode


    @staticmethod
    def run_command(cmd):
        try:
            # Kör git-kommandot med subprocess
            result = subprocess.Popen(cmd)
            return result.stdout
        except Exception as error:
            return f"There was an error: {error}"

    @staticmethod
    def monitor_mode():
        while True:

            # print("CPU", CPU())
            # print("DISK", DISK())
            # print("MEMORY", MEMORY())
            try:
                # future implement add concurrency https://docs.python.org/3/library/multiprocessing.htmlhttps://docs.python.org/3/library/multiprocessing.html
                for x in json_data["CPU"]:
                    if Monitor.CPU() >= int(x):
                        print(f"ALARM! CPU value {x} has been reached")
                        Logger.logger_save_alarm_reached("CPU", x)
                        if platform == "linux" or platform == "linux2":
                        # TODO: make this a function/method
                            command = ["notify-send", "ALARM! CPU value", f"{x} has been reached", "--icon=dialog-crital"]
                            Monitor.run_command(command)

                for x in json_data["DISK"]:
                    if Monitor.DISK() >= int(x):
                        print(f"ALARM! DISK value {x} has been reached")
                        Logger.logger_save_alarm_reached("DISK", x)
                        if platform == "linux" or platform == "linux2":
                            command = ["notify-send", "ALARM! DISK value", f"{x} has been reached", "--icon=dialog-crital"]
                            Monitor.run_command(command)

                for x in json_data["MEMORY"]:
                    if Monitor.MEMORY() >= int(x):
                        print(f"ALARM! MEMORY value {x} has been reached")
                        Logger.logger_save_alarm_reached("MEMORY", x)
                        if platform == "linux" or platform == "linux2":
                            command = ["notify-send", "ALARM! MEMORY value", f"{x} has been reached", "--icon=dialog-crital"]
                            Monitor.run_command(command)

            except KeyboardInterrupt:
                break
