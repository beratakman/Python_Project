def factorialCalculation(x):
    number = 0
    a = 1
    for factorial in range(x):
        number += 1
        factorial0 = a * number
        a = factorial0
        factorial = factorial0
    return factorial
        
print(factorialCalculation(5))