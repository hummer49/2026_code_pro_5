
def imprimir_lista(lista):
    for ii in lista:
        for jj in ii:
            print(jj, end="\t")
        print(end="\n"*2)

def verificar_palabra(palabra_objetivo, palabra_ingresada):
    if len(palabra_objetivo) != len(palabra_ingresada):
        print("error")
        return # raise error
    if palabra_objetivo == palabra_ingresada:
        return [f"[{a}]" for a in palabra_ingresada]
    palabra_verificada = []
    for ii in range(len(palabra_objetivo)):
        if palabra_objetivo[ii] == palabra_ingresada[ii]:
            palabra_verificada.append(f'[{palabra_ingresada[ii]}]')
        elif palabra_ingresada[ii] in palabra_objetivo:
            palabra_verificada.append(f'({palabra_ingresada[ii]})')
        else:
            palabra_verificada.append(f'{palabra_ingresada[ii]}')
    return(palabra_verificada)

def juego():
    # SETUP
    secreto = "hacer" # placeholder
    cantidad_letras = 5
    intentos = 5
    victoria = False
    lista_palabras = []
    while victoria == False and intentos > 0:
        print(f"\nQuedan {intentos} intentos\n")
        # pedir la palabra al usuario
        palabra_ingresada = input(f"Introduzca una palabra de {cantidad_letras} letras: ")
        # verificamos la palabra ingresada
        lista_palabras.append(verificar_palabra(secreto, palabra_ingresada))
        # Mostramos la lista de palabras
        imprimir_lista(lista_palabras)
        # verificamos si el jugador gano
        if secreto == palabra_ingresada:
            victoria = True
            break # por seguridad
        intentos-=1
    print("Ganaste" if victoria==True else "Perdiste")
    print(f"Te quedaron {intentos} intetos")
    


# p0 = verificar_palabra("hacer", "parte")
# p1 = verificar_palabra("hacer", "madre")
# p2 = verificar_palabra("hacer", "nacer")
# p3 = verificar_palabra("hacer", "hacer")

# imprimir_lista([p0,p1,p2, p3])

juego()
