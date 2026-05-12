class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        zeros = arr.count(0)
        
        i = n - 1
        j = n + zeros - 1  # vị trí sau khi nhân đôi
        
        # duyệt ngược
        while i < j:
            if j < n:
                arr[j] = arr[i]
            
            # nếu là 0 thì ghi thêm 1 lần nữa
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            
            i -= 1
            j -= 1
        