class WaterArea(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.heights = {}
        self.prev_left_idx = 0
        self.prev_right_idx = 0

    def find_water_area(self, curr_idx):
        assert curr_idx >= 0

        if curr_idx == 0 or curr_idx == (self.length - 1):
            return 0

        if curr_idx in self.heights:
            height = self.heights[curr_idx]
        else:
            left_idx, left_max = self.get_left_max(curr_idx)
            right_idx, right_max = self.get_right_max(curr_idx)
            height = min(left_max, right_max)
            self.memoize(curr_idx, right_idx, height)

        area = height - self.nums[curr_idx]

        return area if area > 0 else 0

    def get_left_max(self, curr_idx):
        left_max = 0
        max_idx = None
        for idx, num in enumerate(self.nums[self.prev_left_idx:curr_idx + 1]):
            if num > left_max:
                left_max = num
                max_idx = idx

        if max_idx is not None:
            return max_idx + curr_idx, left_max
        return curr_idx, self.nums[curr_idx]

    def get_right_max(self, curr_idx):
        right_max = 0
        max_idx = None
        for idx, num in enumerate(self.nums[curr_idx:]):
            if num > right_max:
                right_max = num
                max_idx = idx

        if max_idx is not None:
            return max_idx + curr_idx, right_max
        return curr_idx, self.nums[curr_idx]

    def memoize(self, curr_idx, right_idx, height):
        if curr_idx > self.prev_right_idx:
            self.prev_left_idx = self.prev_right_idx
            self.prev_right_idx = right_idx

        for idx in range(self.prev_left_idx + 1, right_idx + 1):
            self.heights[idx] = height

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
    # test_water_area()
    answer = solution(nums)
    assert 15 == answer