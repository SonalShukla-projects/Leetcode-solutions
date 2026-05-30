class Solution(object):
    def containsDuplicate(self, nums):
        n=len(nums)
        seen=set()
        duplicate=set()
        found=False
        for i in range(0,n):
            if nums[i] in seen:
                duplicate.add(nums[i])
                found=True
            else:
                seen.add(nums[i])
        if found==True:
            return True
        else:
            return False

s=Solution()
print(s.containsDuplicate([1,2,3,1]))
        