import itertools as it


def num_of_friends(friend_pairs):
    unique_friends = set(it.chain.from_iterable(friend_pairs))
    friend_map = _friend_mapping(friend_pairs)
    friend_count = {}
    for friend in unique_friends:
        if friend not in friend_map:
            friend_count[friend] = 0
            continue

        history = set()
        _depth_first_search(friend, friend_map, history)
        friend_count[friend] = len(history) - 1

    return friend_count


def _depth_first_search(friend, friend_map, history):
    if friend in history or friend not in friend_map:
        return

    history.add(friend)
    for other_friend in friend_map[friend]:
        _depth_first_search(other_friend, friend_map, history)


def _friend_mapping(friend_pairs):
    friend_map = {}
    for friend_pair in friend_pairs:
        if len(friend_pair) == 1:
            continue

        first_friend = friend_pair[0]
        second_friend = friend_pair[1]

        if first_friend not in friend_map:
            friend_map[first_friend] = set()
        friend_map[first_friend].add(second_friend)

        if second_friend not in friend_map:
            friend_map[second_friend] = set()
        friend_map[second_friend].add(first_friend)
    return friend_map


def print_mapping(friend_map):
    for key, val in friend_map.items():
        print("{key}: {val}".format(key=key, val=val))


def generate_friends1():
    friends = [
        ['A', 'B'],
        ['A', 'C'],
        ['B', 'D'],
        ['B', 'C'],
        ['R', 'M'],
        ['S'],
        ['P'],
        ['A']
    ]
    return friends


if __name__ == '__main__':
    friend_pairs = generate_friends1()
    friend_count = num_of_friends(friend_pairs)
    print_mapping(friend_count)