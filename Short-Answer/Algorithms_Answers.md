em#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This block of code's run time would be O(1) constant time. This is due to the fact that any value greater than 1 will run through the loop twice. By the second loop, `a` will be n^4 which is always bigger than n^3 in the `while` condition. 


b) This block of code's run time would be O(n^2). This is due to the fact that there is a while loop, nested within a for loop. As `n` increases, it increases the amount of times these loops run. For example, when `n = 2`, it will run through the loops twice `2^2`, when `n = 3`, it will run through the loops three times `3^3`.


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

- `n` is height of the building
- `f` is the minimum floor level that an egg will break at when dropped
- `any floor < f` will not break the egg
- `any floor > f` will break the egg

```python
    def egg_drop(height, floor):
        if floor <= height:
            if floor == 0:
                return floor
            
            return 1 + egg_drop(height, floor - 1)
```

This function would return an egg surviving a drop off of each floor. This run time would be O(2^n) due to the fact that the recursion calls itself until it reaches the base case (when you are on the bottom floor).


