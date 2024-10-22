import time
import json

import psutil
from menu import Menu
from utils import Utils

# Objekt av klass metoden pointer från Utils klassen.
pointer = Utils.pointer()

monitor_started = []


class Monitor:

    monitor = False
    update_freq = 1

    @classmethod
    def monitor_start(cls):
        # cls.monitor = Monitor.monitor
    # Startar övervakning av CPU användning, minnesanvändning och diskanvändning.
    # Notera alltså att ingen övervakning ska starta automatiskt vid programstart
        print("monitor started")
        Monitor.monitor = True
        return print(Monitor.monitor)

    @classmethod
    def monitor_mode(cls):
        # Listar aktiv övervakning som är aktiv samt nuvarande övervakningsstatus.
        # Har man inte startat övervakningen ska en text visas som informerar användaren om att ingen övervakning är aktiv. Annars visas övervakningen, t.ex:
        if Monitor.monitor is True:

            with open("alarms.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)
            # print('\033[1;1H' + time.asctime(time.localtime()))
            print('\033[1;1H' + data)
            time.sleep(1)  # update frequency TODO: make it a function for
            # configurability.
        else:
            print("please activate monitor first")
            # Menu.menu_startup()

    @classmethod
    def update_frequency(cls, input):
        pass
        update_freq = input


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
    print(psutil.virtual_memory()[2], "%")


# monitor_start()
# Monitor.monitor_start()
