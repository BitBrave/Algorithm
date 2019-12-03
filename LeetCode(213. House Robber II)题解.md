# LeetCode(\213. House Robber II)题解

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

**Example 1:**

```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

**Example 2:**

```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

## 解题思路

一个盗贼偷窃一排房屋，每个房屋内有一定的钱财，房屋是围成圆形的，盗贼只能在不相邻的房屋之间实施盗窃，否则就会触发警报。问如何能偷到最多的钱财。这个题形式化就是，从一个环形数组内，找出不相邻的数字相加得到最大的和。

这个可以使用DP解决。首先简单考虑，如果房屋不是环形的话，应该怎么处理，这就很简单了，直接定义一个状态数组D，D[i]表示盗贼从0房间开始到i房间能偷到的最多钱财，那么状态转移方程就是D[i]=max(D[i-1], D[i-2]+nums[i])。表示在当前房屋下选择偷与不偷之间的最大值。

现在如果变成环形的话，我们可以分析，那就是nums数组首尾不能同时都被偷，那么我们可以分别求出1到n和0到n-1的线性的最优解，然后二者取最大值即可。

代码如下，时间复杂度O(n)，空间复杂度O(n)。

`Runtime: 4 ms, faster than 58.56% of C++ online submissions for House Robber II.`

`Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for House Robber II.`

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size(), ret;
        if(len == 0) return 0;
        
        vector<int> D(len+2, 0);
        for(int i=0; i<len-1; i++){
            D[i+2] = max(D[i+1], nums[i]+D[i]);
        }
        ret = max(nums[0], D[len]);
        for(int i=1; i<len; i++){
            D[i+1] = max(D[i], nums[i]+D[i-1]);
        }
        return max(ret, D[len]);
    }
};
```


