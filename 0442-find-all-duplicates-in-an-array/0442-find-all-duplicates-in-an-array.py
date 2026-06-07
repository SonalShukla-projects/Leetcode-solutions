class Solution(object):
    def findDuplicates(self, nums):
        ans=[]
        for num in nums:
            idx=abs(num)-1
            if nums[idx]<0:
                ans.append(abs(num))
            else:
                nums[idx]*=-1
        return ans
sol=Solution()
arr=[4,3,2,7,8,2,3,1]
print(sol.findDuplicates(arr))       