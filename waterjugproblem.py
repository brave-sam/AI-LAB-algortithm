from collections import deque

def waterJugProblem(capacityA, capacityB, target):
    visited = set()
    queue = deque([(0, 0)])
    visited.add((0, 0))

    print("Jug A | Jug B")
    print("-------------")
    print("  0   |   0  ")

    while queue:
        curr_state = queue.popleft()
        waterA, waterB = curr_state

        if waterA == target or waterB == target:
            print("Target amount of water", target, "is possible.")
            return

        actions = [
            (capacityA, waterB),
            (waterA, capacityB),
            (0, waterB),
            (waterA, 0),
            (max(0, waterA - (capacityB - waterB)), min(capacityB, waterA + waterB)),
            (min(capacityA, waterA + waterB), max(0, waterB - (capacityA - waterA)))
        ]

        for action in actions:
            if action not in visited:
                queue.append(action)
                visited.add(action)
                print(f"  {action[0]}   |   {action[1]}  ")

    print("Target amount of water", target, "is not possible with given jug capacities.")

capacity_jugA = 4
capacity_jugB = 3
target_amount = 2

waterJugProblem(capacity_jugA, capacity_jugB, target_amount)
