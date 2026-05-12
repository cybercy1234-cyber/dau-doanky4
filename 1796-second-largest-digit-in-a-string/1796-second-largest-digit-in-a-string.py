class Solution(object):
    def secondHighest(self, s):
        digits = set()

        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))

        digits = sorted(digits, reverse=True)

        if len(digits) < 2:
            return -1

        return digits[1]
        