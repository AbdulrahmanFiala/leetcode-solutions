## Valid Palindrome

You need to write a function solution that takes a string S of length N as input. It should return any palindrome that can be obtained by replacing all the question marks in S by lowercase letters ('a' to 'z'). If no palindrome can be obtained, the function should return the string "NO".

A palindrome is a string that reads the same both forwards and backwards. Examples of palindromes include "kayak", "radar", "mom".

### Examples

Given S = "?ab??a", the function should return "aabbaa".

Given S = "bab??a", the function should return "NO".

Given S = "?a?", the function may return "aaa". It may also return "zaz", among other possible answers.

### Constraints

- N is an integer within the range [1, 1000].
- The string S consists only of lowercase letters ('a' - 'z') or '?'.
