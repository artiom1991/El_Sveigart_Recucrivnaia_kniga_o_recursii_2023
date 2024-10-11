
def book_reverse_string(theString):
    print(theString)
    if len(theString) == 0 or len(theString) == 1:
        return theString
    else:
        head = theString[0]
        tail = theString[1:]
        return book_reverse_string(tail) + head

def my_reverse_string(inString):
    print(inString)
    if len(inString) < 2:
        return inString
    else:
        return inString[-1] + my_reverse_string(inString[:-1])


s = "string"
print(book_reverse_string(s))
print("_____________________")
print(my_reverse_string(s))
