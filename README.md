
# Dynamic Programming

## Optimal Substructure Property

It means that the optimal solution to the problem can be formulated from the optimal solution to smaller instances of the same problem.
Example: `f(n) = f(n - 1) + f(n - 2)`. Problem of size n reduced to `n - 1` and `n - 2`.



## Overlapping Subproblems

The smaller problems, which are needed to solve the bigger problem, are called multiple times while solving.

Example: `f(n) = f(n - 1) + f(n - 2)`, `f(n - 1) = f(n - 2) + f(n - 3)`. `f(n - 2)` is required at least twice to solve this.


# References
* https://www.hackerrank.com/topics/dynamic-programming
* https://www.geeksforgeeks.org/dynamic-programming/
