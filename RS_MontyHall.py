import numpy as np
import random 

def sort_doors():
	lista = ['goat', 'goat', 'car']
	random.shuffle(lista) #Se desorganiza la lista
	return lista

def choose_door():
	return int(np.random.choice(3,1)) #Se escoje un numero al azar entre 0 y 2
	

def reveal_door(lista, choice):
	for i in range(len(lista)):
		if(i != choice):
			if lista[i] == 'goat':
				lista[i] = "GOAT_MONTY"
				break
	return lista

def finish_game(lista, choice, change):
	if not change:
		return lista[choice]
	else:
		for i in range(len(lista)):
			if i!=choice and lista[i]!='GOAT_MONTY':
				return lista[i] #Se escoge la opcion diferente

cambia = 0
no_cambia = 0
#Escenario en el que cambia de seleccion
for i in range(100):
	lista_t = sort_doors()
	puerta = choose_door()
	lista_t = reveal_door(lista_t, puerta)
	ans = finish_game(lista_t, puerta, True)
	if ans == 'car':
		cambia += 1

#Escenario en el que no cambia
for i in range(100):
	lista_f = sort_doors()
	puerta = choose_door()
	lista_f = reveal_door(lista_t, puerta)
	ans = finish_game(lista_t, puerta, False)
	if ans == 'car':
		no_cambia += 1

print("La probabilidad de obtener el premio cuando no hubo cambio es: "+ str(no_cambia/100.0))
print("La probabilidad de obtener el premio cuando si hubo cambio es: "+ str(cambia/100.0))
