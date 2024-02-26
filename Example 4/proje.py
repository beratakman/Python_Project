
# Bütün Hepsi Büyük Harf(Türkçe Karakterler)

def allUpper(text): # Bir Fonksiyon Açıyoruz
    return str(text).replace("i", "İ").upper() # Replace Komutu ile Türkçe Klavyedeki Harflerin Yazdırılabilmesi için Küçük(i) Harfini, Büyük(İ) Harfiyle Değiştiriyoruz; Ardından Upper Komutunu Verip Bütün Harfleri Büyük Yazdırtırtıyoruz ve Return ilede Geri Döndürtüyoruz

print(allUpper("ismail baki")) # Fonksiyonun İçine Değer Verip Yazdırıyoruz

###############################################################################################################################################################################

# Bütün Hepsi Küçük Harf(Türkçe Karakterler)

def allLower(text): # Bir Fonksiyon Açıyoruz
    return str(text).replace("I", "ı").lower() # Replace Komutu ile Türkçe Klavyedeki Harflerin Yazdırılabilmesi için Büyük(I) Harfini, Küçük(ı) Harfiyle Değiştiriyoruz; Ardından Lower Komutunu Verip Bütün Harfleri Küçük Yazdırtırtıyoruz ve Return ilede Geri Döndürtüyoruz

print(allLower("PINAR BAKIR")) # Fonksiyonun İçine Değer Verip Yazdırıyoruz