# Inputs: A graph containing the flights that travel across destinations, along with two strings, that are both a starting point and a ending point respectively (destination)
# Output: An integer that represents the total number of miles from the starting point to the ending point

def prob05(flights, start: str, dest: str) -> int:
    visited = set()

    def dfs(curr_airport: str) -> int:
        if curr_airport == dest:
            return 0

        visited.add(curr_airport)

        if curr_airport in flights:
            for neighbor, cost in flights[curr_airport]:
                if neighbor not in visited:
                    result = dfs(neighbor)
                    if result != -1:
                        return result + cost

        visited.remove(curr_airport)
        return -1

    return dfs(start)
