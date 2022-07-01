
"""
8 Puzzle solver using Simulated Annealing.
"""

# Import required libraries.
import random
import math
import copy

# Setting the random seed for same output.
random.seed(42)

class Solver:

    def __init__(self, initial_state, goal_state):
        """
        Initialize the object.
        """

        # Setup the class with the initial and goal states.
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_blank_pos(self, state):
        """
        Get the position of the blank in the puzzle.
        """

        for i in range(3):
            for j in range(3):

                if state[i][j] == 0:
                    return [i, j]


    def get_neighbors(self, state):
        """
        Get all the valid moves.
        """

        # Get the blank position.
        blank_pos = self.get_blank_pos(state)

        # Top, Left, Right, and Bottom moves.
        positions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        # Initialize the neighbors.
        neighbors = []

        for pos in positions:

            # Get the new x move.
            x = pos[0] + blank_pos[0]

            # Get the new y move.
            y = pos[1] + blank_pos[1]

            # If x and y are valid moves then add it to the neighbors list.
            if (x >= 0 and x < 3) and \
               (y >= 0 and y < 3):

                neighbors.append([x, y])

        return neighbors

    def print_state(self, state):
        """
        Print the state of the solution.
        """


        output = ''

        output += '.-------.\n'

        for i in range(3):

            output += '| '

            for j in range(3):

                output += str(state[i][j]) + ' '

            output += '|\n'

        output += '.-------.'

        print(output)

        # for i in range(3):

        #     for j in range(3):

        #         print(state[i][j], end=' ')

        #     print('')

    def compute_cost(self, state):
        """
        Computes the hamming distance i.e; number of cells that are out of place
        from the goal state
        """

        cost = 0

        for i in range(3):

            for j in range(3):

                if state[i][j] != self.goal_state[i][j]:

                    # Update the cost.
                    cost += 1

        return cost

    def simulated_annealing(self, state):
        """
        Use the Simulated Annealing to solve the 8-puzzle.
        """

        # Set the initial temperature.
        initial_temp = 90

        # Set the final temperature.
        final_temp = 0.01

        # Set the alpha value.
        alpha = 0.0001

        # Set the current temperature, state, solution, and best solution.
        current_temp = initial_temp
        current_state = state
        solution = state
        solution_best = state

        while current_temp > final_temp:

            # Get the blank position.
            blank_pos = self.get_blank_pos(current_state)

            # Pick the random move.
            neighbor = random.choice(self.get_neighbors(current_state))

            # Deep copy the current state.
            new_state = copy.deepcopy(current_state)

            # Find the blanks in the current state.
            bp1 = blank_pos[0]
            bp2 = blank_pos[1]

            # Get the x and y of the new state.
            np1 = neighbor[0]
            np2 = neighbor[1]

            # Swap the blank with the new move.
            new_state[bp1][bp2], new_state[np1][np2] = new_state[np1][np2], new_state[bp1][bp2]

            # Find the cost difference with the old state and the new state.
            cost_diff = self.compute_cost(new_state) - self.compute_cost(current_state)

            if self.compute_cost(solution_best) > self.compute_cost(new_state):

                # If the new state is better the global best solution then update it.
                solution_best = new_state

            # If the new cost difference is greater than or eu the current cost.
            #
            # Compute the e^(-|old_cost - new_cost| / T) and if it's greater than
            # or equal to the the random probability then update the
            # current state.
            if random.uniform(0, 1) <= math.exp((-1 * cost_diff) / current_temp):
                current_state = new_state

            # Update the temperature.
            current_temp -= alpha

        # return the best solution.
        return solution_best

if __name__ == '__main__':

    # Initial state.
    # initial = [
    #     [5, 7, 3],
    #     [1, 6, 4],
    #     [8, 0, 2]
    # ]

    initial = [
        [1, 3, 4],
        [8, 0, 5],
        [7, 2, 6]
    ]

    # Goal state.
    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    # Initialze the solver.
    solver = Solver(initial, goal)

    print('The initial state:')
    solver.print_state(initial)

    print('Using simulated annealing to solve the 8-puzzle.')

    # Get the solution.
    sol = solver.simulated_annealing(initial)

    print('8-puzzle solved.')

    print('Final state:')

    # Perform the simulated annealing and print the best solution.
    solver.print_state(sol)

# Output
# ---
#
# The initial state:
# .-------.
# | 1 3 4 |
# | 8 0 5 |
# | 7 2 6 |
# .-------.
# Using simulated annealing to solve the 8-puzzle.
# 8-puzzle solved.
# Final state:
# .-------.
# | 1 2 3 |
# | 8 0 4 |
# | 7 6 5 |
# .-------.
