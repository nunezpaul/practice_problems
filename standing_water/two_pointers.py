def find_total_water_area(height):
    total_area = 0
    left_max = 0
    right_max = 0

    left = 0
    right = len(height) - 1
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            total_area += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total_area += right_max - height[right]
            right -= 1

    return total_area

def test():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    find_total_water_area(heights)

if __name__ == '__main__':
    test()

    nums = [int(i) for i in list('413533253221321')]
    assert find_total_water_area(nums) == 15

    nums = [int(i) for i in list('61313131316')]
    assert find_total_water_area(nums) == 37