
def get_profit_weight_ratio(profits, weights):
    """
    Returns the list of tuples with profits, weight, and profit-weight ratio.

    Time Complexity: O(n)
    """

    tuples = []

    for i in range(len(profits)):

        ratio = profits[i] / weights[i]

        tuples.append((profits[i], weights[i], ratio))

    return tuples



def fractional_knapsack(profits, weights, capacity):
    """
    Computes the maximum profit from the given data and capacity.

    Time Complexity: O(n logn)
        Where n = No. of items/objects
    """

    # Initialize the maximum profit.
    maximum_profit = 0

    # Get the profit-weight ratio.
    tuples = get_profit_weight_ratio(profits, weights)

    # Sort the list by profit-weight ratio in decreasing order.
    tuples.sort(key=lambda x: x[2], reverse=True)

    for i in range(len(tuples)):

        # Get item at ith index.
        item = tuples[i]

        # Get profit.
        profit = item[0]

        # Get weight.
        weight = item[1]

        if weight <= capacity:

            # Update the profit as the item is included.
            maximum_profit += profit

            # Include the item and update the capacity.
            capacity = capacity - weight
        else:

            # Calculate the capacity-weight fraction.
            fraction = capacity / weight

            # Update the maximum profit by including the fraction of the item.
            maximum_profit += (fraction * profit)

            # Update the capacity
            # capacity -= fraction

            # Terminate.
            break

    return maximum_profit

if __name__ == '__main__':

    # Set profits.
    profits = [10, 5, 15, 7, 6, 18, 3]

    # Set weights.
    weights = [2, 3, 5, 7, 1, 4, 1]

    # Set capacity.
    capacity = 15

    print('Profits:', profits)
    print('Weights:', weights)
    print('Capacity:', capacity)
    print('Maximum Profit:', round(fractional_knapsack(profits, weights, capacity), 2))

# Result:
# ---
#
# Profits: [10, 5, 15, 7, 6, 18, 3]
# Weights: [2, 3, 5, 7, 1, 4, 1]
# Capacity: 15
# Maximum Profit: 55.33
