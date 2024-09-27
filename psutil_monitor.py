import psutil
import os
import textual

# HOME PATH

path = "$HOME"
# gets user $HOME director
def get_home_directory_with_expanduser():
     return os.path.expanduser("~")
home_dir = get_home_directory_with_expanduser()
print(home_dir)

# END HOME PATH

def get_cpu_percent():
    print(psutil.cpu_percent(1))

def get_disk_usage():
    return psutil.disk_usage(home_dir)
    # index 3 print % of total usage (see docs below).
    # return class: <class 'psutil._common.sdiskusage'>
    # see docs: https://psutil.readthedocs.io/en/latest/#disks
    # "Return disk usage statistics about the partition
    # which contains the given path as a named tuple
    # including total, used and free space expressed in
    # bytes, plus the percentage usage."

# surplus...
#
# def get_disk_total():
#     print(get_disk_usage()[1])
# get_disk_total()
#
#
# def get_disk_free():
#     print(get_disk_usage()[2])
# get_disk_free()
#
#
# def get_disk_percentage():
#     print(get_disk_usage()[3])
# get_disk_percentage()

# tuple with index 1 return total size in bytes.
# tuple with index 2 return total free.
# tuple with index 3 return %.


# TODO:
# disk_usage % 🏁
# cpu_percent

# END welcome message

# User input in terminal:


# value = survey.routines.input('ping? ')
# print(f'Answered {value}.')

# standard library version:
# user_input = "disk_usage"

# welcome message

print("welcome to the pymonitor program, please choose an option")
opts = ["cpu_percent", "disk_usage"]
print(opts)
user_input = input()
if user_input == "cpu_percent":
    get_cpu_percent()
elif user_input == "disk_usage":
    disk_usage_params = input("välj ett alternativ 1. total, 2. used or 3. free")
    if disk_usage_params == "total":
        print(get_disk_usage()[1])
    elif disk_usage_params == "used":
        print(get_disk_usage()[2])
    elif disk_usage_params == "free":
        print(get_disk_usage()[3])
    else:
        print("felaktig error försök igen")
    # # Conversion to kilobytes, megabytes, and gigabytes
    # file_size_kb = get_disk_usage()[1] / 1024
    # file_size_mb = file_size_kb / 1024
    # file_size_gb = file_size_mb / 1024
    # print(file_size_mb)
