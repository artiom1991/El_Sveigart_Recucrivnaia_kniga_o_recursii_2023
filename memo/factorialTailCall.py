

def factorial(number, accum=1):             # оптимизация через вызов хвостовой рекурсии, но она не работает в Python
    if number == 1:
        return accum
    else:
        return factorial(number - 1, accum * number)

print(factorial(1001))
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
# Переполнение стека происходит, потому что Python не оптимизирует хвостовую рекурсию.
# Несмотря на то, что функция написана с использованием хвостовой рекурсии, каждый рекурсивный
# вызов все еще добавляется в стек вызовов. Когда количество вызовов превышает ограничение стека,
# возникает ошибка RecursionError: maximum recursion depth exceeded.