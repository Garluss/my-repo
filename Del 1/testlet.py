maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"
maaned = int(input())

if maaned >= 13 or maaned <= 0:
    print("Denne måneden eksisterer ikke.")
else:
    print(maaneder[maaned*3-3:maaned*3])