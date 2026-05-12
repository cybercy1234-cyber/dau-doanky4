class Solution(object):
    def destCity(self, paths):
        start_cities = set()
        
        # lưu các cityA
        for a, b in paths:
            start_cities.add(a)
        
        # tìm cityB không nằm trong cityA
        for a, b in paths:
            if b not in start_cities:
                return b 