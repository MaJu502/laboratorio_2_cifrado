# Cadena a Base 64
def convertir_letra_binario(x):
    a = ord(x)

    binario = ''
    while a > 0:
        residuo = a % 2
        binario = str(residuo) + binario
        a = a // 2
    temp = 8 - len(binario)

    retorno = ''
    for i in range(temp):
        retorno = retorno + '0'
    retorno = retorno + binario
    return retorno

def codificar_base64(x):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binarios = ""
    for i in x:
        binarios += convertir_letra_binario(i)

    temp = []
    for i in range(0, len(binarios), 6):
        segmento = binarios[i:i+6]
        if len(segmento) < 6:
            resultado_temp = 6 - len(segmento)
            retorno = ''
            for i in range(resultado_temp):
                retorno = retorno + '0'
            retorno = retorno + segmento
            segmento = retorno
        temp.append(segmento)

    resultado = [base64[int(seg, 2)] for seg in temp]
    return ''.join(resultado)

# Ejemplo 1
p1 = 'Carro'
print('Palabra 1: ', p1) # Palabra 1:  Carro
p1_res = codificar_base64(p1)
print('Resultado letras palabra 1: ', p1_res) # Resultado letras palabra 1:  Q2FycmP


# Ejemplo 2
p2 = 'Perro'
print('Palabra 2: ', p2) # Palabra 2:  Perro
p2_res = codificar_base64(p2)
print('Resultado letras palabra 2: ', p2_res) # Resultado letras palabra 2:  UGVycmP