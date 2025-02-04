def searchRange(nums, target):
    def Binary_search(nums, target, isLeft):
        left = 0
        right = len(nums) - 1
        index = -1

        while(left <= right):
            mid = (left + right) // 2
            if(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1
            else:
                index = mid
                if(isLeft):
                    right = mid - 1
                else:
                    left = mid + 1
        return index
    
    left = Binary_search(nums, target, True)
    right = Binary_search(nums, target, False)
    return [left, right]

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = input()
    print(searchRange(nums, int(target)))
