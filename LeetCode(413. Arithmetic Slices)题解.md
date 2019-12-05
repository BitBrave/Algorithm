# LeetCode(\413. Arithmetic Slices)题解

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not arithmetic.

```
1, 1, 2, 5, 7
```



A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.



**Example:**

```
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```

## 解题思路

这个题说白了就是从给定的数组内找出有多少个大于等于3的等差数列。

这个题可以通过DP一次遍历解决。通过扫描一遍数组，发现下一个数字是否能够加入到等差数列中。维护遍历到当前位置的数组内，包括最后一个元素在内的等差数组的长度，如果新的能加入，就直接最终结果内加上对应等差数组差数组长度-1,（因为必须大于等于3，而且新增加的等差数组一定是包括当前遍历的位置的），最后等差数组长度加1。如果当前元素不能加入，就将等差数组归零，重新开始计算即可。

代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 63.86% of C++ online submissions for Arithmetic Slices.`

`Memory Usage: 8.9 MB, less than 31.25% of C++ online submissions for Arithmetic Slices.`

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int ret = 0, len = A.size(), c = 0;

        for(int i=2; i<len; i++){
            if(A[i]-A[i-1] != A[i-1]-A[i-2]) c = 0;
            else{
                c++;
                ret += c;
            }
        }
        return ret;
    }
};
```

BitBrave，2019-12-05