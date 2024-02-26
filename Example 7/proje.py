from datetime import date
from datetime import datetime
from datetime import timedelta
import time

currentTime = datetime.today()

userYear0 = int(input("Lütfen Doğduğunuz Yılı Girin. (Sadece Yıl):\n"))
userMonth0 =  int(input("Lütfen Doğduğunuz Ayı Girin. (Sadece Ay):\n"))
userDay0 =  int(input("Lütfen Doğduğunuz Günü Girin. (Sadece Gün):\n"))

userTime0 = datetime(userYear0, userMonth0, userDay0)

userTime = (currentTime - userTime0) / 365

print(f"{userTime} Yaşındasınız.")


def userBirthDate(year,month,day):
    userBirthDate0 = time.struct_time(year, month, day, 0, 0, 0, 0, 0, None)
    return userBirthDate0

userYear0 = int(input("Lütfen Doğduğunuz Yılı Girin. (Sadece Yıl):\n"))
userMonth0=  int(input("Lütfen Doğduğunuz Ayı Girin. (Sadece Ay):\n"))
userDay0 =  int(input("Lütfen Doğduğunuz Günü Girin. (Sadece Gün):\n"))

print(datetime(userYear0, userMonth0, userDay0))

difference = datetime.now()-datetime(userYear0, userMonth0, userDay0)


fark_gun = difference.days
fark_yil, fark_ay = divmod(fark_gun, 365)

# Ekrana yazdır
print("Girilen tarih ile bugünkü tarih arasındaki fark:")
print(f"{fark_gun} gün, {fark_ay} ay, {fark_yil} yıl")


userYear = userBirthDate(userYear0, 0, 0)
userMonth = userBirthDate(0, userMonth0, 0)
userDay = userBirthDate(0, 0, userDay0)

currentTime = datetime.today()
currentTimeYear = datetime.strftime(currentTime, "%Y")
currentTimeMonth = datetime.strftime(currentTime, "%m")
currentTimeDay = datetime.strftime(currentTime, "%d")

birthYear = currentTimeYear - userYear # Yaş

if currentTimeMonth <= userMonth and currentTimeDay <= userDay:
    birthYear =+ 1
    print(f"{birthYear} yaşındasınız")
else:
    print(f"{birthYear} yaşındasınız")
