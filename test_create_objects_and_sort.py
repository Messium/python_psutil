from utils import Utils
from new_alarm import Alarm

json_data = Utils.read_alarms_json()

alarm_list = []

for key in json_data.keys():
    for value in json_data.get(key):
        alarm_list.append(Alarm(value, key))


# old implementation DISCARDED:
# for x in json_data.get("CPU"):
#     alarm_list.append(Alarm(x, "CPU"))
#
# for x in json_data.get("DISK"):
#     alarm_list.append(Alarm(x, "DISK"))
#
# for x in json_data.get("MEMORY"):
#     alarm_list.append(Alarm(x, "MEMORY"))
#
for item in alarm_list:
    print(item)

new_list = sorted(alarm_list, key=lambda alarm: (alarm.alarm_type, alarm.alarm_level))
#  It looks like you are trying to sort a list of `Alarm` objects based on both their `alarm_type` and `alarm_level` attributes. However, in your lambda function for `key`, you are only providing one argument which is an instance of the `Alarm` class.
#
# To make it work with multiple attributes, you should use a tuple as the value of the `key` parameter:
#
# ```python
# new_list = sorted(alarm_list, key=lambda alarm: (alarm.alarm_type, alarm.alarm_level))


for item in new_list:
    print(item)
# TODO: use sorted instead
# sorted_alarms = sorted(alarms, key=lambda alarm: alarm.alarm_level, alarm.alarm_type)
#
# print(sorted_alarms)
