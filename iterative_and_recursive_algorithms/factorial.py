# Итеративный алгоритм вычисления факториала. Он всегда используют цикл
def iterational_factorial(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product
# iterational = iterational_factorial(10)
# print(iterational)


# Рекурсивный алгоритм вычисления факториала
def recursional_factorial(number):
    if number == 1:
        return 1
    else:
        return number * recursional_factorial(number - 1)

# recursional = recursional_factorial(10)
# recursional = recursional_factorial(1000)
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
# print(recursional)


# Итеративный алгоритм с имплементацией своего стека вызовов
def iterative_factorial(number):
    callStack = []                                                      # стековая структура
    callStack.append({"returnAddr": "start", "number": number})         # добавление кадра
    returnValue = None
    while len(callStack) > 0:                                           # цикл отрабатывает до тех пор пока очередь стека не пуста
        number = callStack[-1]["number"]
        returnAddr = callStack[-1]["returnAddr"]
        print(number, returnAddr)
        if returnAddr == "start":                                       # блок добавления кадров в стек
            if number == 1:
                returnValue = 1
                callStack.pop()
                continue
            else:
                callStack[-1]["returnAddr"] = "after recursive call"
                callStack.append({"returnAddr": "start", "number": number - 1})
                continue
        elif returnAddr == "after recursive call":                                          # блок извлечения кадров из стека
            returnValue = number * returnValue
            callStack.pop()
            continue
    return returnValue

value = iterative_factorial(1559)
print(value)