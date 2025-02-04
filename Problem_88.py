def merge(nums1, m, nums2, n):
    while(n != 0):
        nums1[-n] = nums2[-n]
        n = n - 1
    nums1.sort()

if __name__ == "__main__":
    nums1 = [-1,0,0,3,3,3,0,0,0]
    nums2 = [1,2,2]
    merge(nums1, len(nums1), nums2, len(nums2))
    print(nums1)