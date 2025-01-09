#Brukere lagret som en ordbok
brukere =  {
    "admin" : "1234",
    "per12" : "likerjobb45",
    "marie_årstad" : "2015"
}


forsøk = True
while forsøk == True:
    bruker = input("Skriv inn brukernavn: ").lower().strip()
    #Sjekker om bruker eksisterer
    if bruker in brukere.keys():
        tall = 2
        while True:
            passord = input("Skriv inn passord: ").strip()
            if passord == brukere.get(bruker):
                print("Innlogging fullført!")
                admin = True
                forsøk = False
                break
            else:
                if tall == 0:
                    print("Innlogging stengt.")
                    forsøk = False
                    break
                else:
                    print("Feil passord! Prøv på nytt!")
                    print(f"Du har {tall} forsøk igjen.")
                    tall = tall - 1
    else:
        print("Brukeren eksisterer ikke!")

#Starten på et konsept
# if admin == True:
#     print("Du er logget inn som administrator.")
#     print("Her kan du skape eller fjerne kontoer")