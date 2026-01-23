
def imprimir_grilla(grilla):
    for ii in grilla:
        print(ii)

def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []
    cantidad_letras = 5
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] # True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            letras_verificadas.append(palabra_ingresada[i])
    
    return letras_verificadas

verificador_palabra('holas', 'calor')


# ==============================

secreto = "palos"
victoria = False
intentos = 2
lista_de_intentos = []


# ==============================
for i in range(intentos):
    palabra_intento = input("Ingrese una palabra:\t")
    lista_de_intentos.append(verificador_palabra(palabra_intento, secreto))
    imprimir_grilla(lista_de_intentos)
    if secreto == palabra_intento:
        victoria = True
        break
    intentos = intentos - 1
# ==============================

if victoria == True:
    print("Ganaste!!")
else:
    print("Perdiste :(")
