def removeDuplicates(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
        else: continue
    unique_lenght = len(unique)
    nums[:] = unique
    return unique_lenght

if __name__ == "__main__":
    nums = [1, 1, 2]
    expectedNums = [1, 2, 0]
    k = removeDuplicates(nums)
    
    print(k) 
    print(nums)
            