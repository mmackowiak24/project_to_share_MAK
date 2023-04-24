# dla podanych dwoch punktow, oblicz, czy funkcja liniowa jest rozsnaca, czy malejaca
# dla niemalejacej zrwoc True
# dla malejacej zwroc False
def funkcja_liniowa(punkty) -> bool:
    x1, y1 = punkty[0]
    x2, y2 = punkty[1]
    if(y1 < y2):
        return True
    else:
        return False