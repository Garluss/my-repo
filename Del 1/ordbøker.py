person = {
    "fornavn": "Per",
    "etternavn": "Christensen"
}

#Hente verdi av nøkkel
print(person["fornavn"])

#Endre verdi av nøkkel
person["fornavn"] = "Jallamann"
print(person["fornavn"])

#Skriver ut hele ordboken
print(person)

#Fjerner nøkkelen og verdien
person.pop("fornavn")

#Søker i 'person' etter nøkkelen 'fornavn' og deretter sletter den og dens verdi
if "fornavn" in person:
  person.pop("fornavn")

#Printer ut alle nøkler med sine verdier
for x in person:
  print(x)
  print(person[x])

for noekkel, verdi in person.items():
  print(noekkel, verdi)

#Samling av ordbøker, noen ordbøker i ordbøker
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

print(type(sommer_ol))

#Printer ut årstall med vinnerverdi på 100 m
for ol in sommer_ol:
  aar = ol["årstall"]

  vinnertid_100m = ol["vinnertider"]["100 m"] #Dette henter ordboken fra alle ordbøkene 'vinnertider' fra listen 'sommer_ol', og deretter verdien fra '100 m'
  print(f"I {aar} var vinnertiden på 100 m: {vinnertid_100m}.")