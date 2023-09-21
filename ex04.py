#
# autores: Cristiano, Michel
#
# Data: 21/09/2023
#
# Dada uma tupla, conte quantas vezes um elemento específico aparece nela. 
# Imprima o número de ocorrências.
# tupla = (10, 20, 30, 40, 50, 10, 10)

tupla = (10, 20, 30, 40, 50, 10, 10)
elemento_procurado = 10
numero_de_ocorrencias = tupla.count(elemento_procurado)
print("O elemento", elemento_procurado, "aparece", numero_de_ocorrencias, "vezes na tupla.")

