class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
        return nums


s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))
        