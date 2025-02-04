def isMatch(s, p):
    if(s == p):
        return True
    while(len(s) > len(p)):
        p = p + ' '
    for i in range(len(p)):
        if(s[i] == p[i]):
            continue
        if(s[i] != p[i]):
            if(p[i] == '.' or p[i] == '*'):
                continue
            return False
    return True
        

if __name__ == "__main__":
    s = input()
    p = input()
    if(isMatch(s, p)): print("true")
    else: print("false")