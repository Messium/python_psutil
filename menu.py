from alarm import Alarms
from logger import Logger
from monitor import Monitor # surpless
from utils import Utils

# Objekt av klass metoden pointer() från Utils klassen.
pointer = Utils.pointer()
# monitor_start = Monitor.monitor_start()
monitor_monitor_mode = Monitor.monitor_mode()
get_home_path = Utils.get_home_path()


class Menu():

    # Eftersom klassens state eller objekt inte behövs ändras eller få tillgång
    # till klassattribut eller andra värden så har jag valt en staticmethod över en classmethod.

    @staticmethod
    def menu_startup():
        while True:

            options = [
                "Starta övervakning",
                "Lista aktiv övervakning",
                "Skapa larm",
                "Visa larm",
                "Starta övervakningsläge",
                "clear alarms",
                "delete alarms",
            ]

            # actions = [
            #     "Monitor.monitor_start()",
            #     "Alarms.active_alarms()",
            #     "Alarms.options_menu()",
            #     "Alarms.active_alarms()",
            #     "Monitor.monitor_mode()",
            # ]

            welcome_message = "Hello and welcome choose an option:"
            print(pointer, welcome_message)
            for num, item in enumerate(options, 1):
                print(pointer, str(num), str(item))

            user_input = input()

            if user_input == "1":
                #          ╭──────────────────────────────────────────────────────────╮
                #          │          Startar övervakning av CPU användning,          │
                #          │    minnesanvändning och diskanvändning. Notera alltså    │
                #          │     att ingen övervakning ska starta automatiskt vid     │
                #          │                      programstart.                       │
                #          ╰──────────────────────────────────────────────────────────╯
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
                Alarms.active_alarms()

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
                Alarms.options_menu()

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
                Alarms.active_alarms()

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
                Monitor.monitor_mode()

            elif user_input == "6":
                Alarms.clear_alarm()

            elif user_input == "7":
                Alarms.delete_alarm()

            elif user_input == "exit":
                break
            else:
                print("bad input")


logger_instance = Logger.logger()
menu_instance = Menu.menu_startup()
