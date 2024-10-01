# setup alarms init

alarms = {}
alarms["minnesanvändning"] = []
alarms["cpuanvändning"] = []
alarms["diskanvändning"] = []

# setup alarms init end

def pointer():
    return "👉"

def alarm_create():
    while True:
        options = [
            "cpuanvändning",
            "minnesanvändning",
            "diskanvändning",
            "gå tillbaka till huvudmeny",
        ]

        message = "Create an alarm for:"
        print(message)
        for num, item in enumerate(options, 1):
            print(pointer(), str(num), str(item))


        user_input = input()

        if user_input == "1":
            print("start alarm för", options[0])
            print("desired %?")
            user_input = input()
            alarms[options[0]] = user_input
        elif user_input == "2":
            # print("start alarm för", options[1])
            # print("desired %?")
            user_input = input()
            ## REVIEW:
            try:
                val = int(user_input)
            except ValueError:
                print("That's not an int!")
            if user_input in alarms["minnesanvändning"]:
                print("already activated")
                continue
            if int(user_input) > 100:
                print("please choose a number between 1-100")
                continue
            if int(user_input) <= 0:
                print("please choose a number between 1-100")
            else:
                alarms["minnesanvändning"].append(user_input)
            print("activated:", alarms["minnesanvändning"])
            # if not alarms["minnesanvändning"]:
            #     print("empty list")

            # if "minnesanvändning" in alarms.keys():
            #     print(alarms["minnesanvändning"])
            #
            #     for x in alarms["minnesanvändning"]:
            #         if x == user_input:
            #             print("value already added")
            #         else:
            #             alarms["minnesanvändning"].append(user_input)
            # 1. check for existing alarm if yes append to a list in the
            # dictionary key named "minnesanvändning".
            # alarms[options[1]] = [user_input]
        elif user_input == "3":
            print("start alarm för", options[2])
            print("desired %?")
            user_input = input()
            alarms[options[2]] = user_input
        elif user_input == "4":
            print("start alarm för", options[3])
        else:
            print("do something else")
            # return to main meny

def alarm_remove():
    pass

def alarm_list_active():
    for monitor_category_name, value in alarms.items():
        print(monitor_category_name, value)

    pass

alarm_create()
