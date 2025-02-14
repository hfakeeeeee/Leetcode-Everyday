from sortedcontainers import *

def minOperations(nums: list, k: int):
    nums = SortedList(nums)
    a = 0
    while nums[0] < k:
        b = nums.pop(0)
        c = nums.pop(0)
        d = min(b, c) * 2 + max(b, c)
        nums.add(d)
        a += 1
    return a

if __name__ == "__main__":
    nums = [2,11,10,1,3]
    k = 20
    print(minOperations(nums, k))