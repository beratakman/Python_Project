dersler = ["Türkçe", "Matematik", "Fen Bilimleri", "İnklap Tarihi", "İngilizce"]
notlar = [1,2,3,4,5,6]
toplamDersNotlari = 0
allNotesTotal = 0


for ders in dersler:
    toplamDersNotu = 0 #her desr döngüsünde o derse ait puan sıfırlanacak
    for not0 in notlar:
        dersNotu = (int(input("{} {}. Ders Notu:".format(ders,not0))))
        toplamDersNotu = toplamDersNotu + dersNotu
    dersOrtalamasi = toplamDersNotu / 6
    print("{} Yıl Sonu Ortalaması:{}".format(ders,dersOrtalamasi)) 
    allNotesTotal = allNotesTotal + dersOrtalamasi
    
print("Yıl Sonu Ortalaması:{}".format(allNotesTotal / 5)) 
