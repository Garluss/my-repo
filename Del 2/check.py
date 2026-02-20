import csv

new = []
with open("glos.txt",encoding="utf-8",mode="r") as fil:
    data = csv.reader(fil,delimiter="-")
    for i in data:
        new.append(i[1].strip() + " - " + i[0].strip())
    
with open("glos2.txt",encoding="utf-8",mode="w") as fil:
    data_to_write = '\n'.join(new)
    fil.write(data_to_write)