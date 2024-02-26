import time

def zaman_olustur(saat, dakika):
    # Yıl, ay, gün gibi değerleri varsayılan olarak alarak bir struct_time nesnesi oluşturuyoruz.
    # Saat ve dakikayı belirtiyoruz.
    zaman_nesnesi = time.struct_time((0, 0, 0, saat, dakika, 0, 0, 0, None))
    return zaman_nesnesi

# Sabit saat ve dakika bilgilerini belirliyoruz
sabit_saat = 4
sabit_dakika = 0

# İlk zaman bilgilerini kullanıcıdan alıyoruz
ilk_saat = int(input("İlk saat: "))
ilk_dakika = int(input("İlk dakika: "))

# İkinci zaman bilgilerini kullanıcıdan alıyoruz
ikinci_saat = int(input("İkinci saat: "))
ikinci_dakika = int(input("İkinci dakika: "))

# İlk ve ikinci zaman nesnelerini oluşturuyoruz
ilk_zaman = zaman_olustur(ilk_saat, ilk_dakika)
ikinci_zaman = zaman_olustur(ikinci_saat, ikinci_dakika)

# İki zaman nesnesini topluyoruz
toplam_saat = ilk_zaman.tm_hour + ikinci_zaman.tm_hour
toplam_dakika = ilk_zaman.tm_min + ikinci_zaman.tm_min

# Dakikayı saate dönüştürme
toplam_saat += toplam_dakika // 60
toplam_dakika = toplam_dakika % 60

# Sabit zamandan toplam zamanı çıkarıyoruz
fark_saat = toplam_saat - sabit_saat
fark_dakika = toplam_dakika - sabit_dakika

print("Fark:", fark_saat, "saat", fark_dakika, "dakika")