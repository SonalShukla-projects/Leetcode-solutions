class Solution(object):
    def findDuplicate(self, nums):
        n=len(nums)
        seen=set()
        duplicate=set()
        for i in range(0,n):
            if nums[i] in seen:
                duplicate.add(nums[i])
            else:
                seen.add(nums[i])
        for x in duplicate:
            return x

s=Solution()
print(s.findDuplicate([1,3,4,2,2]))