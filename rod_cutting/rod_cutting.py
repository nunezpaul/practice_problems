def optimal_cuts(rod_length, prices):
    memo = {}
    total = cut_rod(rod_length, prices, memo)
    return total


def cut_rod(curr_len, prices, memo):
    if curr_len < 1:
        return 0

    max_price = 0
    for cut in range(1, curr_len + 1):
        remaining = curr_len - cut
        if remaining in memo:
            curr_price = memo[remaining]
        else:
            curr_price = cut_rod(remaining, prices, memo)
            memo[remaining] = curr_price
        curr_price += prices[cut]
        max_price = max(max_price, curr_price)

    return max_price


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    results = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
    for result, r0d_l3ngth in zip(results, range(11)):
        assert result == optimal_cuts(r0d_l3ngth, prices)