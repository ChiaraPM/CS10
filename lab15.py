
# Exercise 1
#Create a function that finds al lthe subsets in a given list
#The subsets is any combination of elements from the original ist
#This includes an empty set and the list itself as a full list.
def make_subsets(lst):
    if len(lst)==0:   ##Asking if lst is empty ==[]
        return [[]]
    else:
        subsets=[]
        for subset in make_subsets(lst[1:]):
            subsets.append(subset)
            subsets.append([lst[0]]+subset)
        return subsets
    
    """
    Find all subsets of a given list.

    A subset is any combination of elements from the original list, including the empty set and the list itself.

    Parameters:
    - lst (list): The list from which to find subsets.

    Returns:
    - list of lists: A list containing all subsets of the original list.

    Examples:
    >>> make_subsets([])
    [[]]
    >>> make_subsets([1])
    [[], [1]]
    >>> make_subsets([1, 2])
    [[], [1], [2], [1, 2]]
    >>> make_subsets([1, 2, 3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    >>> make_subsets(["a", "b", "c", "d"])  # Example provided
    [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c'], ['d'], ['a', 'd'], ['b', 'd'], ['a', 'b', 'd'], ['c', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]
    """
    pass #FIX ME

#This function will calculate the n-th Fibonacci number
#Uses memoization
# Exercise 2
def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using tree recursion with memoization.

    Memoization is an optimization technique that stores the results of expensive function calls
    and reuses them when the same inputs occur again.

    Parameters:
    - n (int): The position in the Fibonacci sequence.

    Returns:
    - int: The n-th Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)  # Example provided
    55
    >>> fibonacci(30)  # Example provided
    832040
    """
    def helper(n, memo):
        if n <= 1:
            return n 
        if n in memo:
            return memo[n]
        
        memo[n] = helper(n-1, memo) + helper(n-2, memo)

        return memo[n]
        pass #
    return helper(n, {})



# Exercise 4
def max_depth(lst):
    """
    Find the maximum depth of nested lists using recursion and a helper function.

    Parameters:
    - lst (list): A list which may contain nested lists of integers

    Returns:
    int

    Examples:
    >>> max_depth([1, 2, 3])
    1
    >>> max_depth([1, [2, [3, 4], 5], 6])
    3
    >>> max_depth([[1, 2, [3]], 4])
    3
    >>> max_depth([1, [2, [3, [4, [5]]]]])
    5
    >>> max_depth([1, [2, 3], [4, 5]])
    2
    """
    #bone strucutre found in supplementary guide
    def helper(sub_lst, current_depth):
        max_depth = current_depth 
        for item in sub_lst:
            if isinstance(item, list):
                # Recursively call helper, increasing depth
                depth = helper(item, current_depth+1)
                max_depth = max(max_depth, depth)
        return max_depth

        pass #FIX ME

    return helper(lst, 1) # This line should be kept and is part of the solution