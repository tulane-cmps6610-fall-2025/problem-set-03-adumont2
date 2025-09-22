# CMPS 6610 Problem Set 03
## Answers

**Name:**__ Aaron Dumont_______________________


Place all written answers from `problemset-03.md` here for easier grading.

- **1a.**
See main.py

Output:
✅ All isearch tests passed!

- **1b.**
This function is sequential. It makes a single recursive call on a list that is one element smaller. This creates a dependency chain where each step must complete before the next one can begin.

**Work**: The function is called for each of the $n$ elements in th list. Therefore, the total work is proportional to the length of the list. **Work: $O(n)$**

**Span**: The algorithm is sequential so work and span are the same. **Span: $O(n)$**

- **1c.**
See main.py

Output:[False, False, False, False, True, False, False]
[False, False, False]
[False]
[False, False]
[False]
[False]
[False, True, False, False]
[False, True]
[False]
[True]
[False, False]
[False]
[False]
[False, False, False, False, False, True]
[False, False, False]
[False]
[False, False]
[False]
[False]
[False, False, True]
[False]
[False, True]
[False]
[True]
[False, False, False, False, False, False]
[False, False, False]
[False]
[False, False]
[False]
[False]
[False, False, False]
[False]
[False, False]
[False]
[False]
[]
✅ All rsearch tests passed!

- **1d.**
**Work:** Rsearch has 2 stages: the initial mapping and the reduction. Let $n$ be the length of the list L.

1. Mapping L to bool_list: This step involves one operation per element. 

Work: $O(n)$

Span: This is a parallel operation so, assuming enough processors, it can be done in constant time. Span: $O(1)$.

2. Reduce call: The reduce function splits the list in half at each step.

Work: $W(n) = 2W(n/2) + O(1). Leaf-dominated. #leaves = $n^{log_2(2)} = n. Therefore, **Work = $O(n)$**

Span: $S(n) = S(n/2) + O(1)$. Balanced. Work per level=1. #levels, $k = log_2(n)$. Therefore **$S(n) = O(logn)$**

Combining the above: 

Work: **$W(n) = O(n) + O(n) = O(n)$**

Span: **$S(n) = O(1) + O(logn) = O(logn)$**


- **1e.**
The ureduce function asymmetrically splits the list into 1/3 and 2/3. It then calls the original (balanced) reduce function on these 2 smaller lists.

Work: $W(n) = W(n/3) + W(2n/3) + O(1)$ Leaf-dominated **Work: $O(n)$**

Span: $S(n) = max(S(n/3), S(2n/3)) + O(1)$ = $S(2n/3) +O(1)$ = $O(log(2n/3))$ = **$O(logn)$**

- **2a.**
```
Python like:
def dedup(A):
    seen = set()
    result = []
    for item in A:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

SPARC like:
dedup(A) =
  let
    // f is the function that processes one item.
    // It takes the current state (seen, result) and an item,
    // and returns the next state.
    let f((seen, result), item) =
      if Set.member(item, seen) then
        (seen, result) // Item already seen, state is unchanged
      else
        // Item is new, add it to both the set and the result list
        (Set.insert(item, seen), result ++ <item>) 
    in
      // Run the iteration, starting with an empty set and empty list.
      let 
        (_, final_result) = iterate(f, (Set.empty, <>), A)
      in
        final_result
      end
    end
```
- Work: O(n) — each element is checked once, with O(1) expected membership tests.

- Span: O(n) — recursion is sequential due to order preservation.

- Result: Returns the list of distinct elements of A, preserving their first occurrence order.

- **2b.**

Algorithm:
- Flatten all lists into one sequence.
- Group elements by value (using hashing or sorting).
- Output one representative per group.

SPARC Specification:
```
fun multi_dedup(A : list of lists) : list =
    let
        val flat = flatten(A)
        val grouped = groupBy(flat, key = id)
    in
        keys(grouped)
    end
```
Work:

Flattening: O(N).

Grouping: O(N) expected (hash partitioning).

Extracting keys: O(U), where U = number of unique elements.

Total Work = O(N).

Span:

Flattening can be done in O(log m) span (parallel concatenation).

Grouping can be done in O(log N) span (parallel hashing / sorting).

Extracting keys is O(1) span per group.

Total Span = O(log N).

Comparison:
- Part (a): Work O(n), Span O(n) (sequential, order-preserving)
- Part (b): Work O(N), Span O(log N) (parallel, order not required)

--

- **2c.**

Useful operations:
- map: to transform elements into key–value pairs
- flatten/concat: to merge multiple lists
- groupBy/reduce: to collect duplicates and keep one representative
- filter: to remove already-seen elements in sequential dedup

These operations are especially powerful in the distributed setting, where they enable parallelism and reduce span from O(n) to O(log n).

Not useful operations:
- iterate: this function is not helpful for designing an efficient parallel algorithm because it is inherently sequential. Using it, as shown in my dedup algorithm (in 2a), results in a linear span (O(n)), which offers no parallelism.

--

- **3b.**




- **3d.**





- **3f.**




- **4a.**




- **4b.**





- **4c.**




