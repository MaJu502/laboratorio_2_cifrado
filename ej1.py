# Caracteres a bits
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

def codificar_binario(x):
    retorno = ""
    for i in x:
        retorno += convertir_letra_binario(i)
    return retorno

# Ejemplo 1
p1 = 'Carro'
print('Palabra 1: ', p1) # Palabra 1:  Carro
p1_binario = codificar_binario(p1)
print('Resultado binario palabra 1: ', p1_binario) # Resultado binario palabra 1:  0100001101100001011100100111001001101111


# Ejemplo 2
p2 = 'Perro'
print('Palabra 2: ', p2) # Palabra 2:  Perro
p2_binario = codificar_binario(p2)
print('Resultado binario palabra 2: ', p2_binario) # Resultado binario palabra 2:  0101000001100101011100100111001001101111