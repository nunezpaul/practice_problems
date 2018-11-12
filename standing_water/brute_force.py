class WaterArea(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)

    def find_water_area(self, idx):
        if idx == 0 or idx == (self.length - 1):
            return 0

        left_idx, left_max = self.get_left_max(idx)
        right_idx, right_max = self.get_right_max(idx)
        height = min(left_max, right_max)
        area = height - self.nums[idx]

        return area if area > 0 else 0

    def get_left_max(self, start_idx):
        left_max = 0
        max_idx = None
        for idx, num in enumerate(self.nums[:start_idx]):
            if num > left_max:
                left_max = num
                max_idx = idx


        if max_idx is not None:
            return max_idx, left_max
        return start_idx, self.nums[start_idx]

    def get_right_max(self, start_idx):
        right_max = 0
        max_idx = None
        for idx, num in enumerate(self.nums[start_idx:]):
            if num > right_max:
                right_max = num
                max_idx = idx

        if max_idx is not None:
            return max_idx, right_max
        return start_idx, self.nums[start_idx]

def solution(nums):
    water_area = WaterArea(nums)
    total = 0
    for idx, num in enumerate(nums):
        total += water_area.find_water_area(idx)

    return total

def test_water_area():
    nums = [int(i) for i in list('413533253221321')]
    water_area = WaterArea(nums)
    assert 0 == water_area.find_water_area(0)
    assert 0 == water_area.find_water_area(water_area.length - 1)

    assert 3 == water_area.find_water_area(1)
    assert 1 == water_area.find_water_area(2)

    assert 0 == water_area.find_water_area(3)
    assert 0 == water_area.find_water_area(7)

    assert 0 == water_area.find_water_area(water_area.length - 2)
    assert 0 == water_area.find_water_area(water_area.length - 3)


if __name__ == '__main__':
    nums = [int(i) for i in list('413533253221321')]
    test_water_area()
    assert 15 == solution(nums)