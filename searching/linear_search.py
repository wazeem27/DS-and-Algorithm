"""Linear search algorithm example"""


def linear_search(L, e):
    """Simple function for linear search algorithm 
    :parameters
        L: Array of items we need to search in
        e: element we need to search for in the given array
    return Boolean Value"""
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
            # I could return here but it won't impact worst case
            # Rather it impact on average case
    return found

