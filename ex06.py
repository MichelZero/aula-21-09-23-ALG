#
# autores: Cristiano, Michel
#
# Data: 21/09/2023
#

# Dada uma lista e uma tupla, crie uma nova lista contendo todos os 
# elementos da lista seguidos pelos elementos da tupla. Imprima a nova lista.
# lista = [1, 2, 3]
# tupla = (4, 5, 6)

lista = [1, 2, 3]
tupla = (4, 5, 6)
nova_lista = lista + list(tupla)
print("Nova lista:", nova_lista)
