import time

def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1
    print('\nquicksort() called on this range:', items[left:right + 1])
    print('................The full list is:', items)
    if right <= left:
        return
    i = left
    pivotValue = items[right]
    print('....................The pivot is:', pivotValue)
    for j in range(left, right):
        if items[j] <= pivotValue:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[right] = items[right], items[i]
    print('....After swapping, the range is:', items[left:right + 1])
    print('Recursively calling quicksort on:', items[left:i], 'and', items[i + 1:right + 1])
    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)

def quicksort_2_0(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1
    if right <= left:
        return
    i = left
    pivotValue = items[right]
    for j in range(left, right):
        if items[j] <= pivotValue:
            items[i], items[j] = items[j], items[i]
            i += 1
    items[i], items[right] = items[right], items[i]
    quicksort_2_0(items, left, i - 1)
    quicksort_2_0(items, i + 1, right)


def quicksort_grokaem(array):                           # сортировка из книги грокаем алгоритмы
    if len(array) < 2:  # базовый случай
        return array
    else:               # рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_grokaem(less) + [pivot] + quicksort_grokaem(greater)

myList_1 = [0, 7, 6, 3, 1, 2, 5, 4]
print(quicksort(myList_1))
myList_2 = [0, 7, 6, 3, 1, 2, 5, 4]
print("____________грокаем сортировку___________")
print(quicksort_grokaem(myList_2))

