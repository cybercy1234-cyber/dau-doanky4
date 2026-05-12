class Solution(object):
    def findClosestNumber(self, nums):
        ans = nums[0]

        for num in nums:

            # gần 0 hơn
            if abs(num) < abs(ans):
                ans = num

            # khoảng cách bằng nhau -> lấy số lớn hơn
            elif abs(num) == abs(ans) and num > ans:
                ans = num

        return ans