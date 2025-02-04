def searchInsert(nums, target):
    if(target not in nums):
        nums.append(target)
        nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) / 2
        mid = int(mid)
        if(nums[mid] == target):
            return mid
        elif(nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target))