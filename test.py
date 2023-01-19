#я ебал#

from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.GREEN)
wat = input( "Что делаем? (+, -): ")
a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

if wat == "+":
	c = a + b
	print("Результат: " + str(c))
elif wat == "-":
	c = a - b
	print("Результат: " + str(c))
else:
	print("Выбрана неверная операция!")
input()