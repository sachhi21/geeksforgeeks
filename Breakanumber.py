// Given a really large number N, break it into 3 whole numbers such that they sum up to the original number and 
find the number of ways to do so. Since this number can be very large, return it modulo 109+7. 

 

// Example 1:

// Input:
// N = 2
// Output:
// 6
// Explanation:
// Possible ways to break the number:
// 0 + 0 + 2 = 2 
// 0 + 2 + 0 = 2
// 2 + 0 + 0 = 2
// 0 + 1 + 1 = 2
// 1 + 1 + 0 = 2
// 1 + 0 + 1 = 2

//python:

class Solution:
    def waysToBreakNumber(self, n):
        return ((n+1)*(n+2)//2)%(10**9+7)

