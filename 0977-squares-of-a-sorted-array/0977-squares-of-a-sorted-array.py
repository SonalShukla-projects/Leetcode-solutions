class Solution(object):
    def sortedSquares(self, nums):
       res=[]
       l=0
       r=len(nums) -1

       while l<=r:
        if (nums[l] * nums[l]) > (nums[r] * nums[r]):
            res.append(nums[l]*nums[l])
            l+=1
        else:
            res.append(nums[r] * nums[r])
            r-=1
        
       return res[::-1]

s=Solution()
n=[-4,-1,0,3,10]
print(s.sortedSquares(n))
