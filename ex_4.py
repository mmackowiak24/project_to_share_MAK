# Zaokraglij do dwoch miejsc po przecinku

def oblicz_potega(liczba, potega) -> float:
    oblicz_potega = pow(liczba, potega)
    result = round(oblicz_potega, 2)
    return result
