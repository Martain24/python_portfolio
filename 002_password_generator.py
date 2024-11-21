# Password generator
## Preguntamos al usuario cuantas letras quiere que tenga la contraseña
## Cuantos símbolos
## Cuantos números
## Generamos contraseña

import string 
import random

alphabet_list = list(string.ascii_uppercase + string.ascii_lowercase)
simbolos_list = list("#@_%&=+-[]^*")
numeros_list = list("123456789")

def ask_for_number(input_str):
    while True:
        try:
            number = int(input(input_str))
            break
        except:
            print("No has escrito un número válido.")
    return number


num_letras = ask_for_number("¿Cuántas letras quieres que tenga tu contraseña? ")
num_simbolos = ask_for_number("¿Cuántos símbolos quieres que tenga tu contraseña? ")
num_numeros = ask_for_number("¿Cuántos números quieres que tenga tu contraseña? ")
        
        
letras = random.choices(alphabet_list, k=num_letras)
simbolos = random.choices(simbolos_list, k=num_simbolos)
numeros = random.choices(numeros_list, k=num_numeros)


list_password = letras + simbolos + numeros
# random.shuffle(list_password)
indexes = [i for i in range(len(list_password))]

password = ""

while True:
    random_index = random.choice(indexes)
    password += list_password[random_index]
    indexes.remove(random_index)
    if len(indexes) == 0:
        break

print(password)