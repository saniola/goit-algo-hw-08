import heapq


def minimize_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Choose the two shortest cables
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)

        # Calculate the cost of merging these two cables and add it to the total cost
        cost = shortest1 + shortest2
        total_cost += cost

        # Add a new cable to the heap representing the total length of the two merged cables
        heapq.heappush(cables, cost)

    return total_cost


# Example usage
cables = [4, 3, 2, 6, 1, 5]
min_cost = minimize_cost(cables)
print("Total costs for connecting cables:", min_cost)
