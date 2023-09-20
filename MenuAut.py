
import re
import os
import random
import time  ##MENÚ NUEVO, ACTUALIZADO. EL ORIGINAL NO LO DESHAGAS.
from colorama import Fore, Style


def cargar_memoria_grams():
    with open(Texto, 'r') as f:
        dto_n = int(f.readline().strip())  
        dto_t = int(f.readline().strip())
        f.readline().strip()
        f.readline().strip()
        # n = [dto_n]
        # t = [dto_t]
        dtos_n = f.readline().strip().split()
        no_n=dtos_n[0].split("N")
        n = no_n[1].strip("{}").split(",") #split se utiliza para separar palabras con poco espacio
        print( Fore.MAGENTA + "VALOR LEÍDO NO TERMINALES=>>> " + Style.RESET_ALL , n)
        dtos_t = f.readline().strip().split()
        no_t=dtos_t[0].split("T")
        t = no_t[1].strip("{}").split(",") 
        print( Fore.MAGENTA + "VALOR LEÍDO TERMINALES=>>> " + Style.RESET_ALL, t)

        dtos_p = f.readlines() 
        apilar = ""

        for rest_p in dtos_p:    # almacacena el contenido de las demás líneas 
            apilar = apilar + rest_p.strip()
       
        patron = r">(.*?)(,|\})" # patron para determinar entre que signos extraer el texto, captura cualquier cantidad de caracteres entre esos signos 
        resultados = re.finditer(patron, apilar) #"finditer" busca todo los valores que coinciden con la cadena
        res = []

        for match in resultados:
            res.append(match.group(1).strip().split(" | ")) #"corchete sobre corchete es una matrix"
        print(res)

    return t, n, res
            
####################################################################################################################################################
def cadena_random(t, n, p):

        indice = random.randint(0, len(p[0])-1)
        elegido = p[0][indice]
        print(elegido)

        control = True
        recursividades = 0
        while control:
             for v1 in elegido:
                if v1 in n:
                    recursividades = recursividades + 1
                    i = n.index(v1)
                    indice = random.randint(0, len(p[i])-1)
                    elegido1 = p[i][indice]
                    elegido = elegido.replace(v1, elegido1, 1)
                    print(elegido)
                    v2 = list(elegido)
                    control = any(fin in n for fin in v2)
                    if control:
                        break
                else:
                    control = False 
        return recursividades


################################################################################################################################

def recurcion():

    Texto = str(input("ESCRIBE EL NOMBRE DEL ARCHIVO : "))
    with open (Texto,"r") as text:
        dto_n = int(text.readline().strip())  
        dto_t = int(text.readline().strip())
        text.readline().strip()
        text.readline().strip()
        n = [dto_n]
        t = [dto_t]
        dtos_n = text.readline().strip().split()
        no_n=dtos_n[0].split("N")
        n = no_n[1].strip("{}").split(",") 
        print(n) 

        dtos_t = text.readline().strip().split()
        no_t=dtos_t[0].split("T")
        t = no_t[1].strip("{}").split(",") 
        print(t)
        dtos_p = text.readlines() 
        apilar = ""

        for rest_p in dtos_p:    
            apilar = apilar + rest_p.strip()
    
        patron = r">(.*?)(,|\})" # patron para determinar entre que signos extraer el texto, captura cualquier cantidad de caracteres entre esos signos 
        resultados = re.finditer(patron, apilar) #"finditer" busca todo los valores que coinciden con la cadena
        p = []

        for match in resultados:
            p.append(match.group(1).strip().split("|"))  
        print(p)

    vuelta=0
    recurcion=0
    for vector in p: ##
         for i in range(len(vector)):
            
            if n[vuelta] in vector[i]:
                print (f"EL VALOR ´{n[vuelta]}´ SE ENCUENTRA EN=>> {vector[i]}")
                recurcion=recurcion+1
                vuelta=vuelta+1
           
    print(f"El valor total de recurciones es: {recurcion}")


################################################################################################################################
def cargar_memoria():
    #Texto = str(input("ESCRIBE EL NOMBRE DEL ARCHIVO, POR FAVOR =>>  "))#PIDE EL TXT Y LO LEE, DE MANERA QUE LO ACOMODA E IMPRIME
    with open (Texto,"r") as text:
        dto_sigma = int(text.readline().strip())  
        dto_fin = int(text.readline().strip()) 
        dto_estados=int(text.readline().strip())
        
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
            CadEdos.append(match.group(1).strip().split(" | ")) 
            print(CadEdos)
    return f, s, CadEdos
            
################################################################################################################################
def cadena_eval():
    
    with open (Texto,"r") as text:
        dto_sigma= int(text.readline().strip())  
        dto_fin= int(text.readline().strip()) 
        dto_estados=int(text.readline().strip())
       
        dtos_n =text.readline().strip().split()
        no_n=dtos_n[0].split("Sig")
        f = no_n[1].strip("{}").split(",") 
        print("VALORES SIGMA DEL gram SELECCIONADO =>>>> ",f) ##ESTE RENGLON SON LOS SIGMA

        dtos_t = text.readline().strip().split()
        no_t=dtos_t[0].split("F")
        s = no_t[1].strip("{}").split(",") 
        print("VALORES EDOS FINALES DEL AUTOMATA SELECCIONADO =>>>  ",s) ##ESTE RENGLON SON LOS FINALES

        dtos_p = text.readlines() 
        apilar = ""

        for rest_p in dtos_p:    
            apilar = apilar + rest_p.strip()
       
        patron = r">(.*?)(,|\})" 
        resultados = re.finditer(patron, apilar) 
        CadEdos = []
        for match in resultados:
            CadEdos.append([match.group(1).strip()])  
        print("AUTOMATA SELECCIONADO =>>>  ", CadEdos)  
    cad_in=input("FAVOR DE INGRESAR LA CADENA A EVALUAR=>> ")
    for i in range(len(cad_in)):
        car=cad_in[i]
        #print(car) #BANDERA
        for j in range(len(f)):
            if f[j]==car:
                pos=j
                break
        else:
            print(f"{car} NO ESTA EN EL ALFABETO") #BANDERA
            print(f"{f[j]} DIFERENTE de {car}") #bandera
            print("CADENA NO VÁLIDA")
            break
    else:
     print("CADENA VÁLIDA") #BANDERA

################################################################################################################################
def determinista():
   
    with open (Texto,"r") as text:
        dto_sigma = int(text.readline().strip())  
        dto_fin = int(text.readline().strip()) 
        dto_estados=int(text.readline().strip())
        
        dtos_n =text.readline().strip().split()
        no_n=dtos_n[0].split("Sig")
        f = no_n[1].strip("{}").split(",") 
        print("-> VALOR SIGMA LEÍDO =>>> ", f) ##ESTE RENGLON SON LOS SIGMA

        dtos_t = text.readline().strip().split()
        no_t=dtos_t[0].split("F")
        s = no_t[1].strip("{}").split(",") 
        print("-> VALOR EdoFINAL LEÍDO =>>> ", s) ##ESTE RENGLON SON LOS FINALES

        dtos_p = text.readlines() 
        apilar = ""

        for rest_p in dtos_p:    
            apilar = apilar + rest_p.strip()
       
        patron = r">(.*?)(,|\})" 
        resultados = re.finditer(patron, apilar) 
        CadEdos = []
        for match in resultados:
            CadEdos.append(match.group(1).strip().split(" | "))  
        print("-> AUTOMATA =>>>", CadEdos)

    es_determinista = all(len(yo)==1 or yo == "NULL" for fila in CadEdos for yo in fila)
    
    if es_determinista:
        print("\n \n" "EL AUTÓMATA ES DETERMINISTA")
    else:
        print( "\n \n" "EL AUTÓMATA NO ES DETERMINISTA")

################################################################################################################################
def read(archivo):
    with open(archivo, 'r') as f:
        estados = int(f.readline().strip())
        print(f"Numero de Estados -> {estados}")
        sigma = int(f.readline().strip())
        print(f"Tamaño de sigma -> {sigma}")
        finales = int(f.readline().strip())
        print(f"Tamaño de Estados Finales -> {finales}")

        datos_sig = f.readline().strip().split()
        sin_n=datos_sig[0].split("Sig")
        sig = sin_n[1].strip("{}").split(",") 
        print(f"Valores de Sigma -> {sig}")

        datos_f = f.readline().strip().split()
        sin_t=datos_f[0].split("F")
        fd = sin_t[1].strip("{}").split(",") 
        print(f"Valores de Estados Finales -> {fd}")

        alcanzables = f.readlines()
        acumulador = ""
        

        for restantes_estados in alcanzables:
            acumulador = acumulador+ restantes_estados.strip()

        patron = r">(.*?)(,|\})"

        resultados = re.finditer(patron, acumulador)
        valores = []

        for aux in resultados:
            valores.append(aux.group(1).strip().split(" | "))
            
        print(f"Transiciones -> {valores}")

        return sig, fd, valores

def matriz_to_Dict(matriz, Sigma):
    tabla_transiciones = {}
    for i in range(len(matriz)):
        estado = str(i)
        transiciones = {}
        for j in range(len(Sigma)):
            simbolo = Sigma[j]
            estado_destino = matriz[i][j]
            transiciones[simbolo] = estado_destino
        tabla_transiciones[estado] = transiciones
    return tabla_transiciones
################################################################################################################################
def minimizacion(Sigma, Estados, Estado_inicial, Estados_finales, Transiciones):  # Paso 1: Inicialización
    
    n = len(Estados)
    particion_actual = [set(Estados_finales), set(
        Estados) - set(Estados_finales)]
    particion_anterior = []

    # Paso 2: División
    while particion_actual != particion_anterior:
        particion_anterior = particion_actual.copy()
        for i, particion in enumerate(particion_actual):
            for simbolo in Sigma:
                transiciones = {}
                for estado in particion:
                    if Transiciones[estado].get(simbolo) is None:
                        estado_destino = None
                    else:
                        estado_destino = Transiciones[estado][simbolo]
                    if estado_destino in transiciones:
                        transiciones[estado_destino].add(estado)
                    else:
                        transiciones[estado_destino] = {estado}
                particion_actual[i] = set.union(particion_actual[i], *[particion_actual[j] for j in range(len(particion_actual)) if transiciones.get(
                    list(particion_actual[j])[0]) is not None and len(particion_actual[j] & transiciones[list(particion_actual[j])[0]]) > 0])
                particion_actual.extend([particion_actual[j] & transiciones[list(particion_actual[j])[0]] for j in range(len(particion_actual)) if transiciones.get(list(
                    particion_actual[j])[0]) is not None and len(particion_actual[j] & transiciones[list(particion_actual[j])[0]]) > 0 and particion_actual[j] not in particion_actual])

    
    tabla_transiciones_minimizada = {}
    for particion in particion_actual:
        estado = list(particion)[0]
        tabla_transiciones_minimizada[estado] = {}
        for simbolo in Sigma:
            estado_destino = None
            for estado_en_particion in particion:
                if Transiciones[estado_en_particion].get(simbolo) is not None:
                    estado_destino = Transiciones[estado_en_particion][simbolo]
                    break
            for particion_destino in particion_actual:
                if estado_destino in particion_destino:
                    tabla_transiciones_minimizada[estado][simbolo] = list(particion_destino)[
                        0]
                    break

    
    print(f"Matriz Automata minimizado : {tabla_transiciones_minimizada}")
  

    #print(tabulate(rows, headers=headers, tablefmt="grid"))
  
    
def conseguir_estados(transicionesDict):
    estados = []
    for estado in transicionesDict:
        estados.append(estado)
    return estados

estados_diferentes = []
def buscar_diferentes(valores):
    for x in valores:
        for xy in x:
            if len(xy) != 1 and xy != 'NULL':
                if xy not in estados_diferentes:
                    estados_diferentes.append(xy)
                    print("diferentes = ", estados_diferentes)
    return estados_diferentes

def transiciones(valores, estados_afnd, sig):
    interaccion = []
    datos_leidos = []
    #print(f"estados afnd = {estados_afnd}")
    for valor_sigma in sig:
        for j in estados_afnd:
            interaccion = []
            for i in j:
                interaccion.append(valores[int(i)][sig.index(valor_sigma)])
                #print(f"valor index de sigma = {interaccion}")
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

    #print(f"valor de la variable nuevos_valores2 = {nuevos_valores2}")

    fin = False
    while fin == False:
        nuevos_estados = transiciones(valores, nuevos_valores2, sig)
        #print(f"valor de nuevos valores gg = {nuevos_valores}")

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
                        
        #print(f"valor de la variable lista_final = {lista_final}")

        # Convertir las listas a conjuntos
        set_lista_final = set(map(tuple, lista_final))
        set_nuevos_valores2 = set(map(tuple, nuevos_valores2))

        # Calcular la diferencia simÃ©trica
        resultado = set_lista_final.symmetric_difference(set_nuevos_valores2)

        # Convertir el conjunto de nuevo a una lista
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
    #print("valores no repetidos",resultado)  # Imprime: [[1, 0, 2], [1, 3, 0]]

   # print("valor final de nuevos valores 2 = ",nuevos_valores2)

    print(  Fore.GREEN + "Nuevos edos del AFD: -> " + Style.RESET_ALL ,nuevos_valores2  )  
    print(  Fore.GREEN + "Transiciones del AFD -> " + Style.RESET_ALL ,set_lista_final )
    #print(  Fore.GREEN + "Edos Finales del AFD -> " + Style.RESET_ALL ,nuevos_finales )
    
    
    
################################################################################################################################################################################################################################################################
if __name__ == "__main__":  
    
    menu_principal = True
    while menu_principal == True:
        
        print("\tMENU DE OPCIONES\n") 
        print ("1) Gramaticas")
        print ("2) Automatas")
        print ("3) Salir")

        op = input("FAVOR DE ELEGIR UNA OPCION DEL MENÚ DADO ->> ")

        if (op == '1'): 
            menu_principal1  = True
            t = ""
            n = ""
            res = ""
            while menu_principal1 == True: 

                print("\tMENU DE OPCIONES GRAMÁTICAS \n")
                print("A) Cargar gramática ->> ")
                print("B) Generar cadenas aleatorias ->> ")
                print("C)Recursividadeas totales de la gramatica->> ")
                print("D) SALIR")

                op2 = (input(" \n INGRESE UNA OPCION DEL MENÚ GRAMAS ->>>> ")).upper()

                if op2 == 'A': 
                    print( Fore.GREEN + "HA INGRESADO A CARGA DE GRAMATICA, INGRESE EL NOMBRE CORRECTO" + Style.RESET_ALL  )
                    Texto = str(input("\tFAVOR DE INGRESAR EL NOMBRE DEL ARCHIVO TXT ->>>>   "))
                    os.system("cls")
                    if Texto in ['Gram1.txt', 'Gram2.txt', 'Gram3.txt', 'Gram4.txt' ]:
                        t, n, res = cargar_memoria_grams()
                    else:
                        print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Aut1.txt) " + Style.RESET_ALL)
                    time.sleep(5)

                elif op2 == 'B':
                    print ( Fore.GREEN + "HA INGRESADO A GENERAR CADENAS ALEATORIAS DE GRAMATICA, INGRESE EL NOMBRE CORRECTO" + Style.RESET_ALL  )
                    if t == "" or n == "" or res == "":
                        Texto = str(input("\tFAVOR DE INGRESAR EL NOMBRE DEL ARCHIVO TXT ->>>>   "))
                        os.system("cls")
                        if Texto in ['Gram1.txt', 'Gram2.txt', 'Gram3.txt', 'Gram4.txt' ]:
                            t, n, res = cargar_memoria_grams()
                        else:
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Aut1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                    else:
                        if Texto in ['Gram1.txt', 'Gram2.txt', 'Gram3.txt', 'Gram4.txt' ]:
                            recursion = cadena_random(t, n, res)
                        else:
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Aut1 (1-8).txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                        

                elif op2 == 'C':
                    print ( Fore.GREEN + "HA INGRESADO RECURSIONES DE LA GRAMATICA, INGRESE EL NOMBRE CORRECTO" + Style.RESET_ALL  )
                    if t == "" or n == "" or res == "":
                        Texto = str(input("\tFAVOR DE INGRESAR EL NOMBRE DEL ARCHIVO TXT ->>>>   "))
                        if Texto in ['Gram1.txt', 'Gram2.txt', 'Gram3.txt', 'Gram4.txt' ]:
                            t, n, res = cargar_memoria_grams()
                        else:
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Aut1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                    else:
                        os.system("cls")
                        if recursion == "":
                            print("Se necesita crear una cadena alaetoria primero")
                            recursion = cadena_random(t, n, res)
                        else:
                            print(f"Las recursividades son = {recursion}")
                   

                elif op2 == 'D': 
                    os.system("cls")
                    print( Fore.BLUE + " \n HA SALIDO DEL PROGRAMA. ¡VUELVA PRONTO!" + Style.RESET_ALL ) 
                    menu_principal1 = False
                    

#MENU DE AUTOMATAS

        elif op == '2': 
            menu_principal2 = True
            f = ""
            s = ""
            cadena = ""
            while menu_principal2 == True: 
                print("\tMENU DE OPCIONES AUTOMATAS \n") 
                print("A) CARGAR AUTOMATA A MEMORIA.")  
                print("B) EVALUAR CADENA AUTOMATA.")  
                print("C) DETERMINAR TIPO DE AUTOMATA.")    
                print("D) CONVERSION DE AUTOMATA") 
                print("E) MINIMIZACION DE UN AFD.") 
                print("F) SALIR.")

                opcion = (input(" \n INGRESE UNA OPCION ->>>> ")).upper()
            
            
                if (opcion == 'A'):
                    Texto = str(input("\tFAVOR DE INGRESAR EL NOMBRE DEL ARCHIVO TXT ->>>>   "))
                    if Texto in ['Aut1.txt', 'Aut2.txt', 'Aut3.txt', 'Aut4.txt', 'Aut5.txt', 'Aut6.txt', 'Aut7.txt', 'Aut8.txt']:
                        f, s, cadena = cargar_memoria()
                    else:
                        print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Gram1.txt) " + Style.RESET_ALL)
                    time.sleep(5)
                    os.system("cls")
                    

                elif opcion == 'B': #EVALUA CADENA
                    if f == "" or s == "" or cadena == "":
                        if Texto in ['Aut1.txt', 'Aut2.txt', 'Aut3.txt', 'Aut4.txt', 'Aut5.txt', 'Aut6.txt', 'Aut7.txt', 'Aut8.txt' ]:
                            f, s, cadena = cargar_memoria()
                        else:
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Aut1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                    else:
                        
                        cadena_eval()
                       
                        time.sleep(5)
                        os.system("cls")
                    
                elif opcion == 'C': #DETERMINA SI ES O NO DETERMINISTA
                    if f == "" or s == "" or cadena == "":
                        if Texto in ['Aut1.txt', 'Aut2.txt', 'Aut3.txt', 'Aut4.txt', 'Aut5.txt', 'Aut6.txt', 'Aut7.txt', 'Aut8.txt' ]:
                            f, s, cadena = cargar_memoria()
                        else: 
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Gram1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                    else: 
                        determinista()
                        time.sleep(5)
                        
               
                elif opcion  ==  'D':
                    if f == "" or s == "" or cadena == "":
                        if Texto in ['Aut1.txt', 'Aut2.txt', 'Aut3.txt', 'Aut4.txt', 'Aut5.txt', 'Aut6.txt', 'Aut7.txt', 'Aut8.txt' ]:
                            f, s, cadena = cargar_memoria()
                        else: 
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Gram1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                    else: 
                        
                        convertir_afnd_a_afd(s, f, cadena)
                        time.sleep(5)

                elif opcion == 'E': #MINIMIZA
                    if f == "" or s == "" or cadena == "":
                        if Texto in ['Aut1.txt', 'Aut2.txt', 'Aut3.txt', 'Aut4.txt', 'Aut5.txt', 'Aut6.txt', 'Aut7.txt', 'Aut8.txt' ]:
                            f, s, cadena = cargar_memoria()
                        else: 
                            print( Fore.YELLOW + "NOMBRE INCORRECTO DEL ARCHIVO, FAVOR DE VERIFICAR QUE SEA (Gram1.txt) " + Style.RESET_ALL)
                        time.sleep(5)
                        os.system("cls")
                    else: 
                        sig, fd, valores = read(Texto)
                        Estado_inicial = sig[0]
                        diccionario_transiciones = matriz_to_Dict(valores, sig)
                        estados = conseguir_estados(diccionario_transiciones)
                        minimizacion(sig, estados, Estado_inicial, fd, diccionario_transiciones)
                        time.sleep(5)

                elif opcion == 'F':
                    os.system("cls")
                    print( Fore.BLUE + " \n HA SALIDO DEL PROGRAMA. ¡VUELVA PRONTO!" + Style.RESET_ALL ) 
                    menu_principal2 = False
                else:
                    os.system("cls")
                    print( Fore.RED + " \n OPCION NO VALIDA. INTENTE DE NUEVO!! " + Style.RESET_ALL )   
                    time.sleep(5)

        elif(op == '3'):
            os.system("cls")
            print("HA SALIDO DEL PROGRAMA")
            menu_principal = False
                

