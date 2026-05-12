class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
    
        for c in t:
            result += ord(c)
            
        for c in s:
            result -= ord(c)
            
        return chr(result)
            