
from showcallstack import showcallstack
def stack_overflow():                                   # пример переполнения стека при помощи бесконечной рекурсии
    stack_overflow()
# stack_overflow()                                      # RecursionError: maximum recursion depth exceeded


def recursion(arg):
    if not arg:                                         # базовый случай
        print("Вход в базовый случай")
        print("Возвращение из базового случая")
        return
    else:
        print("Вход в рекурсивный случай")
        recursion(False)
        print("Возвращение из рекурсивного случая")
        return
# recursion(True)
# print()
# recursion(False)


def counter(number):
    if number == 0:                                     # базовый случай
        print("Достигнут базовый случай")
        return
    else:                                               # рекурсивный случай
        counter(number - 1)
        print(number, " возвращается ")
        return
counter(1000)

def factorial(num):
    showcallstack()
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
# factorial(999)