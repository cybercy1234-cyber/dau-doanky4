class Solution(object):
    def countHillValley(self, nums):
        arr = [nums[0]]

        # loại bỏ phần tử trùng liên tiếp
        for num in nums[1:]:

            if num != arr[-1]:
                arr.append(num)

        count = 0

        # đếm đồi và thung lũng
        for i in range(1, len(arr) - 1):

            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1

            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1

        return count