#
# autores: Cristiano, Michel
#
# Data: 21/09/2023
#
# Dada uma tupla, verifique se um elemento está presente nela. 
# Imprima se o elemento foi encontrado ou não.
# tupla = (10, 20, 30, 40, 50)


tupla = (10, 20, 30, 40, 50)
elemento_procurado = 30
if elemento_procurado in tupla:
    print("O elemento", elemento_procurado, "foi encontrado na tupla.")
else:
    print("O elemento", elemento_procurado, "não foi encontrado na tupla.")
