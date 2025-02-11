def removeOccurrences(s, part):
    while part in s:
        s = s[:s.index(part)] + s[s.index(part) + len(part):]
    return s

if __name__ == "__main__":
    s = input()
    part = input()
    print(removeOccurrences(s, part))

