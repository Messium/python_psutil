import menu

monitor_started = []

def monitor_start():
    while True:
        options = [
            "cpuanvändning",
            "minnesanvändning",
            "diskanvändning",
        ]
        message = "Choose an option:"
        print(">", message)
        for num, item in enumerate(options, 1):
            print(">", str(num), str(item))
        user_input = input()
        if user_input == "1":
            print("cpuanvändning started")
            monitor_started.append("cpuanvändning")
        elif user_input == "2":
            print("minnesanvändning started")
            monitor_started.append("minnesanvändning")
        elif user_input == "3":
            print("diskanvändning started")
            monitor_started.append("diskanvändning")
        elif user_input == "exit":
            break
        elif user_input == "return":
            print("return to main menu")

def monitor_list_active():
    if monitor_started == "":
        print("no process started")
    else:
        print(monitor_started)

def monitor_monitorize():
    pass

monitor_start()
