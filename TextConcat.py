file = open("textofinal.txt","w", encoding="utf8") 
for x in range(0, 54):
    fileaux = open("textos\\"+str(x) + ".txt","r", encoding="utf8") 
    file.write("\n")
    file.write(fileaux.read())
    fileaux.close()
file.close()
