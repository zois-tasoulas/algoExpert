def task_assignment(workers, tasks):
    task_id_pairs = list(zip(tasks, (index for index in range(len(tasks)))))

    task_id_pairs.sort()
    schedule = []
    for worker in range(workers):
        schedule.append(
            [task_id_pairs[worker][1], task_id_pairs[2 * workers - worker - 1][1]]
        )

    return schedule


def main():
    workers = 5
    tasks = [1, 6, 6, 4, 15, 9, 2, 5, 3, 12]

    for pair in task_assignment(workers, tasks):
        print(pair)


if __name__ == "__main__":
    main()
