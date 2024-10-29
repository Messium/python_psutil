list_1 = ["asdf", "afsada"]

with open("save_text.txt", mode="w", encoding="utf-8") as f:
    save = str(list_1)
    f.write(save)

with open("save_text.txt", mode="r") as f:
    opened_file = f.read()
    # print(opened_file)
    test = opened_file.split(", ")
    print(test)
