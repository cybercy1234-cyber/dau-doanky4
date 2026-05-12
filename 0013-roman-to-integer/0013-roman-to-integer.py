class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0   # giá trị ký tự trước đó

        for ch in s:
            curr = roman[ch]
            if curr > prev:
                # Trường hợp trừ: IV, IX, XL, XC, CD, CM
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr

        return total

        