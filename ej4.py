# Base 64 a letras
def decodificar_base64(x):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binarios = ""
    for i in x:
        if i in base64_chars:
            valor_decimal = base64_chars.index(i)
            binario = bin(valor_decimal)[2:]
            while len(binario) < 6:
                binario = '0' + binario
            binarios += binario

    texto = ""
    for i in range(0, len(binarios), 8):
        segmento = binarios[i:i+8]
        if len(segmento) == 8:
            valor_decimal = int(segmento, 2)
            texto += chr(valor_decimal)

    return texto



# Ejemplo 1
p1 = 'Q2FycmP'
print('Palabra 1: ', p1) # Palabra 1:  Q2FycmP
p1_res = decodificar_base64(p1)
print('Resultado letras palabra 1: ', p1_res) # Resultado letras palabra 1:  Carrc


# Ejemplo 2
p2 = 'UGVycmP'
print('Palabra 2: ', p2) # Palabra 2:  UGVycmP
p2_res = decodificar_base64(p2)
print('Resultado letras palabra 2: ', p2_res) # Resultado letras palabra 2:  Perrc