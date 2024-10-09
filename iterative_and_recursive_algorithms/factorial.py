# Чем плох рекурсивный алгоритм вычисления факториала ?
# Если вы захотите вычислить факториал числа 1001, вам придется вызвать рекурсивную функцию factorial() 1001 раз. Однако ваша программа, скорее всего,
# аварийно завершится в связи с переполнением стека, потому что такое количество вызовов функций без возврата, вероятно, превысит максимальный размер стека
# вызовов интерпретатора. Никогда не используйте рекурсивный алгоритм вычисления факториала в реальном коде — это ужасно.


# Итеративный алгоритм вычисления факториала
def iterational_factorial(number):              # Итеративные алгоритмы всегда используют цикл
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product
iterational = iterational_factorial(5)
print(iterational)


# Рекурсивный алгоритм вычисления факториала
def recursional_factorial(number):
    if number == 1:
        return 1
    else:
        return number * recursional_factorial(number - 1)

# recursional = recursional_factorial(999)
# print(recursional)


def iterative_factorial(number):                                # итеративный факториал с реализацией импровизированного стека вызовов
    callStack = []
    callStack.append({"returnAddr": "start", "number": number})
    returnValue = None
    while len(callStack) > 0:
        number = callStack[-1]["number"]
        returnAddr = callStack[-1]["returnAddr"]
        print(number, returnAddr)
        if returnAddr == "start":
            if number == 1:
                returnValue = 1
                callStack.pop()
                continue                                                         # continue ???
            else:
                callStack[-1]["returnAddr"] = "after recursive call"
                callStack.append({"returnAddr": "start", "number": number - 1})
                continue
        elif returnAddr == "after recursive call":
            returnValue = number * returnValue                                              # returnValue *= number
            callStack.pop()
            continue
    return returnValue

# value = iterative_factorial(1234)
# print(value)