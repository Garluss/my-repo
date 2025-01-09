tabell = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"]
]

print(tabell[2][1])


# Dele opp lister
# Vi kan hente ut eller redigere deler av lister ved å bruke det som kalles «slices». Da kan vi angi en start- og en sluttindeks for den delen av lista vi ønsker å jobbe med. Generelt skriver vi

# liste[startindeks:sluttindeks]
# liste[startindeks:sluttindeks]
# Da henter vi ut verdiene fra og med startindeks til, men ikke med, sluttindeks.

# Hvis vi bare oppgir startindeks, hentes alle verdier fra og med startindeksen:

# liste[startindeks:]
# liste[startindeks:]
# Hvis vi bare oppgir sluttindeks, hentes alle verdier til, men ikke med, sluttindeksen:

# liste[:sluttindeks]
# liste[:sluttindeks]

# Sortere lister
# For å sortere en liste kan vi bruke sort():
tall = [1, 5, 3, 4, 7, 2, 6]
tall.sort()
tall = [1, 5, 3, 4, 7, 2, 6]
tall.sort()

# Vi kan også sortere en liste i omvendt rekkefølge:
tall = [1, 5, 3, 4, 7, 2, 6]
tall.sort(reverse=True)
tall = [1, 5, 3, 4, 7, 2, 6]
tall.sort(reverse=True)

# Hvis vi bare ønsker å snu rekkefølgen på verdiene i en liste, kan vi bruke reverse():
tall = [1, 5, 3, 4, 7, 2, 6]
tall.reverse()