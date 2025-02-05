def isPalindrome(s: str):
    result = ""
    for i in s:
        if(i.isalpha()):
            result += i
    result = result.lower()
    if(result == result[::-1]):
        return True
    return False

if __name__ == "__main__":
    s = input()
    print(isPalindrome(s))