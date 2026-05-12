class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        # Đếm ký tự trong magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Dùng ký tự cho ransomNote
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True
