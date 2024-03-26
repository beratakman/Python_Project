def factorialCalculation(x):
    factorial = 1
    for count in range(1, x+1):
        factorial = factorial * count
    return factorial

print(factorialCalculation(int(input("Lütfen Faktöriyelini Hesaplamak İstediğiniz Sayıyı Giriniz: "))))
