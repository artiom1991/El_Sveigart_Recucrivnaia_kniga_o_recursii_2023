

def sum_numbers_in_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)

my_list = [1, 5, 10, 50, 100]
my_list = sum_numbers_in_list(my_list)
print(my_list)
# print(sum([i for i in range(1000)])) # RecursionError: maximum recursion depth exceeded

