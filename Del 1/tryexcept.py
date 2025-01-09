gyldig = False

while not gyldig:
    try:
        tall = input("Skriv et tall ")
    except KeyboardInterrupt:
        print("")
        print("Sluttet program via Ctrl-C eller Delete.")
        print("")
        exit()

    try:
        tall = int(tall)
        if tall < 0:
            print("Tallet må være positivt.")
        else:
            gyldig = True
    except ValueError:
        print("Du må skrive inn et heltall.")
print(f"Du skrev inn {tall}.")