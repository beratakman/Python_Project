with open("functions","w"):
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

    functionTitles = ["listFunctions","tupleFunctions","dictFunctions","setFunctions","strFunctions","intFunctions","floatFunctions"] # Listeler alt alta olucağı için en üstlerine bir başlık koymamız gerekecek ve o başlık işinide bu liste karşılayacak
    functionClasses = [listFunctions,tupleFunctions,dictFunctions,setFunctions,strFunctions,intFunctions,floatFunctions] # ve alt alta yazmadan önce bilgi almak içinde bu listeyi kullanıcaz

    maxFunction = 0 # Başlangıçta toplam fonksiyon değişkeninde hiç bir değer yok
    for listedFunctions in functionClasses: # fonksiyon isimleri yazan listenin içinden listeleri tek tek sıralıyoruz
        if len(listedFunctions) > maxFunction: # eğer herhangi bir fonksiyon sayısı bizim şuanki sayımızdan büyükse
             maxFunction = len(listedFunctions) # toplam fonksiyon değişkenine bulduğumuz en büyük rakamı seçtirtiyoruz  
        
    for titles in functionTitles:
        print(titles,end="")
        print(" " * 17,end="")
        
    for x in range(maxFunction):
        print()
        for listedFunctions in functionClasses:
            if x >= len(listedFunctions):
                print("-------",end="")
                print(" " * 23,end="")
            else:
                print(listedFunctions[x],end="")
                print(" " * (30 - len(listedFunctions[x])),end="")
                
with open("functions.txt","w") as toWrite:
    text = toWrite.write()
    print(text)