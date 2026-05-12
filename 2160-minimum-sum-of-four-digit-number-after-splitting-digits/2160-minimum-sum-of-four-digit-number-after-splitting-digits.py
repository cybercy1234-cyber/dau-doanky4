class Solution(object):
    def minimumSum(self, num):
        digits = sorted(str(num))

        new1 = digits[0] + digits[2]
        new2 = digits[1] + digits[3]

        return int(new1) + int(new2)
        