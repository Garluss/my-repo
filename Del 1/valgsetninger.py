
import time


print("Hallo, hallo, hallo.")
time.sleep(1)
print("Jeg trenger å vite alderen din slik at du får riktig billett.")
time.sleep(3)

alder = int(input("Hva er alderen din, kompis? "))

print("")
print(f"Jeg: Alderen min er {alder} år.")
print("")

if alder < 0:
    print("Jeg tror ikke på det kompis. Ingen tull er akseptert ved denne billettstasjonen, ha deg vekk.")
elif alder > 6 and alder <= 15:
    print("Her har du en barnebillett. Kos deg.")
elif alder > 0 and alder < 7:
    print("Her har du en babybillett, lille baby.")
elif alder > 15 and alder < 24:
    print("Er du student?")
    svar = input("J / N ")
    if svar.lower() == "j":
        print("Her har du en studentbillett. Kos deg.")
    elif svar.lower() == "n":
        print("Vær så god, en voksenbillett.")
    else:
        print("Ingen tull akseptert, kom deg ut.")
elif alder > 120:
    print("Jeg tror ikke det, kompis. Du ser ikke så gammel ut.")
else:
    print("Her, en god og fin voksenbillett. Kos deg.")
