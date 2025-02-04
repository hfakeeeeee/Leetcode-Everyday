def isValid(s):
    check = []
    for i in range(len(s)):
        if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
            check.append(s[i])
        if(s[i] == ")" or s[i] == "]" or s[i] == "}"):
            if(not check):
                return False
            elif(s[i] == ")" and check[-1] != "("):
                return False
            elif(s[i] == "]" and check[-1] != "["):
                return False
            elif(s[i] == "}" and check[-1] != "{"):
                return False
            else:
                check.pop()
    if(len(check) > 0):
        return False
    return True

if __name__ == "__main__":
    s = input()
    print(isValid(s))
