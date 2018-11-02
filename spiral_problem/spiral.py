def spiral(val):
    coord = [0, 0]
    step_dir = {'U': [0, 1], 'R': [1, 0], 'D': [0, -1], 'L': [-1, 0]}

    count = 0
    steps = 1
    queue = ['U', 'R']  # D * step
    while count < val:
        for item in queue:
            for step in range(steps):
                if count < val:
                    step_vector = step_dir[item]
                    coord[0] += step_vector[0]
                    coord[1] += step_vector[1]
                    count += 1

        steps += 1
        if queue == ['U', 'R']:
            queue = ['D', 'L']
        else:
            queue = ['U', 'R']

    return coord


if __name__ == '__main__':
    print(spiral(0))
    print(spiral(2))
    print(spiral(6))
    print(spiral(10))
    print(spiral(17))