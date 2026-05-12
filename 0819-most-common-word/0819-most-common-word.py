class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        # chuyển về chữ thường
        paragraph = paragraph.lower()
        
        # thay dấu câu bằng khoảng trắng
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        words = paragraph.split()
        banned_set = set(banned)
        
        count = {}
        
        for word in words:
            if word not in banned_set:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        
        # tìm từ xuất hiện nhiều nhất
        max_word = ""
        max_count = 0
        
        for word in count:
            if count[word] > max_count:
                max_count = count[word]
                max_word = word
        
        return max_word
            