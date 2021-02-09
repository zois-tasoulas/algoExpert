def staircase_traversal(height, max_steps):
    ways_to_top = [0 for _ in range(height + 1)]
    ways_to_top[0] = 1
    ways_to_top[1] = 1

    for current_height in range(2, height + 1):
        current_step = 1
        while current_step <= current_height and current_step <= max_steps:
            ways_to_top[current_height] += ways_to_top[current_height - current_step]
            current_step += 1

    return ways_to_top[height]


def main():
    height = 7
    max_steps = 4

    print(staircase_traversal(height, max_steps))


if __name__ == "__main__":
    main()
