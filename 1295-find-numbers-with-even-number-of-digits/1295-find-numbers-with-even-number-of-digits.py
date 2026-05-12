class Solution(object):
    def findNumbers(self, nums):
        
        count2=0
        for i in nums:
            i=str(i)
            if (len(i)%2==0):
                count2+=1
        return count2