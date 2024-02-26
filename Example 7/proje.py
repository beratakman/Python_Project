from datetime import date
from datetime import datetime
from datetime import timedelta
import time

def userBirthDate(year,month,day):
    userBirthDate0 = time.struct_time(year,month,day,0,0,0,0,0,0)
    return userBirthDate0

userYear = input("Lütfen Doğduğunuz Yılı Girin. (Sadece Yıl)\n:")
userMonth = input("Lütfen Doğduğunuz Ayı Girin. (Sadece Ay)\n:")
userDay = input("Lütfen Doğduğunuz Günü Girin. (Sadece Gün)\n:")

currentTime = datetime.today()
currentTimeYear = datetime.strftime(currentTime, "%Y")
currentTimeMonth = datetime.strftime(currentTime, "%m")
currentTimeDay = datetime.strftime(currentTime, "%d")