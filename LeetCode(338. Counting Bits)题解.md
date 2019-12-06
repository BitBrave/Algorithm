# LeetCode(\338. Counting Bits)题解

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example 1:**

```
Input: 2
Output: [0,1,1]
```

**Example 2:**

```
Input: 5
Output: [0,1,1,2,1,2]
```

**Follow up:**

- It is very easy to come up with a solution with run time **O(n\*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
- Space complexity should be **O(n)**.
- Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.

## 解题思路

给定一个数num，要求返回0-num中的每个数的二进制形式中1的个数。

这个题可以使用DP解决。首先分析一个数x如果是偶数，那么+1在二进制表示中只会影响最后一个数，因此x+1中的1的数目就是x中1的数目-1.如果x是奇数，那么+1会将最后一位进1，x除了最后一位前面的数就进1。因此x+1的数目也就是将x/2+1的数目。这就可以每次迭代向后进行计算了。

同时，如果后面的数的状态总是能用前面的数进行表达。那么也可以从前面计算。比如要计算X的1的数目，其二进制表示中第一位肯定是1，后面的数组成的值肯定比X小，所以在计算X的时候肯定已经计算出来了。而X中除了第一位之外的所有元素组成的数可以使用对数计算得到。为X-2^(int(log(X)/log(2))。

这两种方法都可以在O(n)的时间内得到结果。这里我选用了第一种，代码如下，空间复杂度O(n)。

`Runtime: 52 ms, faster than 94.32% of C++ online submissions for Counting Bits.`

`Memory Usage: 9.5 MB, less than 95.12% of C++ online submissions for Counting Bits.`

****

```c++
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ret(num+1, 0);
        for(int i=1; i<=num; i++){
            if(i & 1) ret[i] = ret[i-1] + 1;
            else ret[i] = ret[(i-1)/2+1];
        }
        return ret;
    }
};
```

BitBrave，2019-12-06