

def book_is_palindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        return True
    else:
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and book_is_palindrome(middle)

def my_is_palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return my_is_palindrome(string[1:-1])
        return False

s = "roar"
print(my_is_palindrome(s))
