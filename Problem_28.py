def strStr(haystack, needle):
    k = len(needle)
    if(not haystack):
        return -1
    elif(not needle):
        return 0
    for i in range(len(haystack)):
        h = 0
        if(i + k <= len(haystack)):
            for t in range(i, i + k):
                if(haystack[t] == needle[h]):
                    h += 1
            if(h == k):
                return i
    return -1


if __name__ == "__main__":
    haystack = input()
    needle = input()
    print(strStr(haystack, needle))
