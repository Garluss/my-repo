def klassifisering(h,v):
    bmi = round(v/(h**2),1)
    if bmi < 18.5: return "Undervektig"
    elif 18.5 < bmi < 25.0: return "Normalvektig"
    elif 25.0 < bmi < 30.0: return "Overvektig"
    elif 30.0 < bmi < 35.0: return "Fedme, grad 1"
    elif 35.0 < bmi < 40.0: return "Fedme, grad 2"
    elif bmi > 40.0: return "Fedme, grad 3"