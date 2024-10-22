import json
try:
    with open("alarms.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("no alarms.json")


# Diagnostics: "data" is possibly unbound [reportPossiblyUnboundVariable]

keys_list = list(data.keys())
for x, y in enumerate(keys_list):
    # print(f'\033[1;{x}H' + y)
    if "CPU" in y:
        print(x, y, data.get("CPU"))
    if "MEMORY" in y:
        print(x, y, data.get("MEMORY"))
    if "DISK" in y:
        print(x, y, data.get("DISK"))
# print('\033[2K') # delete current line
# print('\033[3J') # This clears the entire screen


    # TODO: use:
    # print('\033[1;1H' + x)
