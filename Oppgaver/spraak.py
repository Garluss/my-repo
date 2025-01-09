import json

def storeWord(wordn,wordai,wordtype="substantiv"):
    with open('output.json') as f:
        x = json.load(f)
        print(x)
        wordn = wordn.lower()
        wordai = wordai.lower()
        wordtype = wordtype.lower()
        x.update({"Norsk":wordn,"Ai-Fel":wordai,"Ordtype":wordtype})
        with open('output.json','w') as l:
            json.dump(x, l, indent=4)

storeWord("test","testum","substantiv")