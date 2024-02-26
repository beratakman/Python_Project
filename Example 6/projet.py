
# Modüller

import random
import time
import Function.function as function

######################################################################################################################################################

entrance = int(input("E-Okula Hoşgeldiniz Lütfen İşlem Yapacağınız Bölüm Numarasını Giriniz\n(1:Devamsızlık, 2:Ders Programı, 3:Sınav Sonucu Öğrenme):\n"))

#################################################################################

if entrance == 1:
    print("Şuanda Mevcut Değil, Lütfen Yeni Okul Yılında Tekrar Deneyin")
    exit()
elif entrance == 2:
    print("Şuanda Mevcut Değil, Lütfen Yeni Okul Yılında Tekrar Deneyin")
    exit()
elif entrance == 3:
    print("Sınav Sonucunuzu Öğrenmek İçin Giriş Yapınız")
else:
    print("Geçerli bir bölüm numarası giriniz")
    exit()

######################################################################################################################################################

name = input("İsminizi Giriniz:")
surname = input("Soyisminizi Giriniz")
password = input("Şifrenizi Giriniz:")

#################################################################################

print("Giriş Başarılı Lütfen Bekleyin")
time.sleep(4)

######################################################################################################################################################

formOfAddress = (name + " " + surname).title()

examGrade = (int(input(f"Hoşgeldin {formOfAddress}, Lütfen Sınavdan Aldığınız Notu Giriniz\n(Sınır 500 Puan):\n")))

######################################################################################################################################################


hours00 = int(input("Lütfen Sözel Kitapçığını Kaç Saate Bitirdiğinizi Yazınız\n(Sınavda Verilen Süre: 2 Saat, Sadece Saati Yazınız):\n"))
minute00 = int(input("Lütfen Sözel Kitapçığını Kaç Dakikada Bitirdiğinizi Yazınız\n(Sınavda Verilen Süre: 2 Saat, Sadece Dakikayı Yazınız):\n"))
verbalDuration = function.totalExamTime0(hours00,minute00)

hours000 = int(input("Lütfen Sayısal Kitapçığını Kaç Saate Bitirdiğinizi Yazınız\n(Sınavda Verilen Süre: 2 Saat, Sadece Saati Yazınız):\n"))
minute000 = int(input("Lütfen Sayısal Kitapçığını Kaç Dakikada Bitirdiğinizi Yazınız\n(Sınavda Verilen Süre: 2 Saat, Sadece Dakikayı Yazınız):\n"))
numericalDuration = function.totalExamTime0(hours000,minute000)

hours0 = 3
minute0 = 60
totalExamTime = function.totalExamTime0(hours0,minute0)

totalHours = verbalDuration.tm_hour + numericalDuration.tm_hour
totalMinutes = verbalDuration.tm_min + numericalDuration.tm_min

totalHours += totalMinutes // 60
totalMinutes = totalMinutes % 60

finishExamTimeHours = abs(totalHours - totalExamTime.tm_hour)
finishExamTimeMinutes = abs(totalMinutes - totalExamTime.tm_min)

######################################################################################################################################################
    
print("Lütfen Biraz Bekleyin, Notunuz Hesaplanıyor")
time.sleep(7)

######################################################################################################################################################

randomNumber0 = random.randint(985001,1000000)
randomNumber1 = random.randint(950001,985000)
randomNumber2 = random.randint(800001,950000)
randomNumber3 = random.randint(550001,800000)
randomNumber4 = random.randint(400001,550000)
randomNumber5 = random.randint(150001,400000)
randomNumber6 = random.randint(50001,150001)
randomNumber7 = random.randint(2,50000)

#################################################################################

randomNumber8 = random.randint(50001,100001)
randomNumber9  = random.randint(2,25000)

#################################################################################

randomNumber10 = random.randint(50001,75001)
randomNumber11  = random.randint(2,15000)

#################################################################################
    
if examGrade == 0:
    print(f"Barajı Geçemediniz\nSıranız:{randomNumber0}")
elif examGrade >= 1 and examGrade <= 50:
    print(f"Barajı Geçemediniz\nSıranız:{randomNumber1}")
elif examGrade >= 51 and examGrade <= 100:
    print(f"Barajı Geçemediniz\nSıranız:{randomNumber2}")
elif examGrade >= 101 and examGrade <= 200:
    print(f"Tebrikler, Sıranız:{randomNumber3}")
elif examGrade >= 201 and examGrade <= 300:
    print(f"Tebrikler, Sıranız:{randomNumber4}")
elif examGrade >= 301 and examGrade <= 400:
    print(f"Tebrikler, Sıranız:{randomNumber5}")
        
#################################################################################

elif examGrade >= 401 and examGrade <= 450:
    print(f"Tebrikler, Sıranız:{randomNumber6}")
elif (examGrade >= 401 or examGrade <= 450) and  (finishExamTimeHours <= 2 or finishExamTimeHours >=1) and (finishExamTimeMinutes <= 60 or finishExamTimeMinutes >= 0):
        print(f"Tebrikler, Sıranız:{randomNumber8}")
elif (examGrade >= 401 or examGrade <= 450) and  finishExamTimeHours == 3 and (finishExamTimeMinutes <= 60 or finishExamTimeMinutes >= 0):
        print(f"Tebrikler, Sıranız:{randomNumber10}")
        
#################################################################################

elif examGrade >= 451 and examGrade <= 499:
    print(f"Tebrikler, Sıranız:{randomNumber7}")
elif (examGrade >= 451 or examGrade <= 499) and  (finishExamTimeHours <= 2 or finishExamTimeHours >=1) and (finishExamTimeMinutes <= 60 or finishExamTimeMinutes >= 0):
    print(f"Tebrikler, Sıranız:{randomNumber9}")
elif (examGrade >= 451 or examGrade <= 499) and  finishExamTimeHours == 3 and (finishExamTimeMinutes <= 60 or finishExamTimeMinutes >= 0):
    print(f"Tebrikler, Sıranız:{randomNumber11}")
             
#################################################################################
        
elif examGrade == 500:
    print(f"Sıranız:1")
