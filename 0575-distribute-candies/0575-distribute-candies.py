class Solution(object):
    def distributeCandies(self, candyType):
        kinds = len(set(candyType))
        return min(kinds, len(candyType) // 2)
        