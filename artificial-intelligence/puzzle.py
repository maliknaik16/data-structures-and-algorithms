
import copy
import heapq

class Node:

    def __init__(self, config, parent, cost, level, move):
        """
        Initialize the node.
        """

        self.parent = parent
        self.config = config
        self.cost = cost
        self.level = level
        self.move = move

    def get_config(self):
        """
        Returns the board configuration.
        """

        return self.config

    def get_parent(self):
        """
        Returns the parent node.
        """

        return self.parent

    def get_cost(self):
        """
        Returns the cost of the current configuration with respect to the goal
        configuration.
        """

        return self.cost

    def get_level(self):
        """
        Returns the level of the node.
        """

        return self.level

    def get_move(self):
        """
        Returns the move performed to reach this configuration.
        """

        return self.move

    def __lt__(self, other):
        return self.get_cost() < other.get_cost()

class Solution:

    def __init__(self, initial, goal, grid_size=3, blank=0):

        self.initial = initial
        self.goal = goal
        self.grid_size = grid_size
        self.blank = blank
        self.points = [
            (1, 0),            # Bottom movement
            (0, 1),            # Right movement
            (-1, 0),           # Top movement
            (0, -1)            # Left movement
        ]


    def cost(self, puzzle):
        """
        Returns the cost of the puzzle i.e; number of cell elements out of place
        from the goal configuration.
        """

        # Initially the cost is 0.
        cost = 0

        for i in range(self.grid_size):

            for j in range(self.grid_size):

                if self.goal[i][j] != puzzle[i][j]:

                    # Increment the cost if the cell don't match with the goal
                    # configuration.
                    cost += 1

        return cost

    def is_valid_pos(self, i, j):
        """
        Checks whether the given position in the grid is valid.
        """

        return (i < self.grid_size and i >= 0) and (j >= 0 and j < self.grid_size)

    def print_puzzle(self, puzzle):
        """
        Prints the given puzzle.
        """

        print('.-------.')

        for i in range(self.grid_size):

            print('|', end=' ')

            for j in range(self.grid_size):

                print(puzzle[i][j], end = ' ')

            print('|')

        print('.-------.')

    def get_puzzle_str(self, puzzle):
        """
        Returns the puzzle as the string.
        """

        output = ''

        output += '.-------.\n'

        for i in range(self.grid_size):

            output += '| '

            for j in range(self.grid_size):

                output += str(puzzle[i][j]) + ' '

            output += '|\n'

        output += '.-------.'

        return output

    def get_blank_pos(self, puzzle):
        """
        Returns the position of the empty cell / blank.
        """

        for i in range(self.grid_size):

            for j in range(self.grid_size):

                if puzzle[i][j] == self.blank:

                    return (i, j)

    def dfs(self, initial_config, max_depth=100):
        """
        Solves the 8-puzzle using Depth-First Search strategy.
        """

        # Initialize the stack.
        s = []

        # Get the cost of the initial configuration.
        # cost = self.cost(initial_config)

        # Initialize the count.
        count = 1

        # Initialize the root node to initial configuration of the puzzle.
        root = Node(initial_config, None, count, 0, '')

        # Push the root node onto the stack.
        s.append(root)

        # Initialize the move strings.
        moves = ['DOWN', 'RIGHT', 'UP', 'LEFT']

        # Initialize the set to track already visited nodes.
        visited = set()


        while len(s) > 0:

            # Get the top node from the stack.
            current = s.pop()

            # Get the current level.
            current_level = current.get_level() + 1

            # Get the configuration of the top node.
            board_config = current.get_config()

            # Get the blank position.
            blank_pos = self.get_blank_pos(board_config)

            # If the current level is greater than the maximum depth allowed
            # then do not search further.
            if current_level > max_depth:
                continue

            for i in range(self.grid_size + 1):

                x1 = blank_pos[0]
                y1 = blank_pos[1]
                x2 = x1 + self.points[i][0]
                y2 = y1 + self.points[i][1]

                # Check if the new position is not out of bounds.
                if self.is_valid_pos(x2, y2):

                    # Deep copy the board configuration so that it won't store
                    # the references to the sublist.
                    new_config = copy.deepcopy(board_config)

                    # Swap the blank space with the new position.
                    new_config[x1][y1], new_config[x2][y2] = new_config[x2][y2], new_config[x1][y1]

                    # Get the new board configuration as string.
                    new_board_config_string = self.get_board_as_str(new_config)

                    if new_board_config_string in visited or not self.is_solvable(new_config):
                        continue

                    # Get the cost of the new configuration.
                    # cost = self.cost(new_config)

                    # Create a new node.
                    new_node = Node(new_config, current, count + 1, current_level, moves[i])

                    if self.cost(new_config) == 0:

                        # Found the goal configuration.
                        #
                        # Print the path.
                        self.print_path(new_node)

                        # Clear the stack.
                        s.clear()
                        break

                    # Increment the count.
                    count = count + 1

                    # Push the new node onto the stack.
                    s.append(new_node)

                    # Add the board configuration to the set.
                    visited.add(new_board_config_string)

    def bfs(self, initial_config):
        """
        Solves the 8-puzzle using Breadth-First Search strategy.
        """

        # Initialize the queue.
        q = []

        # Get the cost of the initial configuration.
        # cost = self.cost(initial_config)

        # Initialize the count.
        count = 1

        # Initialize the root node to initial configuration of the puzzle.
        root = Node(initial_config, None, count, 0, '')

        # Enqueue the root node in the queue.
        q.append(root)

        # Initialize the move strings.
        moves = ['DOWN', 'RIGHT', 'UP', 'LEFT']

        # Initialize the set to track already visited nodes.
        visited = set()

        while len(q) > 0:

            # Dequeue the front element.
            current = q.pop(0)

            # Get the current level.
            current_level = current.get_level() + 1

            # Get the configuration of the top node.
            board_config = current.get_config()

            # Get the blank position.
            blank_pos = self.get_blank_pos(board_config)

            for i in range(self.grid_size + 1):

                x1 = blank_pos[0]
                y1 = blank_pos[1]
                x2 = x1 + self.points[i][0]
                y2 = y1 + self.points[i][1]

                # Check if the new position is not out of bounds.
                if self.is_valid_pos(x2, y2):

                    # Deep copy the board configuration so that it won't store
                    # the references to the sublist.
                    new_config = copy.deepcopy(board_config)

                    # Swap the blank space with the new position.
                    new_config[x1][y1], new_config[x2][y2] = new_config[x2][y2], new_config[x1][y1]

                    # Get the new board configuration as string.
                    new_board_config_string = self.get_board_as_str(new_config)

                    if new_board_config_string in visited or not self.is_solvable(new_config):
                        continue

                    # Get the cost of the new configuration.
                    # cost = self.cost(new_config)

                    # Create a new node.
                    new_node = Node(new_config, current, count + 1, current_level, moves[i])

                    if self.cost(new_config) == 0:

                        # Found the goal configuration.
                        #
                        # Print the path.
                        self.print_path(new_node)

                        # Clear the queue.
                        q.clear()
                        break

                    # Increment the count.
                    count = count + 1

                    # Enqueue the new node in the queue.
                    q.append(new_node)

                    # Add the board configuration to the set.
                    visited.add(new_board_config_string)

    def ucs(self, initial_config):

        # Initialize the heap.
        heap = []

        # Heapify the heap.
        heapq.heapify(heap)

        # Get the cost of the initial configuration.
        # cost = self.cost(initial_config)

        # Initialize the count.
        count = 1

        # Initialize the root node to initial configuration of the puzzle.
        root = Node(initial_config, None, count, 0, '')

        # Add the root node to the heap.
        heapq.heappush(heap, root)

        # Initialize the move strings.
        moves = ['DOWN', 'RIGHT', 'UP', 'LEFT']

        # Initialize the set to track already visited nodes.
        visited = set()

        while len(heap) > 0:

            # Get the current node.
            current = heapq.heappop(heap)

            # Get the current level.
            current_level = current.get_level() + 1

            # Get the configuration of the top node.
            board_config = current.get_config()

            # Get the blank position.
            blank_pos = self.get_blank_pos(board_config)

            if self.cost(board_config) == 0:

                # Found the goal configuration.
                #
                # Print the path.
                self.print_path(new_node)

                # Clear the heap.
                heap.clear()
                break

            for i in range(self.grid_size + 1):

                x1 = blank_pos[0]
                y1 = blank_pos[1]
                x2 = x1 + self.points[i][0]
                y2 = y1 + self.points[i][1]

                # Check if the new position is not out of bounds.
                if self.is_valid_pos(x2, y2):

                    # Deep copy the board configuration so that it won't store
                    # the references to the sublist.
                    new_config = copy.deepcopy(board_config)

                    # Swap the blank space with the new position.
                    new_config[x1][y1], new_config[x2][y2] = new_config[x2][y2], new_config[x1][y1]

                    # Get the new board configuration as string.
                    new_board_config_string = self.get_board_as_str(new_config)

                    if new_board_config_string in visited or not self.is_solvable(new_config):
                        continue

                    # Get the cost of the new configuration i.e; cost of child + parent.
                    new_cost = self.cost(new_config)
                    # new_cost = cost + self.cost(new_config)

                    # Create a new node.
                    new_node = Node(new_config, current, count + 1, current_level, moves[i])

                    if self.cost(new_config) == 0:

                        # Found the goal configuration.
                        #
                        # Print the path.
                        self.print_path(new_node)

                        # Clear the heap.
                        heap.clear()
                        break

                    # Increment the count.
                    count = count + 1

                    # Add the new node to the heap.
                    heapq.heappush(heap, new_node)

                    # Add the board configuration to the set.
                    visited.add(new_board_config_string)

    def is_solvable(self, board_config):
        """
        Returns True if the given board configuration is solvable. Otherwise, False.
        """

        # Initialize the inversion count.
        inversions = 0

        # Convert the 2D array to the 1D array.
        board_config_array = [cell for row in board_config for cell in row]

        # Get the number of cells.
        num_cells = self.grid_size * self.grid_size

        for i in range(self.grid_size):

            for j in range(i + 1, self.grid_size):

                # Increment the inversion count if A[i] > A[j] and i < j.
                if board_config_array[i] != self.blank and \
                   board_config_array[j] != self.blank and \
                   board_config_array[i] > board_config_array[j]:

                    # Increment.
                    inversions += 1

        return (inversions % 2) == 0

    def get_board_as_str(self, board_config):
        """
        Returns the board as the string.
        """

        board_string = ''

        for i in range(len(board_config)):

            for j in range(len(board_config[0])):

                board_string += str(board_config[i][j])

        return board_string

    def print_path(self, node):
        """
        Prints the path from the given node up to the root.
        """

        # Stores the path information.
        path = []

        # Initialize the move string.
        move = ''

        # Repeat until we reach the root node.
        while node != None:

            # Get the current board configuration.
            board_config = node.get_config()

            # Get the move string.
            if node.get_move() == '':
                move = 'DONE.'
            else:
                move = 'Move ' + node.get_move()

            # Add the board configuration and move onto the path list.
            path.append((self.get_puzzle_str(board_config), move))

            # Move pointer to the parent.
            node = node.parent

        # Get number of steps required to solve this puzzle.
        num_steps = len(path) - 1

        # Initialize the step string.
        step_string = ''

        for i in range(num_steps, -1, -1):

            # Print the board configuration.
            print(path[i][0])

            # Print the move.
            move = path[i - 1][1]
            print(move, '\n')

            if move[0] != 'D':

                # Append the move letter.
                step_string += move[move.index(' ') + 1] + ' '

        # Print the steps.
        print('Steps to solve puzzle:', num_steps, '(', step_string + ')')

if __name__ == '__main__':

    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    initial = [
        [1, 3, 4],
        [8, 0, 5],
        [7, 2, 6]
    ]

    solution = Solution(initial, goal, 3)

    # solution.dfs(initial)
    print('####################################################')
    print('#                                                  #')
    print('# Using Depth-First Search Algorithm:              #')
    print('#                                                  #')
    print('####################################################')
    solution.dfs(initial, max_depth=20)

    print('\n\n\n####################################################')
    print('#                                                  #')
    print('# Using Breadth-First Search Algorithm:            #')
    print('#                                                  #')
    print('####################################################')
    solution.bfs(initial)

    print('\n####################################################')
    print('#                                                  #')
    print('# Using Uniform-Cost Search Algorithm:             #')
    print('#                                                  #')
    print('####################################################')
    solution.ucs(initial)


# Code Output:
#
#
# ####################################################
# #                                                  #
# # Using Depth-First Search Algorithm:              #
# #                                                  #
# ####################################################
# .-------.
# | 1 3 4 |
# | 8 0 5 |
# | 7 2 6 |
# .-------.
# Move UP

# .-------.
# | 1 0 4 |
# | 8 3 5 |
# | 7 2 6 |
# .-------.
# Move LEFT

# .-------.
# | 0 1 4 |
# | 8 3 5 |
# | 7 2 6 |
# .-------.
# Move DOWN

# .-------.
# | 8 1 4 |
# | 0 3 5 |
# | 7 2 6 |
# .-------.
# Move RIGHT

# .-------.
# | 8 1 4 |
# | 3 0 5 |
# | 7 2 6 |
# .-------.
# Move RIGHT

# .-------.
# | 8 1 4 |
# | 3 5 0 |
# | 7 2 6 |
# .-------.
# Move DOWN

# .-------.
# | 8 1 4 |
# | 3 5 6 |
# | 7 2 0 |
# .-------.
# Move LEFT

# .-------.
# | 8 1 4 |
# | 3 5 6 |
# | 7 0 2 |
# .-------.
# Move UP

# .-------.
# | 8 1 4 |
# | 3 0 6 |
# | 7 5 2 |
# .-------.
# Move RIGHT

# .-------.
# | 8 1 4 |
# | 3 6 0 |
# | 7 5 2 |
# .-------.
# Move DOWN

# .-------.
# | 8 1 4 |
# | 3 6 2 |
# | 7 5 0 |
# .-------.
# Move LEFT

# .-------.
# | 8 1 4 |
# | 3 6 2 |
# | 7 0 5 |
# .-------.
# Move UP

# .-------.
# | 8 1 4 |
# | 3 0 2 |
# | 7 6 5 |
# .-------.
# Move LEFT

# .-------.
# | 8 1 4 |
# | 0 3 2 |
# | 7 6 5 |
# .-------.
# Move UP

# .-------.
# | 0 1 4 |
# | 8 3 2 |
# | 7 6 5 |
# .-------.
# Move RIGHT

# .-------.
# | 1 0 4 |
# | 8 3 2 |
# | 7 6 5 |
# .-------.
# Move DOWN

# .-------.
# | 1 3 4 |
# | 8 0 2 |
# | 7 6 5 |
# .-------.
# Move RIGHT

# .-------.
# | 1 3 4 |
# | 8 2 0 |
# | 7 6 5 |
# .-------.
# Move UP

# .-------.
# | 1 3 0 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move LEFT

# .-------.
# | 1 0 3 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move DOWN

# .-------.
# | 1 2 3 |
# | 8 0 4 |
# | 7 6 5 |
# .-------.
# DONE.

# Steps to solve puzzle: 20 ( U L D R R D L U R D L U L U R D R U L D )



# ####################################################
# #                                                  #
# # Using Breadth-First Search Algorithm:            #
# #                                                  #
# ####################################################
# .-------.
# | 1 3 4 |
# | 8 0 5 |
# | 7 2 6 |
# .-------.
# Move DOWN

# .-------.
# | 1 3 4 |
# | 8 2 5 |
# | 7 0 6 |
# .-------.
# Move RIGHT

# .-------.
# | 1 3 4 |
# | 8 2 5 |
# | 7 6 0 |
# .-------.
# Move UP

# .-------.
# | 1 3 4 |
# | 8 2 0 |
# | 7 6 5 |
# .-------.
# Move UP

# .-------.
# | 1 3 0 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move LEFT

# .-------.
# | 1 0 3 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move DOWN

# .-------.
# | 1 2 3 |
# | 8 0 4 |
# | 7 6 5 |
# .-------.
# DONE.

# Steps to solve puzzle: 6 ( D R U U L D )

# ####################################################
# #                                                  #
# # Using Uniform-Cost Search Algorithm:             #
# #                                                  #
# ####################################################
# .-------.
# | 1 3 4 |
# | 8 0 5 |
# | 7 2 6 |
# .-------.
# Move DOWN

# .-------.
# | 1 3 4 |
# | 8 2 5 |
# | 7 0 6 |
# .-------.
# Move RIGHT

# .-------.
# | 1 3 4 |
# | 8 2 5 |
# | 7 6 0 |
# .-------.
# Move UP

# .-------.
# | 1 3 4 |
# | 8 2 0 |
# | 7 6 5 |
# .-------.
# Move UP

# .-------.
# | 1 3 0 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move LEFT

# .-------.
# | 1 0 3 |
# | 8 2 4 |
# | 7 6 5 |
# .-------.
# Move DOWN

# .-------.
# | 1 2 3 |
# | 8 0 4 |
# | 7 6 5 |
# .-------.
# DONE.

# Steps to solve puzzle: 6 ( D R U U L D )
