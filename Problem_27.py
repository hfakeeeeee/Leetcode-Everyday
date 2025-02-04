def removeElement(nums, val):
    not_equal = []
    for i in nums:
        if(i != val):
            not_equal.append(i)
    nums[:] = not_equal
    return len(not_equal)

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    k = removeElement(nums, val)
    print(k) 
    print(nums)