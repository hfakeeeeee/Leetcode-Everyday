def maxAscendingSum(nums):
    sum = 0
    longest = 0
    if(len(nums) == 0):
        return 0
    if(len(nums) == 1):
        return sum + nums[0]
    sum = nums[0]
    for i in range(len(nums) - 1):
        if(nums[i] < nums[i + 1]):
            sum += nums[i + 1]
        else:
            if(sum > longest):
                longest = sum
                sum = nums[i + 1]
                continue
            sum = nums[i + 1]
    if(sum > longest):
        longest = sum

    return longest

if __name__ == "__main__":
    nums = [3,6,10,1,8,9,9,8,9]
    print(maxAscendingSum(nums))