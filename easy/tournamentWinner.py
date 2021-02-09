def tournament_winner(competitions, results):
    teams = {}
    for pair in competitions:
        teams[pair[0]] = 0
        teams[pair[1]] = 0

    for index, pair in enumerate(competitions):
        winner_index = (results[index] + 1) % 2
        teams[pair[winner_index]] += 3

    return max(teams, key=teams.get)


def main():
    competitions = [
        ["A", "B"],
        ["B", "C"],
        ["C", "D"],
        ["D", "A"],
        ["A", "C"],
        ["B", "D"],
    ]
    results = [1, 1, 1, 0, 1, 1]
    print(tournament_winner(competitions, results))


if __name__ == "__main__":
    main()
