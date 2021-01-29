def minimum_waiting_time(array):
    array.sort()
    total_waiting_time = 0
    accumulate_times = 0
    for index in range(1, len(array)):
        accumulate_times += array[index - 1]
        total_waiting_time += accumulate_times

    return total_waiting_time


def main():
    times = [4, 3, 6, 1]
    print(minimum_waiting_time(times))


if __name__ == "__main__":
    main()
