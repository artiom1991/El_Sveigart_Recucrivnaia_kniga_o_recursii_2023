def iterational_binary_search(number_list, number): # итеративный пример из книги грокаем алгоритмы
    low = 0
    high = len(number_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = number_list[mid]
        if guess == number:
            return mid
        elif guess > number:
            high = mid - 1
        else:
            low = mid + 1
    return None

def recursional_binary_search(needle, haystack, left=None, right=None): # пример из книги рекурсивная книга о рекурсии
    if left is None:
        left = 0
    if right is None:
        right = len(haystack) - 1
    if left > right:
        return None
    mid = (left + right) // 2
    if needle == haystack[mid]:
        return mid
    elif needle < haystack[mid]:
        return recursional_binary_search(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]:
        return recursional_binary_search(needle, haystack, mid + 1, right)


def new_binary_search(number_list, number, left=0, right=None): # в этом примере я убрал лишнюю проверку
    if right is None:
        right = len(number_list) - 1
    if left <= right:
        mid = (left + right) // 2
        if number == number_list[mid]:
            return mid
        elif number < number_list[mid]:
            return new_binary_search(number_list,number, left, mid - 1)
        else:
            return new_binary_search(number_list,number, mid + 1, right)
    return None


number_list = [1, 4, 8, 11, 13, 16, 19, 19]

first = iterational_binary_search(number_list, 13)
second = recursional_binary_search(13, number_list)
third = new_binary_search(number_list, 13)

print(first, second, third)



