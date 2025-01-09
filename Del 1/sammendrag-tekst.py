#Bruk camelcase
rektangelAreal = 2
rektangelLengde = 1
rektangelBredde = 1

#For konstanter, caps
LYSETS_HASTIGHET = "eg vet ikke hva lysets hastighet er"

sitat = "Wisdom comes from experience. Experience is often a result of lack of wisdom."
antallTegn = len(sitat)

sitat[x:y]  # gir oss tegnene fra og med indeks x til, men ikke med, indeks y
sitat[x:]   # gir oss alle tegnene fra og med x
sitat[:y]   # gir oss alle tegnene fram til, men ikke med, y
sitat[-4:]  # gir oss de fire siste tegnene (- gjør at vi teller bakfra)

input = input("Input: ").lower().strip()

string = "Hallo"
flot = 56.234
print(f"Vel, vel, vel. {flot:.2f}, {string}")

# 42	{verdi}	42	Skriver ut verdien uten formatering.
# 42	{verdi:8}	42	Seks mellomrom legges til foran tallet slik at verdien bruker åtte tegn.
# 3.14	{verdi}	3.14	Skriver ut verdien uten formatering.
# 3.14	{verdi:.1f}	3.1	Tallet skrives ut med én desimal.
# 3.14	{verdi:6.1f}	3.1	Punktumet teller som ett tegn. Vi får derfor tre mellomrom foran tallet.
# "Hei"	{verdi}	Hei	Skriver ut verdien uten formatering.
# "Hei"	{verdi:8}	Hei	Fem mellomrom legges til etter teksten.
# "Hei"	{verdi:<8}	Hei	Ved å bruke < blir teksten venstrejustert (mellomrom legges til etter teksten).
# "Hei"	{verdi:>8}	Hei	Ved å bruke > blir teksten høyrejustert (mellomrom legges til foran teksten).

print("Hei ", end="")
print("på deg!")