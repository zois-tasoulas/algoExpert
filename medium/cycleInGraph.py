def dfs_traversal(edges, node):
    visited = [False for _ in range(len(edges))]
    queue = [node]

    while queue:
        current_node = queue.pop(-1)
        if visited[current_node] and current_node == node:
            return True
        elif visited[current_node]:
            break
        visited[current_node] = True
        for neighbor in edges[current_node]:
            queue.append(neighbor)

    return False


def cycle_in_graph(edges):
    for node in range(len(edges)):
        if dfs_traversal(edges, node):
            return True

    return False


def main():
    edges = [[1, 2], [3, 2, 4], [], [4], [0, 5], [6], [4], []]
    print(cycle_in_graph(edges))


if __name__ == "__main__":
    main()
