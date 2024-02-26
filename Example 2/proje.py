
#bütün harfleri büyük yazan fonksiyon

def allUpper(value):
    return str(value).replace("i","İ").upper()

print(allUpper("I ı İ i"))

##############################################################################################################################################################################

#bütün harfleri küçük yazan fonksiyon

def allLower(value):
    return str(value).replace("I","ı").lower()

print(allLower("İ i I ı"))

##############################################################################################################################################################################

#ilk harfleri büyük yazan fonksiyon
def bTitle(text): #title fonksiyonu düzelten kod
    newtext = ""
    for word in str(text).split(" "):
        newStr = "" #her döngüde kelimeyi sıfırlıyoruz
        countChar = 0 #her döngüde karakter sayasıcını sıfıra eşitledim
        for char in word:
            countChar = countChar + 1 #karakterleri sayarken sayacı bir bir artırıyorum
            if (countChar == 1): #bu durumda sayaç 1 eşit ise ilk karakter demektir. 
                if (char == "i"): #ilk karakter büyük İ varsa aptal yazılım bunu küçük i ye çevirdiği için biz kartakteri manuel olarak büyük i yapacağız
                    char = "İ" #büyük İ yapıyroruz
            else: #değilse diğer karakterlerdir
                if (char == "I"): #diğer karakter küçük harf olacağı için bu sefrde büyük I karakterini küçük ı karakterine çeviriyouz
                    char = "ı" #küçük ı yapıyrouz
            newStr = newStr + char #sonra her karateri tek tek değişkene atıyrouz
        newtext = newtext + " " + newStr.capitalize() # değişkene atadığımız karakterleri aralarında boşluk oalcak şekilde yeni değişkene atıryouz
    return newtext.strip() #yukarıda karakter atmasında ortaya çıkan ilk karakter boşluğu siplit vasıtası ile temizliyoruz

#name = (str(input("Lütfen İsminizi ve Soyisminizi Giriniz:")))
print(bTitle("ismaİl baki ırmak yusuf Kamil PINAR"))


# değişkende olmaaycaklar
# türkçe karakter --> İığĞüÜöÖçÇşŞ  ---> yanlış-> örnek         |  dogru: ornek
# işaretlre .,-?&()                 ---> yanlış-> name,surname  |  dogru: nameSurname
# ilk karakter sayı ile başlayamaz  ---> yanlış-> 3name         |  dogru: name3
