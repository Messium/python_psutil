from alarm import Alarms
from delete_alarm_json import Delete_alarm
from logger import Logger
from new_alarm import Alarm
# from monitor import Monitor
from new_monitor import Monitor
from monitor_check_json_values import Monitorize
from utils import Utils
from sys import platform

# Objekt av klass metoden pointer() från Utils klassen.
pointer = Utils.pointer()
welcome_message = Utils.welcome_message()
# monitor_start = Monitor.monitor_start()
# monitor_monitor_mode = Monitor.monitor_mode()
get_home_path = Utils.get_home_path()


if platform == "linux" or platform == "linux2":
    print("welcome linux user")
elif platform == "darwin":
    print("welcome mac user")
elif platform == "win32":
    print("welcome win user")


class Menu():

    # Eftersom klassens state eller objekt inte behövs ändras eller få tillgång
    # till klassattribut eller andra värden så har jag valt en staticmethod över en classmethod.

    options = {
        # str object made into method not possible unless ?
        # import foo
        # bar = getattr(foo, 'bar')
        # result = bar()
        # key_index: menu_option, method_call
        "1": ["Starta övervakning", "asdf"],
        "2": ["Lista aktiv övervakning", "asdf"],
        "3": ["Skapa larm", "asdf"],
        "4": ["Visa larm", "asdf"],
        "5": ["Starta övervakningsläge", "asdf"],
        "6": ["delete alarms", "Delete_alarm.menu_delete()"],
        "7": ["exit", ""]
    }

    @staticmethod
    def menu_startup():
        while True:
            try:

                print(pointer, welcome_message)

                for key, value in Menu.options.items():
                    print(pointer, key, value[0])

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
                    # Alarms.options_menu()
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
                    # Alarms.active_alarms()
                    # TODO:
                    Alarm.print_all()

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
                    # Monitor.monitor_mode()
                    # REVIEW:
                    Monitorize.monitor_mode()
                elif user_input == "6":
                    Delete_alarm.menu_delete()
                    # DONE:

                elif user_input == "exit" or user_input == "7":
                    break
                else:
                    print("bad input")
            except KeyboardInterrupt:
                break


Logger.logger()
Menu.menu_startup()
