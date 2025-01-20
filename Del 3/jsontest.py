import json
file = "land.json"


with open(file, encoding="utf-8") as content:
    dict = json.load(content)

print(f"Current region: {dict["region"]}")

def load_country():
    while True:
        c = input("Country: ")
        if c == "back":
            return "canceled"
        for i in dict["land"]:
            if c == i["navn"]:
                return i
# add_dict = {}
# def add(path, current=None):
#     add_dict = path
#     while True:
#         if current == None:
#             add = input("Add 'key', 'list', or 'dict': ")
#             match add:
#                 case "key":
#                     name = input("Name the key: ")
#                     add_dict[name] = None
#                     current = "key"
#         elif current == "key":
#             add = input("Insert into the key a 'list' or 'dict': ")
#             match add:
#                 case "list":
#                     current = "list"
#         elif current == "list":
#             add_dict[name] = []
#             cmd = input("Append or complete ('back'): ")
#             match cmd:
#                 case "append":
#                     add = input("Value to append")

topic = None
while True:
    if topic == None:
        cmd = input(f"{topic} » ")
        match cmd:
            case "c": 
                answ = load_country()
                if answ != "canceled":
                    topic = "Country"
            case "quit":
                break
            case _: print("Unknown command. Try 'c' or 'quit'.")
        print("")
    elif topic == "Country":
        print(f"Name: {answ["navn"]}")
        print(f"Currency: {answ["valuta"]}")
        print(f"Cities: {answ["byer"]}")
        cmd = input(f"{topic} » ")
        match cmd:
            case "full": print(answ)
            # case "add":
            #     ret = add(answ)
            case "back": topic = None
            case _: print("Unknown command. Try 'full' or 'back'.")
        print("")
