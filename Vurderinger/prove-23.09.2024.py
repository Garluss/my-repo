import random

print("Skriv setningen din:")
#setning = input()
setning = "Jeg elsker FIS"

styggeord = ["FIS","DRIT","TISS","RÆV","SVERIGE"]

def sensur1(set):
    set = set.upper()
    set = set.replace("FIS","fis")
    set = set.replace("FISK","fisk")
    for i in range(len(styggeord)):
        set = set.replace(styggeord[i], "#"*len(styggeord[i]))
    set = set.lower()
    set = set.replace("fis", "FIS")
    return set
    

def sensur2(set):
    set = set.upper()
    set = set.replace("FISK","fisk")
    set = set.replace("FIS","promp")
    set = set.replace("DRIT","bæsj")
    set = set.replace("TISS","reproduksjonsorgan")
    set = set.replace("RÆV","rumpe")
    set = set.replace("SVERIGE","uviktig stat")
    return set.lower()

print(sensur1(setning))
