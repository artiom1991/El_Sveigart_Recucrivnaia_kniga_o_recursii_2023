def is_palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        return False

s = "Довод"
print(is_palindrome(s))
