def convert(s, numRows):
    if(len(s) <= 1 or numRows == 1):
        return s
    a = [[0 for x in range(1000)] for y in range(numRows)] 
    k = 0
    i = 0
    flag = False
    while(not flag):
        for j in range(0, numRows):
            if(k != len(s)):
                a[j][i] = s[k]
                k = k + 1
            else: 
                flag = True
                break
        i = i + 1
        for t in range(j - 1, 0, -1):
            if(k != len(s)):
                a[t][i] = s[k]
                i = i + 1
                k = k + 1
            else:
                flag = True
                break
    
    s = ""
    for i in range(numRows):
        for j in range(1000):
            if(a[i][j] != 0):
                s = s + a[i][j]
    
    return s

if __name__ == "__main__":
    s = input()
    numrows = input()
    print(convert(s, int(numrows)))