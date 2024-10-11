# Чем плох рекурсивный алгоритм вычисления чисел Фибоначчи

def iterational_fibonachi(number):
    fib_list = [0, 1]
    for i in range(1, number):
        new_number = fib_list[-1] + fib_list[-2]
        fib_list.append(new_number)
    return fib_list


# iterational = iterational_fibonachi(12)
# print(iterational)


def recursional_fibonachi(number):
    if number == 1 or number == 2:
        return [1]
    else:
        return recursional_fibonachi(number - 1) + recursional_fibonachi(number - 2)


# recursional = recursional_fibonachi(17)
# print("Число вызовов функции: ", len(recursional))
# каждый рекурсивный вызов функции был добавлен в список вызовов всех вызовов
# в конечном итоге при передаче параметра 10, было осуществено 55 вызовов
# это произошло изза множества повторных вычислений чисел фибоначи
# Этот алгоритм можно улучшить при помощи мемоизации или аккумулятора!


def recursional_fibonachi(number, acc=None):
    if acc == None:
        acc = [0, 1]
    if number == 1:
        return acc
    else:
        new_value = acc[-1] + acc[-2]
        acc.append(new_value)
        return recursional_fibonachi(number - 1, acc)


recursional = recursional_fibonachi(10)
print(recursional)