# LeetCode(\948. Bag of Tokens)题解

You have an initial power `P`, an initial score of `0` points, and a bag of tokens.

Each token can be used at most once, has a value `token[i]`, and has potentially two ways to use it.

- If we have at least `token[i]` power, we may play the token face up, losing `token[i]` power, and gaining `1` point.
- If we have at least `1` point, we may play the token face down, gaining `token[i]` power, and losing `1` point.

Return the largest number of points we can have after playing any number of tokens.

**Example 1:**

```
Input: tokens = [100], P = 50
Output: 0
```

**Example 2:**

```
Input: tokens = [100,200], P = 150
Output: 1
```

**Example 3:**

```
Input: tokens = [100,200,300,400], P = 200
Output: 2
```

 

**Note:**

1. `tokens.length <= 1000`
2. `0 <= tokens[i] < 10000`
3. `0 <= P < 10000`

## 解题思路

给一个数组，每个元素表示一个能量，同时给定一个初始能量P。现在每选中一个元素需要花费对应元素值的能力，但能得一分。或者选中一个元素花掉一分，但能得到对应元素值的能量，一个元素只能用一次。问如何能得到最多的分，返回最多的分值。

这个题可以使用贪心，因为我们可以这样想，我们需要尽可能得到更多的分，那就用尽可能少的能量买更多的分，因此我们用能量去买元素值低的分，同时我们也要获得更多的能量去买分。因此当发现能量不够时，我们去花费分购买最多的元素值分。在这个过程中记录最大值。可以非常简单证明这一定是最优解。因为如果有一个最优解方案不是这样得出的，那么一定可以调整成这样的方案，同时不改变最优值。

代码如下，时间复杂度O(nlogn), 空间复杂度O(1)。

`Runtime: 8 ms, faster than 74.68% of C++ online submissions for Bag of Tokens.`

`Memory Usage: 8.7 MB, less than 66.67% of C++ online submissions for Bag of Tokens.`

```c++
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int P) {
        int ret = 0, sta = 0, end = tokens.size() - 1, M = P, p = 0;
        sort(tokens.begin(), tokens.end());
        while(sta <= end){
            if(M >= tokens[sta]){
                M -= tokens[sta++];
                p++;
            }
            else if(p > 0){
                ret = max(ret, p);
                p--;
                M += tokens[end--];
            }
            else break;
        }
        return max(ret, p);
    }
};
```

 BitBrave，2019-11-16