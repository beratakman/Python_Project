
import random
    
while True:
    value = (int(input("Lütfen 1 ile 10 arasında bir sayı giriniz:")))
    i = random.randint(1,10)
    if value == i:
        print("Tebrikler 1 milyon TL'nin sahbi siz oldunuz")
        break
    else:
        print(f"Malesef kaznamadınız eğer girdiğiniz sayı {i} olsaydı 1 milyon TL'nin sahibi olurdunuz ")

# while True:
#     value = (int(input("Lütfen 1 ile 1000 arasında bir sayı giriniz:"))) 
#     for abc in range(100):
#         x = random.randint(1,1000)
#         if value == x:
#             print("Tebrikler 1 milyon TL'nin sahbi siz oldunuz")
#             break
#     if value == x:
#         break
#     else:
#         print("Malesef kaznamadınız eğer girdiğiniz sayı olsaydı 1 milyon TL'nin sahibi olurdunuz ")
        