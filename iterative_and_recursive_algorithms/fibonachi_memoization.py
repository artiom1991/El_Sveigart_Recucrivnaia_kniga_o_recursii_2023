import functools

def my_recursional_fibonachi(number, number_list=None):         # использование аккумуляции при помощи number_list которая передается в новый вызов функции
    if number_list is None:
        number_list = [0, 1]
    if len(number_list) < number:
        last_item = number_list[-1] + number_list[-2]
        number_list.append(last_item)
        return my_recursional_fibonachi(number, number_list)
    return number_list
# my_recursional = my_recursional_fibonachi(1001)
# print(my_recursional)



fibonacciCache = {}
def fibonacci(nthNumber, indent=0):
    global fibonacciCache
    indentation = '.' * indent
    print(indentation + 'fibonacci(%s) called.' % (nthNumber))
    if nthNumber in fibonacciCache:
        print(indentation + 'Returning memoized result: %s' % (fibonacciCache[nthNumber]))
        return fibonacciCache[nthNumber]
    if nthNumber == 1 or nthNumber == 2:
        print(indentation + 'Base case fibonacci(%s) returning 1.' % (nthNumber))
        fibonacciCache[nthNumber] = 1
        return 1
    else:
        print(indentation + 'Calling fibonacci(%s) (nthNumber - 1).' % (nthNumber - 1))
        result = fibonacci(nthNumber - 1, indent + 1)
        print(indentation + 'Calling fibonacci(%s) (nthNumber - 2).' % (nthNumber - 2))
        result = result + fibonacci(nthNumber - 2, indent + 1)
        print('Call to fibonacci(%s) returning %s.' % (nthNumber, result))
        fibonacciCache[nthNumber] = result
        return result

# fib_1 = fibonacci(10)
# print(fib_1)


@functools.lru_cache()
def fibonacci(nthNumber):
    print('fibonacci(%s) called.' % (nthNumber))
    if nthNumber == 1 or nthNumber == 2:
        # БАЗОВЫЙ СЛУЧАЙ
        print('Call to fibonacci(%s) returning 1.' % (nthNumber))
        return 1
    else:
        # РЕКУРСИВНЫЙ СЛУЧАЙ
        print('Calling fibonacci(%s) (nthNumber - 1).' % (nthNumber - 1))
        result = fibonacci(nthNumber - 1)
        print('Calling fibonacci(%s) (nthNumber - 2).' % (nthNumber - 2))
        result = result + fibonacci(nthNumber - 2)
        print('Call to fibonacci(%s) returning %s.' % (nthNumber, result))
        return result

# fib_2 = fibonacci(1234)
# print(fib_2)


@functools.lru_cache()
def fibonacci_22(number):
    if number < 2:
        print(1)
        return 1
    else:
        return fibonacci_22(number - 1) + fibonacci_22(number - 2)
# print(fibonacci_22(998))
