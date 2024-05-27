# Water Jug Problem

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
        self.parent = None
        self.action = None

    def __str__(self):
        return "({}, {})".format(self.jug1, self.jug2)

    def is_goal(self, goal_jug1, goal_jug2):
        return self.jug1 == goal_jug1 and self.jug2 == goal_jug2

    def is_valid(self, jug1_max, jug2_max):
        return 0 <= self.jug1 <= jug1_max and 0 <= self.jug2 <= jug2_max

    def get_moves(self, jug1_max, jug2_max):
        moves = []
        # Fill jug 1
        moves.append(State(jug1_max, self.jug2))
        # Fill jug 2
        moves.append(State(self.jug1, jug2_max))
        # Empty jug 1
        moves.append(State(0, self.jug2))
        # Empty jug 2
        moves.append(State(self.jug1, 0))
        # Pour jug 1 into jug 2
        diff = min(self.jug1, jug2_max - self.jug2)
        moves.append(State(self.jug1 - diff, self.jug2 + diff))
        # Pour jug 2 into jug 1
        diff = min(self.jug2, jug1_max - self.jug1)
        moves.append(State(self.jug1 + diff, self.jug2 - diff))
        return moves

def solve(jug1_max, jug2_max, goal_jug1, goal_jug2):
    initial_state = State(0, 0)
    queue = [initial_state]
    visited = set()

    while queue:
        curr_state = queue.pop(0)

        if curr_state.is_goal(goal_jug1, goal_jug2):
            path = []
            while curr_state.parent:
                path.append(curr_state.action)
                curr_state = curr_state.parent
            path.reverse()
            return path

        visited.add(str(curr_state))

        for move in curr_state.get_moves(jug1_max, jug2_max):
            if str(move) not in visited and move.is_valid(jug1_max, jug2_max):
                move.parent = curr_state
                move.action = "{} -> {}".format(curr_state, move)
                queue.append(move)

    return None

# Example usage
jug1_max = 5
jug2_max = 3
goal_jug1 = 4
goal_jug2 = 0

path = solve(jug1_max, jug2_max, goal_jug1, goal_jug2)

if path:
    print("Steps to reach the goal:", path)
else:
    print("Goal is not reachable.")

#In the above code, the State class represents a single state of the problem, with the jug1 and jug2 attributes representing the amount of water in the two jugs, the parent attribute keeping track of the parent state, and the action attribute keeping track of the action that led to the current state. The is_goal method checks if the current state is the goal state, the is_valid method checks if the current state is valid (i.e., the amount of water in each jug is within the valid range), and the get_moves method generates all possible moves from the current state.

#The solve function performs a breadth-first search to