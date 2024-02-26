
öğretmenİsmi = (input("Hoşgeldiniz,Lütfen İsminizi Giriniz:"))


girişBilgisi = (input("""Hoşgeldiniz {} Hocam,hangi sınıfın notlarını düzenliceksiniz; 8A / 8B / 8C:
""".format(öğretmenİsmi.capitalize()))).upper()

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
    if öğrenciNumarası != 234 and öğrenciNumarası != 279 and öğrenciNumarası != 451 and öğrenciNumarası != 712 and öğrenciNumarası != 923 and öğrenciNumarası != 123:
            print("Lütfen Okulumuzda Bulunan Bir Öğrencinin numarasını girin")
            exit()
    elif girişBilgisi == "8A" and öğrenciNumarası == 234:
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
    elif girişBilgisi == "8A":
        print("8A Sınıfında Olan Bir Öğrencinin Okul Numarasını girin")
        exit() 
    elif girişBilgisi == "8B":
        print("8B Sınıfında Olan Bir Öğrencinin Okul Numarasını girin")
        exit()
    elif girişBilgisi == "8C":
        print("8C Sınıfında Olan Bir Öğrencinin Okul Numarasını girin")
        exit()   
    else:
        print("2 Lütfen Okulumuzda Bulunan Bir Öğrencinin İsmini girin")
        exit()

    
öğrenciBilgisi()



            
     #   elif  (öğrenciNumarası != 234 and öğrenciNumarası != 279) and (öğrenciNumarası != 451 and öğrenciNumarası != 712) and (öğrenciNumarası != 923 and öğrenciNumarası != 123):
      #       print("8A Sınıfında Olan Bir Öğrencinin Okul Numarasını girin")
      #       exit() 
            