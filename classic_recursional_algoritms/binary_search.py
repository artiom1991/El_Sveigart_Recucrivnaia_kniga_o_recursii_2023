def binary_search(number_list, number, left=0, right=None):
    if right is None:
        right = len(number_list) - 1
    if left <= right:
        mid = (left + right) // 2
        if number == number_list[mid]:
            return mid
        elif number < number_list[mid]:
            return binary_search(number_list, number, left, mid - 1)
        else:
            return binary_search(number_list, number, mid + 1, right)
    return None


number_list = [1, 4, 8, 11, 13, 16, 19, 19]
result = binary_search(number_list, 13)
print(result)