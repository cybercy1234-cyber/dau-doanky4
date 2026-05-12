class Solution(object):
    def moveZeroes(self, nums):
        k = 0

        # đưa các số khác 0 lên đầu
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # điền 0 vào phần còn lại
        for i in range(k, len(nums)):
            nums[i] = 0
        