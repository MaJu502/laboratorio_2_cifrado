# Bytes a caracteres
def convertir_binario_letra(x):
    valor_decimal = 0

    for i in range(8):
        valor_decimal += int(x[i]) * (2 ** (len(x) - i - 1))


    letra = chr(valor_decimal)
    return letra

def decodificar_binario(x):
    retorno = ""
    for i in range(0, len(x), 8):
        retorno += convertir_binario_letra(x[i:i+8])
    return retorno



# Ejemplo 1
p1 = '0100001101100001011100100111001001101111'
print('Palabra 1: ', p1) # Palabra 1:  0100001101100001011100100111001001101111
p1_binario = decodificar_binario(p1)
print('Resultado letras palabra 1: ', p1_binario) # Resultado letras palabra 1:  Carro


# Ejemplo 2
p2 = '0101000001100101011100100111001001101111'
print('Palabra 2: ', p2) # Palabra 2:  0101000001100101011100100111001001101111
p2_binario = decodificar_binario(p2)
print('Resultado letras palabra 2: ', p2_binario) # Resultado letras palabra 2:  Perro
