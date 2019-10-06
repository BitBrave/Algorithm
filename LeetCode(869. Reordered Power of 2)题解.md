# LeetCode(869. Reordered Power of 2)题解

Starting with a positive integer `N`, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return `true` if and only if we can do this in a way such that the resulting number is a power of 2.

 



**Example 1:**

```
Input: 1
Output: true
```

**Example 2:**

```
Input: 10
Output: false
```

**Example 3:**

```
Input: 16
Output: true
```

**Example 4:**

```
Input: 24
Output: false
```

**Example 5:**

```
Input: 46
Output: true
```

 

**Note:**

1. `1 <= N <= 10^9`

## 解题思路

给你一个数N（1 <= N <= 10^9），你可以对这个数中的每个数字进行重排组成另外一个数字，只要存在一个使得这个数是2的幂，则返回True；例如N=46,你可以重组为64，这样64就是2的幂了，则返回True。

因为1 <= N <= 10^9，而2^{32}>10^{9}，因此，最多只有2^{0}，2^{1}，2^{2}.....2^{31}共32个数，每个数都是不相同的，因此，我们只要判断N中每个数字的个数是否和之前的32个数中某一个数中的每一个数字的个数是否相同，只要相同数字的个数相同，那么就可以重新组合成那个数。因此，我们可以把N中的每个数字分解出来，存在一个长度为10的数组里面，然后将这个数组与前面32个数字分解的数组去对比，只要相等，就符合；
但是，两个数组是否相等比较麻烦，这样，我们又可以把每个数字设为10的多少次方，这样就没必要去比较整个数组是否相等，直接把这组数字用10的多少次方表示出来；比如N=4654，其中有2个4，1个5，1个6，因此可以表示为：10^{4}+10^{4}+10^{5}+10^{6}，这样出来的结果是唯一的，因此可以比较.

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 4 ms, faster than 73.32% of C++ online submissions for Reordered Power of 2.`

`Memory Usage: 9.4 MB, less than 50.00% of C++ online submissions for Reordered Power of 2.`

```c++
class Solution {
public:
    long hash_(long N){
        vector<long> V(10, 0);
        
        while(N){
            V[N % 10]++;
            N /= 10;
        }
        long res = 0;
        for(int i=0; i<10; i++) res += V[i] * (long)pow(10, i);
        return res;
    }
    bool reorderedPowerOf2(int N) {
        set<long> S;
        for(int i=0; i<32; i++) S.insert(hash_(pow(2, i)));
        if(S.find(hash_(N)) == S.end()) return false;
        return true;
    }
};
```

BitBrave, 2019-09-30