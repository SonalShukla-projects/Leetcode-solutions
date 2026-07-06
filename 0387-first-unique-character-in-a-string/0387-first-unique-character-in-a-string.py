class Solution(object):
    def firstUniqChar(self, s):
        count=defaultdict(int) #char-.count
        for c in s:
            count[c]+=1
        for i,c in enumerate(s):
            if count[c]==1:
                return i
        return -1
            
    
s="leetcode"
sol=Solution()
print(sol.firstUniqChar(s))