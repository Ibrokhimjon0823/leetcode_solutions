def twoSum(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i]+nums[j] == 9:
                return [i,j]
            else:
                continue
        # else:
        #     continue

print(twoSum([2,1,3,6]))