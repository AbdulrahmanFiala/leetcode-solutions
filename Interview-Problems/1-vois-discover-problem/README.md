## Distinct Products

You are given an array `A` of `N` positive integers. Consider the following operation: remove one element from `A` and compute the product of all the remaining array elements. If there is only one element remaining in the array, the product is equal to that element.

For example, if `A = (9, 16, 4)`, we can:

- Remove 9 and get a product equal to `(16 × 4) = 64`.
- Remove 16 and get a product of `9 × 4 = 36`.
- Remove 4 and get a product of `9 × 16 = 144`.

As seen in the example above, the product might change depending on which element we remove.

Write a function that, given an array `A` of `N` integers, returns the number of different products that can be obtained by removing exactly one element from `A`.

### Examples

Given `A = [9, 16, 4]`, the function should return 3. The achievable products are 64, 36, and 144.

Given `A = [3, 4, 2, 3, 1]`, the function should return 4.

Given `A = [10000000000, 10000000000]`, the function should return 1.

### Constraints

- `N` is an integer within the range 2 to 100,000.
- Each element of array `A` is an integer within the range 1 to 1,000,000,000.
