def clearDigits(s: str):
    result = ""
    for i in range(len(s)):
        if(s[i].isalpha()):
            result += s[i]
        elif(s[i].isdigit()):
            result = result[:-1]
    return result

if __name__ == "__main__":
    s = input()
    print(clearDigits(s))