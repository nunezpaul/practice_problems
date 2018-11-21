def triple_sum(nums):
    result = []
    for num_i in nums:
        for num_j in nums:
            sum_num = -(num_i + num_j)
            i_is_unique = num_i != num_j
            sum_is_unique = sum_num != num_i and sum_num != num_j
            print(num_i, num_j, sum_num, i_is_unique, sum_is_unique,  sum_num in nums)
            if i_is_unique and sum_is_unique and sum_num in nums:
                addition = set([num_i, num_j, sum_num])
                if addition not in result:
                    result.append(addition)
    return result


if __name__ == '__main__':
    nums = set([0, -1, 2, -3, 1])
    print(triple_sum(nums))

    nums = set([1, -2, 2, 0, 5])
    print(triple_sum(nums))