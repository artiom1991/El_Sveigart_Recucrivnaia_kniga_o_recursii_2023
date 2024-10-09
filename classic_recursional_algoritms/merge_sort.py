import math

def mergeSort(items):
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

myList = [2, 9, 8, 5, 3, 4, 7, 6]
myList = mergeSort(myList)
print(myList)
