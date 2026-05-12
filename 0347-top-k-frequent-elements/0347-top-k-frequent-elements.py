class Solution(object):
    def topKFrequent(self, nums, k):
        dem=Counter(nums)
        return [num for num, _ in dem.most_common(k)]

        