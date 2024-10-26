import psutil
from utils import Utils
from logger import Logger

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
    def monitor_mode():
        while True:

            # print("CPU", CPU())
            # print("DISK", DISK())
            # print("MEMORY", MEMORY())
            try:
                for x in json_data["CPU"]:
                    if Monitor.CPU() >= int(x):
                        print(f"ALARM! CPU value {x} has been reached")
                        Logger.logger_save_alarm_reached("CPU", x)

                for x in json_data["DISK"]:
                    if Monitor.DISK() >= int(x):
                        print(f"ALARM! DISK value {x} has been reached")
                        Logger.logger_save_alarm_reached("DISK", x)

                for x in json_data["MEMORY"]:
                    if Monitor.MEMORY() >= int(x):
                        print(f"ALARM! MEMORY value {x} has been reached")
                        Logger.logger_save_alarm_reached("MEMORY", x)
            except KeyboardInterrupt:
                break
