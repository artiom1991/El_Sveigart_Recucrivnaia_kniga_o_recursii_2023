import time

# По сути, каждый рекурсивный вызов сокращает размер проблемы вдвое. Именно
# поэтому наш рекурсивный алгоритм вычисления экспоненты работает быстрее,
# чем его итеративная версия. Вычисление 31000 итеративным способом предполагает
# выполнение 1000 операций умножения, в то время как рекурсивному алгоритму
# для этого достаточно 23 операций умножения и деления. При запуске кода Python
# в профилировщике производительности 100 000-кратное итеративное вычисление
# 31000 занимает 10,633 секунды, а рекурсивное — всего 0,406 секунды. Это весьма
# впечатляющая разница!


def iterative_power(number, power):
    res = 1
    for i in range(power):
        res *= number
    return res
iterative = iterative_power(2,10)
print(iterative)

def recursional_power(num, pow):
    if pow == 1:
        return num
    else:
        return num * recursional_power(num, pow - 1)
recursional = recursional_power(2,10)
print(recursional)

def exponentByRecursion(a, n):
    if n == 1:
        return a                                            # 2
    elif n % 2 == 0:
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        result = exponentByRecursion(a, n // 2)
        return result * result * a
recursive_exponent = exponentByRecursion(2, 10)
print(recursive_exponent)

def exponentWithPowerRule(a, n):
    opStack = []
    while n > 1:
        if n % 2 == 0:
            opStack.append('square')
            n = n // 2
        elif n % 2 == 1:
            n -= 1
            opStack.append("multiply")
    result = a
    while opStack:
        op = opStack.pop()
        if op == "multiply":
            result *= a
        elif op == "square":
            result *= result
    return result
iterative_exponent = exponentWithPowerRule(2, 10)
print(iterative_exponent)