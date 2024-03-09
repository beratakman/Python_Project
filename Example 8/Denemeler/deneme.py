listFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for listFunction in dir(list): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if listFunction.startswith("__") and listFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    listFunctions.append(listFunction) # Kalan fonksiyonları ekliyoruz

tupleFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for tupleFunction in dir(tuple): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if tupleFunction.startswith("__") and tupleFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    tupleFunctions.append(tupleFunction) # Kalan fonksiyonları ekliyoruz
     
dictFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for dictFunction in dir(dict): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if dictFunction.startswith("__") and dictFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    dictFunctions.append(dictFunction) # Kalan fonksiyonları ekliyoruz
    
setFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for setFunction in dir(set): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if setFunction.startswith("__") and setFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    setFunctions.append(setFunction) # Kalan fonksiyonları ekliyoruz
    
strFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for strFunction in dir(str): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if strFunction.startswith("__") and strFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    strFunctions.append(strFunction) # Kalan fonksiyonları ekliyoruz
    
intFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for intFunction in dir(int): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if intFunction.startswith("__") and intFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    intFunctions.append(intFunction) # Kalan fonksiyonları ekliyoruz

floatFunctions = [] # Bizlerin fonksiyonların isimlerini alıcağımız yer
for floatFunction in dir(float): # döngü ile listlerin bütün fonksiyonlarını yazdırıyoruz (dir'in içine yazdığımız veri yapılarının fonksiyonlarının hepsini gösterir)
    if floatFunction.startswith("__") and floatFunction.endswith("__"): # başlagıcı ve sonu bu şekilde ise
        continue # Es geçerek devam ediuyoruz
    floatFunctions.append(floatFunction) # Kalan fonksiyonları ekliyoruz

functionClasses = [listFunctions,tupleFunctions,dictFunctions,setFunctions,strFunctions,intFunctions,floatFunctions]
