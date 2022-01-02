
def get_empty_slot_index(slots, j):
    """
    Returns the empty slot index from the give slots by searching from j to 0,
    Otherwise, -1 is returned.

    Time Complexity: O(j)
        Where, j <= Maximum deadline time.
    """

    for i in range(j - 1, -1, -1):

        if slots[i] == -1:
            return i

    return -1

def make_pair(x, y):
    """
    Returns the tuple of list by combining the element from the passed lists.

    Time Complexity: O(n)
    """

    pairs = []

    for i in range(len(x)):
        pairs.append((x[i], y[i]))

    return pairs

def job_sequencing_with_deadlines(profits, deadlines):
    """
    Returns the maximum selected jobs and maximum profit from the given list of
    profits and deadlines.

    Time Complexity: O(n logn + nD) ~= O(n logn)
        Where, n = No. of jobs
               D = Maximum deadline time.
    """

    # Get number of jobs.
    n = len(profits)

    # Set the maximum profit.
    maximum_profit = 0

    # Get the maximum time from the given deadlines.
    maximum_time = max(deadlines)

    # Initialize the slots with no jobs.
    slots = [-1] * maximum_time

    # Make the profit-deadline pairs.
    profit_dealine_pairs = make_pair(profits, deadlines)

    # Sort the profit-deadline pairs in decreasing order by profit.
    profit_dealine_pairs.sort(key=lambda x: x[0], reverse=True)

    for i in range(n):

        # Get the job.
        job = profit_dealine_pairs[i]

        # Get the profit.
        profit = job[0]

        # Get the deadline.
        deadline = job[1]

        # Get the empty slot index. The return value of -1 indicates that no
        # empty slot was found.
        #
        # Time Complexity: O(D)
        empty_slot_index = get_empty_slot_index(slots, deadline)

        if empty_slot_index != -1:

            # Include this job and update the profit.
            maximum_profit += profit

            # Assign the job in the empty slot.
            slots[empty_slot_index] = i

    return slots, maximum_profit

if __name__ == '__main__':

    profits = [
        [20, 15, 10, 5, 1],
        [35, 30, 25, 20, 15, 12, 5]
    ]

    deadlines = [
        [2, 2, 1, 3, 3],
        [3, 4, 4, 2, 3, 1, 2]
    ]

    for i in range(len(profits)):

        p = profits[i]
        d = deadlines[i]

        # Get the assigned jobs and the total profit.
        jobs, profit = job_sequencing_with_deadlines(p, d)

        # Prepend J to each job id.
        jobs = list(map(lambda x: 'J' + str(x + 1), jobs))

        print('Given,')
        print('Profits:', p)
        print('Deadlines:', d)
        print('Selected Jobs:', ' -> '.join(jobs))
        print('Maximum Profit:', profit)

        if i != len(profits) - 1:
            print('\n---\n')

# Result
# ---
#
# Given,
# Profits: [20, 15, 10, 5, 1]
# Deadlines: [2, 2, 1, 3, 3]
# Selected Jobs: J2 -> J1 -> J4
# Maximum Profit: 40

# ---

# Given,
# Profits: [35, 30, 25, 20, 15, 12, 5]
# Deadlines: [3, 4, 4, 2, 3, 1, 2]
# Selected Jobs: J4 -> J3 -> J1 -> J2
# Maximum Profit: 110
