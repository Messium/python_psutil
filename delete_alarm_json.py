import json

from utils import Utils


json_data = Utils.read_alarms_json() # No reason to put this in the class 🤣

class Delete_alarm():
    keys = json_data.keys()

    @staticmethod
    def menu_delete():
            while True:
                try:
                    for key in Delete_alarm.keys:
                        print(Utils.pointer(), key)
                    user_input = input("Please input either number or name 1. CPU/2. MEMORY/3. DISK: ")
                    if user_input == "CPU" or user_input == "1":
                        # while loop select a list value.
                        # ADDING the keys might be surpless..
                        # KEY_MEM = "MEMORY"
                        # KEY_DISK = "DISK"
                        # KEY_CPU = "CPU"
                        # while True:
                        #     try:
                        print("please delete a value", json_data.get("CPU"))
                        user_input = input()
                        # TODO: could improve the handeling of a bad value this is a
                        # poor implementation
                        for x in json_data.get("CPU"):
                            if user_input == x:
                                delete_index = json_data.get("CPU").index(x)
                                json_data.get("CPU").pop(delete_index)
                                print("Alarm", x, "was deleted from CPU")
                                Delete_alarm.save_alarm_json()
                                break

                            if len(json_data.get("CPU")) == 0:
                                break
                            # except KeyboardInterrupt:
                            #     break

                    if user_input == "MEMORY" or user_input == "2":
                        while True:
                            try:
                                print("please delete a value", json_data.get("MEMORY"))
                                user_input = input()
                                # TODO: could improve the handeling of a bad value this is a
                                # poor implementation
                                for x in json_data.get("MEMORY"):
                                    if user_input == x:
                                        delete_index = json_data.get("MEMORY").index(x)
                                        json_data.get("MEMORY").pop(delete_index)
                                        print("Alarm", x, "was deleted from MEMORY")
                                        Delete_alarm.save_alarm_json()
                                        break

                                    if len(json_data.get("MEMORY")) == 0:
                                        break
                            except KeyboardInterrupt:
                                break

                    if user_input == "DISK" or user_input == "3":
                        while True:
                            try:
                                print("please delete a value", json_data.get("DISK"))
                                user_input = input()
                                # TODO: could improve the handeling of a bad value this is a
                                # poor implementation
                                for x in json_data.get("DISK"):
                                    if user_input == x:
                                        delete_index = json_data.get("DISK").index(x)
                                        json_data.get("DISK").pop(delete_index)
                                        print("Alarm", x, "was deleted from DISK")
                                        Delete_alarm.save_alarm_json()
                                        break


                                    if len(json_data.get("DISK")) == 0:
                                        break
                            except KeyboardInterrupt:
                                break

                except KeyboardInterrupt:
                    break


    @staticmethod
    def display_key_values():
        key_values = json_data.items()
        print(key_values)


    # overwrite the whole json file after an alarm is deleted
    @staticmethod
    def save_alarm_json():
        try:
            # json_file_name = "alarms.json"
            # json_file_name =
            with open(Utils.json_file_name(), mode="w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4)
        except FileNotFoundError:
            pass


# Delete_alarm.display_key_values()
# Delete_alarm.menu_delete()
