class Solution(object):
    def moveZeroes(self, nums):
        nozero = []

        for i in range(len(nums)):
            if nums[i] != 0:
                nozero.append(nums[i])

        count = len(nums) - len(nozero)

        for i in range(count):
            nozero.append(0)

        for i in range(len(nums)):
            nums[i] = nozero[i]


nums = [0,1,0,3,12]

s = Solution()
s.moveZeroes(nums)

print(nums)