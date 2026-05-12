class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        
        x=[]
        for i in range (len(nums)):
            count=0
            
            for j in range (len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            x.append(count)
            
        return x