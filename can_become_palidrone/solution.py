def off_by_one_palidrone(string):
    return helper(string, left=0, right=len(string) - 1, error_count=0)

def helper(string, left, right, error_count):
    max_skips = 1
    while left < right:

        if string[left] == string[right]:
            left += 1
            right -= 1
        elif error_count < max_skips:
            check_left = helper(string, left + 1, right, error_count + 1)
            check_right = helper(string, left, right - 1, error_count + 1)
            return check_left or check_right
        else:
            return False

    return True


if __name__ == '__main__':
    strings = ['aabbaa', 'aabbbaa', 'ababbaa', 'bbabbaa', 'abcdefg']
    answers = [True, True, True, False, False]
    for string, answer in zip(strings, answers):
        assert answer == off_by_one_palidrone(string)