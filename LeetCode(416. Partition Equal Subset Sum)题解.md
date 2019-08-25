# LeetCode(416. Partition Equal Subset Sum)题解
------
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.
 
Example 1:

    Input: [1, 5, 11, 5]

    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].
    
Example 2:

    Input: [1, 2, 3, 5]

Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.

## 解题思路
将一个集合分成元素和相同的两个子集。

分成两个相同子集，那么这个原本的集合元素之和应该为偶数，每个子集和为这个数的二分之一，那么这个题就是找一些元素，看看能不能满足其和为这个数的二分之一。这个题能使用DP的办法。类似于一个背包的题目，背包容量为数组中元素和的一半+1，这样只要看是否有元素可以正好填满背包即可．但是每个元素只能用一次，所以在尝试放一个元素的时候还要避免他对尝试放其他位置时对自己的影响．所以在尝试放一个元素到背包的时候需要从容量最大的位置开始，如果（当前位置－当前元素大小）位置可以通过放置之前的元素达到，则当前位置也可以通过放置当前元素正好达到这个位置．状态转移方程为：dp[i] = dp[i] || dp[i - nums[k]];

代码如下：时间复杂度o(n*sum(n)),空间复杂度o(sum(n))

Runtime: 176 ms, faster than 24.77% of C++ online submissions for Partition Equal Subset Sum.
Memory Usage: 8.4 MB, less than 94.12% of C++ online submissions for Partition Equal Subset Sum.

```C++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int len = nums.size(), tar = 0;
        for(int i:nums) tar += i;
        
        if(tar & 1) return false;
        else tar /= 2;
        
        vector<bool> res(tar+1, false);
        res[0] = true;
        
        for(int i=0; i<len; i++){
            for(int j=tar; j>=nums[i]; j--){
                res[j] = res[j] || res[j-nums[i]];
            }
        }
        return res[tar];
    }
};
```

BitBrave, 2019-08-25
