class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        return len(set(count.values())) == 1
        