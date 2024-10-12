import math

def mergeSort1(items):
    print('.....mergeSort() called on:', items)
    if len(items) == 0 or len(items) == 1:
        return items
    iMiddle = math.floor(len(items) / 2)
    print('................Split into:', items[:iMiddle], 'and', items[iMiddle:])
    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])
    sortedResult = []
    iLeft = 0
    iRight = 0
    while iLeft < len(left) and iRight < len(right):
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1
    sortedResult.extend(left[iLeft:])
    sortedResult.extend(right[iRight:])
    print('The two halves merged into:', sortedResult)
    return sortedResult

def mergeSort(items):
    if len(items) < 2:
        return items
    iMiddle = len(items) // 2
    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])
    sortedResult = []
    iLeft = 0
    iRight = 0
    while iLeft < len(left) and iRight < len(right):
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1
    sortedResult.extend(left[iLeft:])
    sortedResult.extend(right[iRight:])
    return sortedResult

myList = [2, 9, 8, 5, 3, 4, 6, 7]
myList1 = mergeSort(myList)
print(myList)
print(myList1)