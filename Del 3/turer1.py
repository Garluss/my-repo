'''
Oppgave 1
Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst 
brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.
Del 1 bruker Pandas.
Del 2 bruker Python-dictionary.
'''

import pandas as pd

# Last inn dataene fra CSV-filen
df = pd.read_csv('05.csv')

# Grupper dataene etter startlokasjon og tell antall turer for hver startlokasjon
location_counts = df['start_station_name'].value_counts()

# Få de tre mest brukte startlokasjonene
top_three = location_counts.nlargest(3)

# Få de tre minst brukte startlokasjonene
bottom_three = location_counts.nsmallest(3)

# Presenter resultatene
print("De tre mest brukte startlokasjonene:")
for location, count in top_three.items():
    print(f"{location}: {count} turer")

print("\nDe tre minst brukte startlokasjonene:")
for location, count in bottom_three.items():
    print(f"{location}: {count} turer")