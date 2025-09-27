#problem-set-03

# no other imports needed
from collections import defaultdict
import math
#

### PART 1: SEARCHING UNSORTED LISTS

# search an unordered list L for a key x using iterate
def isearch(L, x):
    # The accumulator 'found' keeps track of whether x has been seen.
    # The lambda function returns True if `found` is already True, or if the current `item` equals x.
    find_logic = lambda found, item: found or (item == x)
    
    # We start with an initial value of False because we haven't found x yet.
    return iterate(find_logic, False, L)

def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([], 2) == (2 in [1, 3, 5])


def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

# search an unordered list L for a key x using reduce
def rsearch(L, x):
    # 1. Map: Create a list of booleans. 
    #    Each element is True if the item in L equals x, and False otherwise.
    bool_list = [item == x for item in L]
    
    # The combining function is logical OR.
    or_op = lambda a, b: a or b
    
    # 2. Reduce: The identity for logical OR is False.
    #    If the list is empty, the result is False.
    return reduce(or_op, False, bool_list)

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [1, 3, 5])

def reduce(f, id_, a):
    print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(reduce(f, id_, a[:len(a)//3]),
                 reduce(f, id_, a[len(a)//3:]))




### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    # This part is already correct. It checks if the final count is 0.
    return iterate(parens_update, 0, mylist) == 0


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    # If the count is already negative, we've found an invalid sequence
    # (like a ')' before a '('). We "latch" onto this error state by
    # returning the negative number immediately.
    if current_output < 0:
        return current_output
        
    # Update the count based on the current character
    if next_input == '(':
        return current_output + 1
    elif next_input == ')':
        return current_output - 1
    else:
        # Ignore non-parenthesis characters
        return current_output

def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative([]) == True


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    if not mylist:
        return True

    # 1. Map: Convert ['(', 'a', ')'] to [1, 0, -1]
    mapped_list = [paren_map(x) for x in mylist]
    
    # Define the addition operation for scan and reduce
    add_op = lambda x, y: x + y
    
    # 2. Scan: Compute the running sum at every position.
    #    scan returns (list_of_partial_sums, total_sum)
    #    e.g., for [1, 1, -1, -1], returns ([1, 2, 1, 0], 0)
    scanned_list, total_sum = scan(add_op, 0, mapped_list)
    
    # 3. Reduce: Find the minimum value in the partial sums.
    #    If this is negative, condition 1 is violated.
    #    The identity for min is positive infinity.
    min_val = reduce(min_f, float('inf'), scanned_list)
    
    # Check both conditions: min is non-negative AND final sum is zero.
    return min_val >= 0 and total_sum == 0

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False
    assert parens_match_scan([]) == True

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    # base cases
    
    # recursive case
    # - first solve subproblems
    
    # - then compute the solution (R,L) using these solutions, in constant time.
    
    ###

    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses.
    """
    # Base cases
    if len(mylist) == 0:
        return (0, 0)
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1)  # 0 unmatched right, 1 unmatched left
        elif mylist[0] == ')':
            return (1, 0)  # 1 unmatched right, 0 unmatched left
        else:
            return (0, 0)
            
    # Recursive case
    else:
        mid = len(mylist) // 2
        # First, solve subproblems in parallel
        (R1, L1) = parens_match_dc_helper(mylist[:mid])
        (R2, L2) = parens_match_dc_helper(mylist[mid:])
        
        # Then, compute the solution using the subproblem results.
        # Unmatched lefts from the first half can match with
        # unmatched rights from the second half.
        matched_pairs = min(L1, R2)
        
        final_R = R1 + (R2 - matched_pairs)
        final_L = L2 + (L1 - matched_pairs)
        
        return (final_R, final_L)
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 

# For testing
if __name__ == "__main__":
    # Test for Part 1a
    #test_isearch()
    #print("✅ All isearch tests passed!")

    # Test for Part 1c
    test_rsearch()
    print("✅ All rsearch tests passed!")
    
    # Test for Part 3a
    test_parens_match_iterative()
    print("✅ All parens_match_iterative tests passed!")
    
    # Test for Part 3c
    test_parens_match_scan()
    print("✅ All parens_match_scan tests passed!")
    
    # Test for Part 3e
    test_parens_match_dc()
    print("✅ All parens_match_dc tests passed!")