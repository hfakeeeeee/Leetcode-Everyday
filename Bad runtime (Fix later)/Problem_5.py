def check(s):
    if(s == s[::-1]):
        return True
    return False

def longestPalindrome(s):
    s_result = ""
    s_check = ""
    max = 0
    index = 0
    if(s == s[::-1]):
        return s
    while(index != len(s) - 1):
        for i in range(index, len(s)):
            s_check = s_check + s[i]
            if(check(s_check)):
                if(len(s_check) > max):
                    max = len(s_check)
                    s_result = s_check
        s_check = ""
        index = index + 1
            
    return s_result


    
if __name__ == "__main__":
    s = input()
    print(longestPalindrome(s))
