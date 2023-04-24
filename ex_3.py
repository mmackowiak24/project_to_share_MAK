# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci) -> [int, int]:
    m = 0
    k = 0
    for student in studenci:
       
        if student.split(" ")[0].lower().endswith('a'):
            k += 1
            print( student)
        else:
            m +=1  
            print( student)  
    return [k, m]
        
        
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
wynik= policz_studentow_plec(studenci)
print (wynik)
