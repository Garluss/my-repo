import random
setning = "Du tror du er den elendige fise-driten i sverige?"

ordb = ["fis","drit","sverige","elendig"]
erst = ["promp","bæsj","uviktig stat","dårlig"]
ordh = ["fisk","FIS"]
def char(len):
    set = ""
    for i in range(len):
        ran = random.randint(1,3)
        match ran:
            case 1: set = set + "#"
            case 2: set = set +"%"
            case 3: set = set + "&"
    return set

def sensur1(set):
    setr = set
    for i in range(len(ordb)):
        dex = setr.lower().find(ordb[i])
        if dex != -1:
            for x in range(len(ordh)):
                chk = setr.find(ordh[x])
                if chk == dex:
                    return set
                else:
                    continue
            setr = setr.lower().replace(ordb[i], char(len(ordb[i]))).capitalize()
    return setr

def sensur2(set):
    setr = set
    for i in range(len(ordb)):
        dex = setr.lower().find(ordb[i])
        if dex != -1:
            for x in range(len(ordh)):
                chk = setr.find(ordh[x])
                if chk == dex:
                    return set
                else:
                    continue
            setr = setr.lower().replace(ordb[i], erst[i]).capitalize()
    return setr

print(sensur2(setning))

