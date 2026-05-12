class Solution(object):
    def distributeCandies(self, candies, num_people):
        
        res = [0] * num_people
        i = 0

        while candies > 0:
            give = i + 1
            res[i % num_people] += min(give, candies)
            candies -= give
            i += 1

        return res
            