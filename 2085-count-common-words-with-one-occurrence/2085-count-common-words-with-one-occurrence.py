class Solution(object):
    def countWords(self, words1, words2):
        count1 = {}
        count2 = {}

        for word in words1:
            count1[word] = count1.get(word, 0) + 1

        for word in words2:
            count2[word] = count2.get(word, 0) + 1

        ans = 0

        for word in count1:

            if count1[word] == 1 and count2.get(word, 0) == 1:
                ans += 1

        return ans