import re
Texto = str(input("ESCRIBE EL NOMBRE DEL ARCHIVO, POR FAVOR =>>  "))#PIDE EL TXT Y LO LEE, DE MANERA QUE LO ACOMODA E IMPRIME
with open (Texto,"r") as text:
    dto_sigma = int(text.readline().strip())  
    dto_fin = int(text.readline().strip()) 
    dto_estados=int(text.readline().strip())
        #n = [dto_sigma]
        #t = [dto_fin]
    dtos_n =text.readline().strip().split()
    no_n=dtos_n[0].split("Sig")
    f = no_n[1].strip("{}").split(",") 
    print(f) ##ESTE RENGLON SON LOS SIGMA

    dtos_t = text.readline().strip().split()
    no_t=dtos_t[0].split("F")
    s = no_t[1].strip("{}").split(",") 
    print(s) ##ESTE RENGLON SON LOS FINALES

    dtos_p = text.readlines() 
    apilar = ""

    for rest_p in dtos_p:    
        apilar = apilar + rest_p.strip()
        patron = r">(.*?)(,|\})" 
        resultados = re.finditer(patron, apilar) 
        CadEdos = []
        for match in resultados:
            CadEdos.append([match.group(1).strip()])  
        print(CadEdos)

   
     