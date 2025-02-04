def findMedianSortedArrays(nums1, nums2):
    if(nums1 == [] and nums2 == []):
        return 0
    med = 0.0
    merge = sorted(nums1 + nums2)
    if(len(merge) % 2 == 0):
        mid = len(merge)/2
        med = (merge[int(mid) - 1] + merge[int(mid)]) / 2
    else:
        med = merge[int(len(merge)/2)]
    return med

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    print(findMedianSortedArrays(nums1, nums2))
