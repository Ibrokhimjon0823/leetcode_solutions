def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
            nums1[m+i]=nums2[i]
            sorted(nums1[:i])
    for iter_num in range(len(nums1)-1,0,-1):
        for idx in range(iter_num):
            if nums1[idx]>nums1[idx+1]:
                temp = nums1[idx]
                nums1[idx] = nums1[idx+1]
                nums1[idx+1] = temp
