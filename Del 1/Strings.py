# +	Pluss	a + b
# -	Minus	a - b
# *	Gange	a * b
# /	Dele	a / b
# **	Eksponent	a**b
# %	Modulus (rest ved divisjon)	17 % 5 (gir 2)
# //	Heltallsdivisjon	17 // 5 (gir 3)

sitat = "Wisdom comes from experience. Experience is often a result of lack of wisdom.";

antallTegn = len(sitat) #lengde på sitatet

x=5
y=15
sitat[x:y]  # gir oss tegnene fra og med indeks x til, men ikke med, indeks y
sitat[x:]   # gir oss alle tegnene fra og med x
sitat[:y]   # gir oss alle tegnene fram til, men ikke med, y
sitat[-4:]  # gir oss de fire siste tegnene (- gjør at vi teller bakfra)

print("Sitatets lengde:", len(sitat))
print("Tegnet med indeks 26:", sitat[26])
print("Tegnene til og med indeks 11:", sitat[:12])
print("Tegnene fra og med indeks 28:", sitat[28:])
print("Tegnene med indeks 16 til 25:", sitat[16:26])


# Tekst                              	Metode               	Resultat               	Beskrivelse               
# tekst = "Hei pÅ DEG!"	tekst.lower()	        "hei på deg!"	     Gir små bokstaver
# tekst = "Hei pÅ DEG!"	tekst.upper()	        "HEI PÅ DEG!"   Gir store bokstaver
# tekst = "nils jensen"	     tekst.capitalize()	    "Nils jensen"	     Første bokstav blir stor
# tekst = "nils jensen"	     tekst.title()	            "Nils Jensen"	    Første bokstav i hvert ord blir stor
# tekst = "3,14"	            tekst.replace(",", ".")	"3.14"               Lar oss erstatte tegn/ord i en tekst med andre tegn/ord
# tekst = "Hei på deg!"	   tekst.index("p")	            4	                Gir indeksen til første forekomst av teksten vi oppgir
# tekst = "Hei på deg!"	   len(tekst)	                    11	                Antall tegn i teksten

ord = "spiser"
lengde = len(ord)
nyttOrd = ord[2] + ord[lengde - 3]
print(nyttOrd)





# Tekster i tekster
# Noen ganger ønsker vi å bruke anførselstegn i en tekst.

# Vi kan løse det ved å bruke apostrofer i stedet for anførselstegn rundt teksten:

# print('Han sa: "Hei"')
# print('Han sa: "Hei"')
# Eller vi kan sette inn skråstrek foran anførselstegnene:

# print("Han sa: \"Hei\"")
# print("Han sa: \"Hei\"")
# Skråstrekene forteller Python at tegnene som kommer, ikke skal tolkes. Vi kaller \ en «escape character».


#Juster desimaler med:
#{areal:.2f}


import math as m

radius1 = 8
areal1 = m.pi*radius1**2

radius2 = 72.3
areal2 = m.pi*radius2**2

print(f"Arealet av en sirkel med radius {radius1} er {areal1:.2f}.")
print(f"Arealet av en sirkel med radius {radius2} er {areal2:.2f}.")


# Verdi	Formatering	Resultat	Kommentar
# 42	{verdi}	           42	            Skriver ut verdien uten formatering.
# 42	{verdi:8}	42   Seks mellomrom legges til foran tallet slik at verdien bruker åtte tegn.
# 3.14	{verdi}	          3.14	          Skriver ut verdien uten formatering.
# 3.14	{verdi:.1f}	    3.1	              Tallet skrives ut med én desimal.
# 3.14	{verdi:6.1f}  3.1	   Punktumet teller som ett tegn. Vi får derfor tre mellomrom foran tallet.
# "Hei"	{verdi}	       Hei	              Skriver ut verdien uten formatering.
# "Hei"	{verdi:8}	  Hei	Fem mellomrom legges til etter teksten.
# "Hei"	{verdi:<8}	 Hei	Ved å bruke < blir teksten venstrejustert (mellomrom legges til etter teksten).
# "Hei"	{verdi:>8}	 Hei	Ved å bruke > blir teksten høyrejustert (mellomrom legges til foran teksten).


print("01", end=" | ")
print("02", end=" | ")
print("03")