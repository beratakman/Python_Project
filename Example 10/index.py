import os

def dosya_isimlerini_degistir(klasor_yolu, yeni_isim):
    # Klasördeki bütün dosyaları listele
    dosya_listesi = os.listdir(klasor_yolu)
    
    # Dosya listesini sırala
    dosya_listesi.sort()
    
    # Her dosya için indeks numarası ekleyerek yeni ismi belirle ve dosya adını değiştir
    for index, dosya in enumerate(dosya_listesi, start=1):
        # Dosyanın uzantısını koruyarak yeni ismi oluştur
        dosya_uzantisi = os.path.splitext(dosya)[1]
        yeni_dosya_isim = yeni_isim + str(index) + dosya_uzantisi
        
        # Dosya yollarını oluştur
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        yeni_dosya_yolu = os.path.join(klasor_yolu, yeni_dosya_isim)
        
        # Dosya adını değiştir
        os.rename(dosya_yolu, yeni_dosya_yolu)

# Klasör yolunu ve yeni ismi belirtin
klasor_yolu = "E:\www\Liberte\Liberte-V1\images\daily-shoes"
yeni_isim = "daily-shoes-"

# Fonksiyonu çağırarak dosya isimlerini değiştirin
dosya_isimlerini_degistir(klasor_yolu, yeni_isim)
