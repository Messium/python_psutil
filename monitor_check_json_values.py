import psutil
from utils import Utils
from logger import Logger

json_data = Utils.read_alarms_json()

# HELP: what does unbound variable mean?


class Monitor():

    def MEMORY(self):
        return psutil.virtual_memory()[2]
    def DISK(self):
        return psutil.disk_usage('/')[3]
    def CPU(self):
        return psutil.cpu_percent(interval=1)

    # TODO: compare class monitor_mode

    def monitor_mode():
        while True:

            # print("CPU", CPU())
            # print("DISK", DISK())
            # print("MEMORY", MEMORY())
            try:
                for x in json_data["CPU"]:
                    if monitorize.CPU() >= int(x):
                        print(f"ALARM! CPU value {x} has been reached")
                        Logger.logger_save_alarm_reached("CPU", x)

                for x in json_data["DISK"]:
                    if monitorize.DISK() >= int(x):
                        print(f"ALARM! DISK value {x} has been reached")
                        Logger.logger_save_alarm_reached("DISK", x)

                for x in json_data["MEMORY"]:
                    if monitorize.MEMORY() >= int(x):
                        print(f"ALARM! MEMORY value {x} has been reached")
                        Logger.logger_save_alarm_reached("MEMORY", x)
            except KeyboardInterrupt:
                break
