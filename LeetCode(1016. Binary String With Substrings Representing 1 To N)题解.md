# LeetCode(\1016. Binary String With Substrings Representing 1 To N)题解

Given a binary string `S` (a string consisting only of '0' and '1's) and a positive integer `N`, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

**Example 1:**

```
Input: S = "0110", N = 3
Output: true
```

**Example 2:**

```
Input: S = "0110", N = 4
Output: false
```

 

**Note:**

1. `1 <= S.length <= 1000`
2. `1 <= N <= 10^9`

## 解题思路

给一个全部由0和1组成的字符串，和一个整数N，判断1到N的所有整数转成的二进制串是否存在于字符串内。

直接使用Python的算法即可，暴力枚举。网上有很多trick，但是我都觉得有点问题。

代码如下，时间复杂度O(bit(N)*len(S))，空间复杂度O(1)。

`Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Binary String With Substrings Representing 1 To N.`

`Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary String With Substrings Representing 1 To N.`

```Python
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for n in range(1, N+1):
            if bin(n)[2:] not in S: return False
        return True
```

BitBrave，2019-12-1