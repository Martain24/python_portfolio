import string
import random

abecedario = string.ascii_lowercase + string.ascii_uppercase
simbolos = "#@*%"
numeros = "0123456789"

def ask_for_number(question):
    while True:
        try:
            numero = int(input(question))
            break
        except:
            print("No has escrito un entero válido.")
    
    return numero

num_letras = ask_for_number("¿Cuántas letras quieres que tenga la contraseña? ")
num_simbolos = ask_for_number("¿Cuántos símbolos quieres que tenga la contraseña? ")
num_numeros = ask_for_number("¿Cuántos números quieres que tenga la contraseña? ")

letras_password = random.choices(abecedario, k=num_letras)
simbolos_password = random.choices(simbolos, k=num_simbolos)
numeros_password = random.choices(numeros, k=num_numeros)

list_password = letras_password + simbolos_password + numeros_password
password = ""

while len(list_password) > 0:
    random_element = random.choice(list_password)
    password += random_element
    list_password.remove(random_element)

print(f"Tu contraseña es: {password}")



