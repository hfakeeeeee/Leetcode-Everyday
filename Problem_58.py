def lengthOfLastWord(s):
    count = 0
    char = False
    if(len(s) == 1):
        return 1
    for i in range(len(s) -1, -1, -1):
        if(s[i].isspace() and char == True):
            return count
        if(s[i].isalpha()):
            char = True
            count += 1
    return count

if __name__ == "__main__":
    s = input()
    print(lengthOfLastWord(s))
