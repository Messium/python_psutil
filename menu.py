import os
from delete_alarm_json import Delete_alarm
from logger import Logger
from new_alarm import Alarm
from new_monitor import Monitor
from utils import Utils
from ansi import Ansi

class Menu():

    options = {
        "1": ["Starta övervakning"],
        "2": ["Lista aktiv övervakning"],
        "3": ["Skapa larm"],
        "4": ["Visa larm"],
        "5": ["Starta övervakningsläge"],
        "6": ["delete alarms"],
        "7": ["exit"]
    }

    @staticmethod
    def menu_startup():
        while True:
            try:

                print(Utils.pointer(), Utils.welcome_message())

                for key, value in Menu.options.items():
                    menu_print = f"{Utils.pointer()} {Ansi.RED} {key} {Ansi.END} {value[0]}"
                    print(menu_print)

                user_input = input()

                if user_input == "1":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │          Startar övervakning av CPU användning,          │
                    #          │    minnesanvändning och diskanvändning. Notera alltså    │
                    #          │     att ingen övervakning ska starta automatiskt vid     │
                    #          │                      programstart.                       │
                    #          ╰──────────────────────────────────────────────────────────╯
                    # DONE:
                    Monitor.monitor_start()


                elif user_input == "2":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │   Listar aktiv övervakning som är aktiv samt nuvarande   │
                    #          │         övervakningsstatus. Har man inte startat         │
                    #          │      övervakningen ska en text visas som informerar      │
                    #          │   användaren om att ingen övervakning är aktiv. Annars   │
                    #          │      visas övervakningen, t.ex: CPU Anvädning: 35%       │
                    #          │     Minnesanvändning: 65% (4.2 GB out of 8 GB used)      │
                    #          │  Diskanvändning: 80% (400 GB out of 500 GB used) Efter   │
                    #          │    detta promtas användaren om att bekräfta genom att    │
                    #          │      trycka enter. Tryck valfri tangent för att gå       │
                    #          │      tillbaka till huvudmeny Efter detta visas åter      │
                    #          │                huvudmenyn för användaren.                │
                    #          ╰──────────────────────────────────────────────────────────╯
                    # DONE:
                    Alarm.active_alarms()


                elif user_input == "3":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │   Väljer man detta alternativ får man upp ytterligare    │
                    #          │   en meny där man får välja att konfigurera larm inom    │
                    #          │      tre områden eller gå tillbaka till huvudmenyn.      │
                    #          │          Konfigurera larm 1. CPU användning 2.           │
                    #          │   Minnesanvändning 3. Diskanvändning 4. Tillbaka till    │
                    #          │   huvudmeny Efter att man valt ett alternativ får man    │
                    #          │   välja en procentuell nivå där larmet ska aktiveras.    │
                    #          │    T.ex. Ställ in nivå för alarm mellan 0-100. Efter     │
                    #          │        att användaren har valt en nivå skrivs en         │
                    #          │  bekräftelse ut, sedan visas huvudmenyn igen. Larm för   │
                    #          │   CPU användning satt till 80%.  Nivån måste matas in    │
                    #          │   som en siffra mellan 1-100 och matas nonsens in ska    │
                    #          │             användaren få ett felmeddelande.             │
                    #          ╰──────────────────────────────────────────────────────────╯
                    # REVIEW:
                    Alarm.alarm_menu()

                elif user_input == "4":
                    #          ╭──────────────────────────────────────────────────────────╮
                    #          │     Listar alla configurerade larm. Larmen ska vara      │
                    #          │   sorterade på typ när de visas. Exempel: 1. CPU larm    │
                    #          │ 70% 2. Disklarm 95% 3. Minneslarm 80% 4. Minneslarm 90%  │
                    #          │   Efter detta promtas användaren om att bekräfta genom   │
                    #          │    att trycka enter. Tryck valfri tangent för att gå     │
                    #          │   tillbaka till huvudmeny Notera att man kan ha flera    │
                    #          │                    larm av samma typ.                    │
                    #          ╰──────────────────────────────────────────────────────────╯
                    # DONE:
                    Alarm.sorted_list()


                elif user_input == "5":
                    #       ╭────────────────────────────────────────────────────────────────╮
                    #       │                 Startar ett övervakningsläge.                  │
                    #       │ Användaren blir promtad om att övervakningsläget har startats, │
                    #       │    sedan loopar en sträng med jämna mellanrum som meddelar     │
                    #       │                           användaren                           │
                    #       │     att övervakningen är aktiv samt att man kan trycka på      │
                    #       │                          valfri knapp                          │
                    #       │                för att återgå till huvudmenyn.                 │
                    #       ╰────────────────────────────────────────────────────────────────╯
                    # REVIEW:
                    Monitor.monitor_mode()
                elif user_input == "6":
                    Delete_alarm.menu_delete()
                    # DONE:

                elif user_input == "exit" or user_input == "7":
                    break
                else:
                    os.system('clear')
                    print("Please choose an numbered option between 1-7")
            except KeyboardInterrupt:
                break


Logger.logger()
json_data = Utils.read_alarms_json()
Menu.menu_startup()
