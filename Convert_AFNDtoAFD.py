import re
def read(TEXTO):
    with open(TEXTO, 'r') as text:
        valor_estados = int(text.readline().strip())
        valor_sigma = int(text.readline().strip())
        valor_f = int(text.readline().strip())
        datos_sig = text.readline().strip().split()
        sin_n=datos_sig[0].split("Sig")
        sig = sin_n[1].strip("{}").split(",") 
        print(f"Valor de Sigma = {sig}")

        datos_f = text.readline().strip().split()
        sin_t=datos_f[0].split("F")
        fd = sin_t[1].strip("{}").split(",") 
        print(f"Valores edos finales = {fd}")

        datos_estados = text.readlines()
        apilar = ""

        for restantes_estados in datos_estados:
            apilar = apilar + restantes_estados.strip()

        patron = r">(.*?)(,|\})"

        res = re.finditer(patron, apilar)
        valores = []

        for match in res:
            valores.append(match.group(1).strip().split(" | "))
            
        print(f"Valor leido de Estados = {valores}")
        return sig, fd, valores
      
def buscar_diferentes(valores):
    estados_diferentes = set()
    for sublista in valores:
        for elemento in sublista:
            if len(elemento) > 1 and elemento != 'NULL':
                estados_diferentes.add(elemento)
    return sorted(estados_diferentes)

def transiciones(valores, estados_afnd, sig):
    datos_leidos = []
    for valor_sigma in sig:
        for j in estados_afnd:
            interaccion = []
            for i in j:
                interaccion.extend(valores[int(i)][sig.index(valor_sigma)])
            datos_leidos.append(sorted(set(interaccion)))
    return datos_leidos 

def convertir_afnd_a_afd(sig, fd, valores):
    nuevos_valores = buscar_diferentes(valores)
    nuevos_valores2 = [list(map(int, estado)) for estado in nuevos_valores]

    while True:
        nuevos_estados = transiciones(valores, nuevos_valores2, sig)
        lista_final = []
        for sublista in nuevos_estados:
            nueva_sublista = []
            for elemento in sublista:
                if elemento != 'N' and elemento != 'U' and elemento != 'L' and elemento != 'L':
                    nueva_sublista.extend(list(map(int, elemento)))
            lista_final.append(sorted(set(nueva_sublista)))

        for inser in nuevos_valores2:
            lista_final.append(inser)

        set_lista_final = set(map(tuple, lista_final))
        set_nuevos_valores2 = set(map(tuple, nuevos_valores2))

        resultado = set_lista_final.symmetric_difference(set_nuevos_valores2)
        resultado = list(map(list, resultado))

        if resultado == []:
            break

        nuevos_valores2.extend(resultado)

    nuevos_valores2.sort()

    print("Lista de estados = ", nuevos_valores2)

archivo = input("Ingrese el nombre del archivo: ")
sig, fd, valores = read(archivo)
convertir_afnd_a_afd(sig, fd, valores)
