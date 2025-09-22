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
dedup (A) =
    if $|A| \le 1$ then
        A
    else
        let
            //1. Tag each element with its index.
            tagged = <(A[i], i) : 0 <= i < |A|>

            // 2. Group indices by element including duplicates using comparison function, cmp.
            grouped = collect(cmp, tagged)

            // 3. Find the first (minimum) index for each element.
            first_indices = <(k, reduce min infinity v) : (k, v) in grouped>
      
            // 4. Sort the unique elements based on their first index.
            sorted_unique = sort(cmp_idx, first_indices)

            // 5. Extract just the elements.
            result = <k : (k, i) in sorted_unique>
    in
      result
    end
```
- **2b.**

- **2c.**

- **3b.**




- **3d.**





- **3f.**




- **4a.**




- **4b.**





- **4c.**




