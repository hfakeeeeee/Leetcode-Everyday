import string

def isPalindrome(s: str):
    s = "".join(s.split())
    s = ''.join(ch for ch in s if ch not in string.punctuation)
    s = s.lower()
    print(s)
    if(s == s[::-1]):
        return True
    return False

if __name__ == "__main__":
    s = input()
    print(isPalindrome(s))