liczby = [2, 10, 12, 15, 20, 25, 30, 35]

# Map applies a function to all the items in an input_list

def funkcja(x):
    return x * 2

wynik = map(funkcja, liczby)
print(list(wynik))

wynik2 = map(lambda x: x+2, liczby)
print(f"Lista 2 : {list(wynik2)}")

# Filters returns True or False for each element in the input_list

wynik3  = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik3))