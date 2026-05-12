class Solution(object):
    from collections import defaultdict 
    def groupAnagrams(self, strs):
        a=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            a[key].append(s)            
        return list(a.values())
        
       
            