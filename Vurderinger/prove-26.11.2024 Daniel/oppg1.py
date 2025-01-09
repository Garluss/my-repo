print("BMI-kalkulator")
def kalkuler_bmi(h, v):
    return v/(h/100)**2

while True:
    try:
        h_cm = input("Høyde (cm): ")
        if h_cm == "":
            break
        v_kg = float(input("Vekt (kg): "))
        res = round(kalkuler_bmi(float(h_cm),v_kg),1)
        t = ""
        if res <= 18.4:
            t = "undervektig"
        elif res >= 18.5 and res <= 24.9:
            t = "normalvektig"
        elif res >= 25:
            t = "overvektig"
        print(f"BMI: {res} ({t})")
    except ValueError:
        print("Sett inn kun tall!")
    except ZeroDivisionError:
        print("Høyde kan ikke være null!")
    print("")

print("Takk for nå.")