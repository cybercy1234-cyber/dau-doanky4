class Solution(object):
    def sortPeople(self, names, heights):
        people = []

        # gộp name + height
        for i in range(len(names)):
            people.append((heights[i], names[i]))

        # sắp xếp giảm dần theo height
        people.sort(reverse=True)

        # lấy lại tên
        result = []
        for h, name in people:
            result.append(name)

        return result
            