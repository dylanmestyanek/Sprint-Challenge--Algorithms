#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This block of code's run time would be O(1) constant time. This is due to the fact that any value greater than 1 will run through the loop twice. By the second loop, `a` will be n^4 which is always bigger than n^3 in the `while` condition. 


b) This block of code's run time would be O(n^2). This is due to the fact that there is a while loop, nested within a for loop. As n increasing, it increases the amount of times these loops run. For example, when `n` is `2`, it will run through the loops twice `2^2`, when `n` is `3`, it will run through the loops three times `3^3`. It runs the loops `n` amount of times.


c) This block of code's run time would be O(2^n). This is due to the fact that the function is recursive, and calls itself until `bunnies` reaches `0`. The result of this is doubling the run time every step through the function. 

For example, if `bunnies = 3` the return statements would look like:
```python
    return 2 + bunnyEars(2) + bunnyEars(1)
```

or if `bunnies = 6`:
```python
    return 2 + bunnyEars(5) + bunnyEars(4) + bunnyEars(3) + bunnyEars(2) + bunnyEars(1)
```

## Exercise II


