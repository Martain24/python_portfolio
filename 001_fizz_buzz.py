# Fizz Buzz
## Imprimir todos los enteros del 1 al 100.
## Si el número es múltiplo de 3 mostramos Fizz.
## Si el número es múltiplo de 5 mostramos Buzz.
## Si el número es múltiplo de 3 y 5 mostramos FizzBuzz.

for number in range(1, 101):
    message = "Fizz" if (number % 3 == 0) else ""
    message += "Buzz" if (number % 5 == 0) else ""
    print(number if message == "" else message)









