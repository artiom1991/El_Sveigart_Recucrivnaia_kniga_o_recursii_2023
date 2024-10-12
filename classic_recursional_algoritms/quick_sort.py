def quicksort(items, left=None, right=None):
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
    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)

myList = [0, 7, 6, 3, 1, 2, 5, 4]
# myList = [i for i in range(0, 1000)]
print(myList)
quicksort(myList)                   # меняет исходный массив
print(myList)

print("_________________________")

def quicksort_grokaem(array):                           # сортировка из книги грокаем алгоритмы
    if len(array) < 2:  # базовый случай
        return array
    else:               # рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_grokaem(less) + [pivot] + quicksort_grokaem(greater)

myList = [0, 7, 6, 3, 1, 2, 5, 4]
myList = [i for i in range(0, 1001)]
print(myList)
print(quicksort_grokaem(myList))        # не меняет исходный массив, а возвращает новый
print(myList)







