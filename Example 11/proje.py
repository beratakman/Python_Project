# nameSurname = input("Adınızı Giriniz: ")
nameSurname = "Berat Akman"
number = 0
nameSurname0 = "".join(reversed(nameSurname))

print(reversed(nameSurname))
for letter in nameSurname:
    print(letter)
    number += 1
    print("\n")
    print(" " * number)
number -=1
for letter0 in nameSurname0:
    print(letter0,end="")
    number -= 1
    print("\n",end="")
    print(" " * number,end="")