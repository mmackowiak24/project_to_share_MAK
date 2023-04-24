# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]


def wykres(coordinates) -> bool:
    if len(coordinates) < 3:
        return True #z dwóch punktów można utworzyć funkcję liniową
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (y2 - y1 ) / (x2 - x1) if x2 != x1 else float('inf')

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        new_slope = (y - y1) / (x - x1) if x != x1 else float('inf')
        if abs(new_slope - slope ) >= 1e-9:
            return False
    return True

print(wykres(wykres_1))
print(wykres(wykres_2))
print(wykres(wykres_3))
