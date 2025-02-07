import csv

# Les dataene fra CSV-filen
with open('05.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = list(reader)

# Hent startlokasjonene
# Opprett en tom liste for startlokasjonene
start_locations = []

# Gå gjennom hver rad i data
for row in data:
    # Hent ut startlokasjonen, som er det femte elementet i raden
    start_location = row[4]
    
    # Legg til startlokasjonen i listen
    start_locations.append(start_location)    

# Alternativt kan vi bruke list comprehension for å gjøre det samme
# start_locations = [row[4] for row in data] 

# Tell antall turer for hver startlokasjon
location_counts = {}
for location in start_locations:
    if location in location_counts:
        location_counts[location] += 1
    else:
        location_counts[location] = 1

# Sorter ordboken etter antall turer
sorted_locations = sorted(location_counts.items(), key=lambda item: item[1]) # item[1] er antall turer i ordboken

# Få de tre mest brukte startlokasjonene
top_three = sorted_locations[-3:]

# Få de tre minst brukte startlokasjonene
bottom_three = sorted_locations[:3]

# Presenter resultatene
print("De tre mest brukte startlokasjonene:")
for location, count in reversed(top_three):
    print(f"{location}: {count} turer")

print("\nDe tre minst brukte startlokasjonene:")
for location, count in bottom_three:
    print(f"{location}: {count} turer")