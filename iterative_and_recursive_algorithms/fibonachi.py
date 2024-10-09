# Чем плох рекурсивный алгоритм вычисления чисел Фибоначчи


def iterational_fibonachi(number):
    a, b = 1, 1
    print("a = %s, b = %s " % (a, b))
    for i in range(1, number):
        a, b = b, a + b
        print("a = %s, b = %s" % (a, b))
    return a

iterational = iterational_fibonachi(12)



def recursional_fibonachi(number):
    # плохая функция так как в ней создается дублирование рассчетов   result = fibonachi_1(number - 1) + fibonachi_1(number - 2) создается две ветки вычислений
    print("fibonachi(%s) called." % (number))
    if number == 1 or number == 2:
        print("call to fibonachi(%s) returning 1." % (number))
        return 1
    else:
        print("call to fibonachi(%s) and fibonachi(%s)." % (number - 1, number - 2))
        result = recursional_fibonachi(number - 1) + recursional_fibonachi(number - 2)
        print("call to fibonachi(%s) returns %s." % (number, result))
        return result

recursional = recursional_fibonachi(12)
