class WaterArea(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.right_heights = self.find_right_max_heights()

    def find_right_max_heights(self):
        max_num = 0
        right_heights = []
        for num in reversed(self.nums):
            max_num = max(max_num, num)
            right_heights.append(max_num)
        return list(reversed(right_heights))

    def find_total_water_area(self):
        total_area = 0
        left_max_heights = 0
        for idx, num in enumerate(self.nums):
            left_max_heights = max(left_max_heights, num)
            total_area += min(left_max_heights, self.right_heights[idx]) - num

        return total_area


def test_water_area():
    nums = [int(i) for i in list('413533253221321')]
    water_area = WaterArea(nums)
    assert water_area.right_heights == [5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 2, 1]

    nums = [int(i) for i in list('61313131316')]
    water_area = WaterArea(nums)
    assert water_area.right_heights == [6] * len(nums)


if __name__ == '__main__':
    test_water_area()
    nums = [int(i) for i in list('413533253221321')]
    water_area = WaterArea(nums)
    assert water_area.find_total_water_area() == 15

    nums = [int(i) for i in list('61313131316')]
    water_area = WaterArea(nums)
    assert water_area.find_total_water_area() == 37