from datetime import date
from datetime import datetime
from datetime import timedelta
import time

##############################################################
# Yaş Bulma

currentTime = date.today()

userYear0 = int(input("Lütfen Doğduğunuz Yılı Girin. (Sadece Yıl):\n"))
userMonth0 =  int(input("Lütfen Doğduğunuz Ayı Girin. (Sadece Ay):\n"))
userDay0 =  int(input("Lütfen Doğduğunuz Günü Girin. (Sadece Gün):\n"))

userTime = date(userYear0, userMonth0, userDay0)
dayİnBetween = currentTime - userTime
dayİnBetween = dayİnBetween.days # days == Datetime


userYear, userDay = divmod(dayİnBetween, 365)
userMonth, userDay = divmod(userDay, 30)

# userYear --> Yıl
# userMonth --> Ay
# userDay --> Gün
##############################################################
# Ara Bölge



##############################################################
# Sonraki Yaşına Ne Kadar Zaman Geçince Gireceğini
 
releaseDate0 = date(1, 1, 1)
releaseDate = date(2, 1, 1)

if userMonth == 0:
    userMonth000 = userMonth + 1
    
    userAge0 = date(userYear, userMonth000, userDay)
    userAge0 = userAge0.day
    
    oneYear = releaseDate - releaseDate0
    oneYear = oneYear.days
    
    oneYearLater = userAge0 + oneYear
    
    currentTime000 = currentTime.day
    
    timeİnBetween = oneYearLater - currentTime000
    

    
else:
    userAge = date(userYear, userMonth, userDay)
    userAge = userAge.day

    oneYear = releaseDate - releaseDate0
    oneYear = oneYear.days
    
    oneYearLater = userAge + oneYear
    
    currentTime000 = currentTime.day
    
    timeİnBetween = oneYearLater - currentTime000
    

currentTime0 = currentTime.year

userLastMonth0, userLastDay0 = divmod(timeİnBetween, 30)

userLastMonth = userLastMonth0 - userMonth
userLastDay = userLastDay0 - userDay

if userYear0 <= currentTime0:
    nextMonth = userLastMonth
else:
    nextMonth = userLastMonth  
    
nextDay = abs(userLastDay)
nextAge = userYear + 1
print(f"{userYear} yaşındasınız ve yaklaşık {nextMonth} ay, {nextDay} gün sonra {nextAge} yaşına gireceksiniz.")

exit()