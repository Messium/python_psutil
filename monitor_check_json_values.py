import json
import psutil
from logger import Logger

try:
    json_file_name = "alarms.json"
    with open(json_file_name, mode="r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("no json monitor file found")
    Logger.logger_file_not_found(json_file_name)

# print(mem)

# data["CPU"]
def MEMORY():
    return psutil.virtual_memory()[2]
def DISK():
    return psutil.disk_usage('/')[3]
def CPU():
    return psutil.cpu_percent(interval=1)

for x in data["CPU"]:
    if CPU() >= int(x):
        print(f"ALARM! CPU value {x} has been reached")
        Logger.logger_save_alarm_reached("CPU", x)

for x in data["DISK"]:
    if DISK() >= int(x):
        print(f"ALARM! DISK value {x} has been reached")
        Logger.logger_save_alarm_reached("DISK", x)

for x in data["MEMORY"]:
    if MEMORY() >= int(x):
        print(f"ALARM! MEMORY value {x} has been reached")
        Logger.logger_save_alarm_reached("MEMORY", x)
