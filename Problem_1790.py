def areAlmostEqual(s1, s2):
    if(s1 == s2):
        return True
    diff = 0
    s = set()
    for i in range(len(s1)):
        if(diff > 2):
            return False
        if(s1[i] != s2[i]):
            s.add(s1[i])
            s.add(s2[i])
            diff += 1
    return True if len(s) == 2 and diff == 2 else False

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(areAlmostEqual(s1, s2))
