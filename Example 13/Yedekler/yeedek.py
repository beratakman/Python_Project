import random

def randomCharacters(numberOfCharacters, characterType): # Bir Fonksiyon Oluşturuyoruz ve İçine Verdiğimiz Fonksiyonlardan {([numberOfCharacters])} --> Kaç Karakterden Oluşucağını , {([characterType])} --> Hangi Tarzda Olucağını Seçer 
    character = ""
    characters = {0 : "ABCDEFGHIJKLMNOPRSTUVYZ" , 1 : "abcdefghijklmnoprstuvyz" , 2 : "!%!&?/?_-" , 3 : "0123456789" , 4 : "ABCDEFGHIJKLMNOPRSTUVYZabcdefghijklmnoprstuvyz!%!&?/?_-0123456789"} # 0 --> Büyük Harfler   \---/   1 --> Küçük Harfler   \---/   2 --> Semboller   \---/   3 --> Rakamlar   \---/   4 --> Şifre
    for z in range(numberOfCharacters):
            character = character + str(random.choice(characters[characterType]))
    return character
            

print(randomCharacters(5,0))