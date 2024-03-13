# endcoding="utf-8" türkçe karakterlerin düzgün yazılamsını sağlıyor

       
def spacer(text, spaceLen, dotted, reserve1, reserve2):
    if spaceLen < len(text):
        if dotted == True:
            return text[:spaceLen-3] + "..."
        else: 
            return text[:spaceLen]
    else:
        return text + (spaceLen - len(text)) * " "

successfulStudent = ""
unsuccessfulStudent = ""
with open("Example 9\\informations.txt", "r", encoding="utf-8") as informations: # Bilgilerin yazdığı metin (İSMİ = informations)
    with open("Example 9\\thoseWhoPassed.txt", "w", encoding="utf-8") as passed: # Geçenlerin yazdığı metin (İSİM = passed)
        with open("Example 9\\theRest.txt", "w", encoding="utf-8") as rest: # Kalanların yazdığı metin (İSİM = rest)
            #txt dosyasındaki değerleri okuyoruz
            counter = 0
            
            
            lastReadNameLen = 0 
            lastReadNameSector = 0 
            for read2 in informations.readlines():
                readValues2 = read2.strip().split(",")
                if len(readValues2[0]) > lastReadNameLen: 
                    lastReadNameLen = len(readValues2[0])
                if len(readValues2[1]) > lastReadNameSector: 
                    lastReadNameSector = len(readValues2[1])
            
            informations.seek(0) #okunancak text saır başına döndürür
            for read in informations.readlines():
                counter = counter+ 1
                readLine = read.strip() #boşlukları silmeye yarar
                #print(readLine)
                readValues = readLine.split(",")
                if counter == 1 :
                    pass
                    #print("Başlıklar: " + name)
                else:
                    calc = ((int(readValues[2]) *30) / 100)  + ((int(readValues[3]) *30) / 100) + ((int(readValues[4]) *40) / 100) 
                    #print("name: " + name)
                    #print("notu: " + str(calc))
                    print("final: " + str(readValues[4]))
                    print("calc: " + str(calc))
                    if int(readValues[4]) >= 70 and calc >= 70: #geçti
                        passed.write(readValues[0] + ", " + readValues[1] + "," + str(calc) + "," + str(readValues[2]) + "," + str(readValues[3])+ "," + str(readValues[4]) + "\n")
                    else : #geçti
                        rest.write(spacer(readValues[0], 12, True, "", "") + " " +  spacer(readValues[1],lastReadNameSector+2, True, "", "") + " " + spacer(str(calc),6, False, "", "") + " " + str(readValues[2]) + "," + str(readValues[3])+ "," + str(readValues[4]) + "\n")
                
       
           