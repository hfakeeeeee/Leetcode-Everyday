def lengthOfLongestSubstring(s): 
    if(len(s) == 1):
        return 1
    max_len = 0
    unique = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if(s[j] not in unique):
                unique.append(s[j])
            else:
                if(len(unique) > max_len):
                    max_len = len(unique)
                    unique = []
                    break
                else:
                    unique = []
                    break
    return max_len

if __name__ == "__main__":
    s = ""
    s = input(s)
    print(lengthOfLongestSubstring(s))