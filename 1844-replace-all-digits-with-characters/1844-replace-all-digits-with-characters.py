class Solution(object):
    def replaceDigits(self, s):
        s = list(s)

        for i in range(1, len(s), 2):

            ch = s[i - 1]
            num = int(s[i])

            s[i] = chr(ord(ch) + num)

        return "".join(s)