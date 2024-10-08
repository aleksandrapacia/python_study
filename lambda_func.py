# lambda inside a function
def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x, 5))

# lambda outside of a function
def kwadrat(x):
    return x*x

funkcja_lambda = (lambda x: x * x)(5)
print(funkcja_lambda)

lam = lambda x: x*x
print(lam(3))

# more arguments
lam2 = lambda x, y : x * y
print(lam2(2,3))