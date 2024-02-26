
öğretmenİsmi = (input("Hoşgeldiniz,Lütfen İsminizi ve Soyisminizi Giriniz:"))
öğretmenİsmi2 = öğretmenİsmi.title()

girişBilgisi = (input("""Hoşgeldiniz {},hangi sınıfın notlarını düzenliceksiniz; 8A / 8B / 8C:
""".format(öğretmenİsmi2))).upper()

#############################################################################################

if girişBilgisi == "8A":
    print("Hangi öğrencinin notları düzenlenicek\nOkul NO:279\nOkul NO:234")
elif girişBilgisi == "8B":
    print("Hangi öğrencinin notları düzenlenicek\nOkul NO:451\nOkul NO:712")
elif girişBilgisi == "8C":
    print("Hangi öğrencinin notları düzenlenicek\nOkul NO:923\nOkul NO:123")
else:
    print("Lütfen Okulumuzda Bulunan Bir Sınıfı girin")
    exit()

#############################################################################################

öğrenciNumarası = (int(input("Öğrencinin Numarasını Giriniz:")))

def öğrenciBilgisi():
    if girişBilgisi == "8A" and öğrenciNumarası == 234:
        print("234 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Miray\nSoyisim:AKMAN\nVeli Telefon Numaras:0567 523 10 20\nEv Adresi:Talatpaşa MAH./1100. SOK./Siyah Evler Apartmanı/Kat:1/NO:2/İstanbul;Beylikdüzü")
    elif girişBilgisi == "8A" and öğrenciNumarası == 279:
        print("279 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Berat\nSoyisim:AKMAN\nVeli Telefon Numaras:524 765 23 53\nEv Adresi:Talatpaşa MAH./1040. SOK./Ak Evler Apartmanı/Kat:2/NO:4/İstanbul;Beylikdüzü")
    elif girişBilgisi == "8B" and öğrenciNumarası == 451:
        print("451 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Burak\nSoyisim:AKMAN\nVeli Telefon Numaras:0538 324 42 46\nEv Adresi:Talatpaşa MAH./1000. SOK./Pembe Evler Apartmanı/Kat:3/NO:6/İstanbul;Beylikdüzü")
    elif girişBilgisi == "8B" and öğrenciNumarası == 712:
        print("712 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Ayşe\nSoyisim:AKMAN\nVeli Telefon Numaras:0539 194 90 86\nEv Adresi:Talatpaşa MAH./1010. SOK./Yeşil Evler Apartmanı/Kat:1/NO:1/İstanbul;Beylikdüzü")
    elif girişBilgisi == "8C" and öğrenciNumarası == 923:
        print("923 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Onur\nSoyisim:AKMAN\nVeli Telefon Numaras:0510 392 78 72\nEv Adresi:Talatpaşa MAH./1040. SOK./Mavi Evler Apartmanı/Kat:6/NO:11/İstanbul;Beylikdüzü")
    elif girişBilgisi == "8C" and öğrenciNumarası == 123:
        print("123 Okul Numaralı Öğrenci Hakkında Bazı Bilgiler\nİsim:Mustafa\nSoyisim:AKMAN\nVeli Telefon Numaras:0508 344 26 66\nEv Adresi:Talatpaşa MAH./1060. SOK./Gri Evler Apartmanı/Kat:8/NO:8/İstanbul;Beylikdüzü")

def öğrencininİsimBilgisi():
    if öğrenciNumarası != 234 and öğrenciNumarası != 279 and öğrenciNumarası != 451 and öğrenciNumarası != 712  and öğrenciNumarası != 923 and öğrenciNumarası != 123:
        print("Lütfen Okulumuzda Bulunan Bir Öğrencinin Numarasını Giriniz")
        exit()
    elif girişBilgisi == "8A" and öğrenciNumarası == 234:
        print("Miray AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8A" and öğrenciNumarası == 279:
        print("Berat AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8B" and öğrenciNumarası == 451:
        print("Burak AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8B" and öğrenciNumarası == 712:
        print("Ayşe AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8C" and öğrenciNumarası == 923:
        print("Onur AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8C" and öğrenciNumarası == 123:
        print("Mustafa AKMAN'nın Ders Notları Düzenleniyor")
    elif girişBilgisi == "8A":
        print("8A Sınıfında Bulunan Bir Öğrencinin Numarasını Giriniz")
        exit()
    elif girişBilgisi == "8B":
        print("8B Sınıfında Bulunan Bir Öğrencinin Numarasını Giriniz")
        exit()
    elif girişBilgisi == "8C":
        print("8C Sınıfında Bulunan Bir Öğrencinin Numarasını Giriniz")
        exit()
        
öğrencininİsimBilgisi()

#############################################################################################

dersler = ["Türkçe", "Matematik", "Fen Bilimleri", "İnklap Tarihi", "İngilizce"]
notlar = [1,2,3,4,5,6]
ortalamaHesaplama = 0
yılSonuOrtalaması = 0

for ders in dersler:
    ortalamaHesaplama = 0
    for not0 in notlar:
        range(6)
        dersOrtalaması = (int(input("{} {}. Ders Notu:".format(ders,not0))))
        if dersOrtalaması <= -1 or dersOrtalaması > 100:
            print("ERROR 333")
            exit()
        else:
            pass
        ortalamaHesaplama = ortalamaHesaplama + dersOrtalaması
        dersYılSonuOrtalaması = ortalamaHesaplama / 6
    print("{} Yıl Sonu Ortalaması:{}".format(ders,dersYılSonuOrtalaması)) 
    yılSonuOrtalaması = yılSonuOrtalaması + dersYılSonuOrtalaması

yılSonuOrtalaması2 = yılSonuOrtalaması / 5

#############################################################################################

if yılSonuOrtalaması2 >= 0 or yılSonuOrtalaması2 <= 50:
    print("{} Okul Numaralı Öğrenci {} Ortalama ile Sınıfda Kalmıştır")
    öğrenciBilgisi()
    print("Bu Bilgilerden Yararlanarak Ailesi ile İletişime Geçebilirsiniz")
elif yılSonuOrtalaması2 >= 50 or yılSonuOrtalaması2 <= 70:
    print("{} Okul Numaralı Öğrenci {} Ortalama ile Hiç Bir Belge Alamamıştır")
    öğrenciBilgisi()
    print("Bu Bilgilerden Yararlanarak Ailesi ile İletişime Geçebilirsiniz")
elif yılSonuOrtalaması2 >= 70 or yılSonuOrtalaması2 <= 85:
    print("{} Okul Numaralı Öğrenci {} Ortalama ile Teşekkür Belgesi Kazanmıştır")
    öğrenciBilgisi()
    print("Öğrencinin Belgesini Bilgilendirmede Bulunan Ev Adresine Gönderebilirsiniz")
elif yılSonuOrtalaması2 >= 85 or yılSonuOrtalaması2 <= 100:
    print("{} Okul Numaralı Öğrenci {} Ortalama ile Takdir Belgesi Kazanmıştır")
    öğrenciBilgisi()
    print("Öğrencinin Belgesini Bilgilendirmede Bulunan Ev Adresine Gönderebilirsiniz")
else:
    print("ERROR 333")