class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)
        return answer