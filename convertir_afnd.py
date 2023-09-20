import re

def lectura(archivo):
    with open(archivo, 'r') as f:
        valor_estados = int(f.readline().strip())
        valor_sigma = int(f.readline().strip())
        valor_f = int(f.readline().strip())

        datos_sig = f.readline().strip().split()
        sin_n=datos_sig[0].split("Sig")
        sig = sin_n[1].strip("{}").split(",") 
        print(f"Valor leido de Sigma = {sig}")

        datos_f = f.readline().strip().split()
        sin_t=datos_f[0].split("F")
        fd = sin_t[1].strip("{}").split(",") 
        print(f"Valor leido de F = {fd}")

        datos_estados = f.readlines()
        acumulable = ""

        for restantes_estados in datos_estados:
            acumulable = acumulable + restantes_estados.strip()

        patron = r">(.*?)(,|\})"

        resultados = re.finditer(patron, acumulable)
        valores = []

        for match in resultados:
            valores.append(match.group(1).strip().split(" | "))
            
        print(f"Valor leido de Estados = {valores}")
        return sig, fd, valores
    
    
estados_diferentes = []
def buscar_diferentes(valores):
    for x in valores:
        for xy in x:
            if len(xy) != 1 and xy != 'NULL':
                if xy not in estados_diferentes:
                    estados_diferentes.append(xy)
    return estados_diferentes

def transiciones(valores, estados_afnd, sig):
    interaccion = []
    datos_leidos = []
    for valor_sigma in sig:
        for j in estados_afnd:
            interaccion = []
            for i in j:
                interaccion.append(valores[int(i)][sig.index(valor_sigma)])
                #print(f"valor index de sigma = {sig.index(valor_sigma)}")
            datos_leidos.append(interaccion)
    return datos_leidos 

def convertir_afnd_a_afd(sig, fd, valores):

    nuevos_valores = buscar_diferentes(valores)
    nuevos_valores2 = []
    for num in nuevos_valores:
        digitos = []
        for digito in num:
            digitos.append(int(digito))
        nuevos_valores2.append(digitos)

    fin = False
    while fin == False:
        nuevos_estados = transiciones(valores, nuevos_valores2, sig)
        lista_final = []
        for sublista in nuevos_estados:
            nueva_sublista = []
            valores_agregados = set()
            for elemento in sublista:
                for caracter in list(str(elemento)):
                    if caracter not in valores_agregados and caracter != 'N' and caracter != 'U' and caracter != 'L' and caracter != 'L':
                        nueva_sublista.append(int(caracter))
                        valores_agregados.add(caracter)
            lista_final.append(nueva_sublista)

        for inser in nuevos_valores2:
            lista_final.append(inser)

        
        set_lista_final = set(map(tuple, lista_final))
        set_nuevos_valores2 = set(map(tuple, nuevos_valores2))

      
        resultado = set_lista_final.symmetric_difference(set_nuevos_valores2)

        
        resultado = list(map(list, resultado))

        if resultado == []:
            fin = True
        else: 
            for dar in resultado:
                nuevos_valores2.append(dar)

    temp_set = set()
    for orden2 in nuevos_valores2:
        orden2_ordenada = sorted(orden2)
        tupla = tuple(orden2_ordenada)
        temp_set.add(tupla)

    nuevos_valores2 = [list(tupla) for tupla in temp_set]
    nuevos_valores2.sort()

    print("Lista de estados = ",nuevos_valores2)

     
 
sig, fd, valores = lectura("Aut3.txt")
convertir_afnd_a_afd(sig, fd, valores)