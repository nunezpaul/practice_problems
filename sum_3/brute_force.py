def triple_sum(nums):
    result = []
    for i in nums:
        for j in nums:
            for k in nums:
                j_is_unique = j != i and j != k
                k_is_unique = k != i
                sum_is_zero = (i + j + k) == 0
                if j_is_unique and k_is_unique and sum_is_zero:
                    if set([i,j,k]) not in result:
                        result.append(set([i,j,k]))
    return result


if __name__ == '__main__':
    nums = set([0, -1, 2, -3, 1])
    print(triple_sum(nums))