# LeetCode(128. Longest Consecutive Sequence)题解
------
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

    Your algorithm should run in O(n) complexity.

Example:

    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## 解题报告
给一个无序的整数数组。从中找出最大的子序列长度，其中元素是连续的，如1，2，3，4. 要求在O(n)的时间复杂度内得到结果。

可以使用Map，以数组元素为key，bool值为value，表示是否遍历到这个数。初始化map中所有元素为true。然后遍历数组，没遍历一个数组，查看对应map内是否为true，如果是就表示还没遇到，然后数组元素+1和-1分别向上和向下找，直到找不到或者遇到false（这其实是不会出现的）。然后把本身的Map标志为false。如果一开始就是false，表示之前已经遍历到了。直接放弃就好了。

代码如下：

Runtime: 16 ms, faster than 34.33% of C++ online submissions for Longest Consecutive Sequence.
Memory Usage: 10.2 MB, less than 32.71% of C++ online submissions for Longest Consecutive Sequence.

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 0, len = nums.size();
        map<int, bool> M;
        for(int i=0; i<len; i++) M[nums[i]] = true;
        
        for(int i=0; i<len; i++){
            if(M[nums[i]] == false) continue;
            int j = nums[i]+1, c = 0;
            M[nums[i]] = false;
            while(M.find(j) != M.end()) M[j++] = false;
            c = j - nums[i];
            j = nums[i] - 1;
            while(M.find(j) != M.end()) M[j--] = false;
            c += nums[i] - j - 1;
            res = max(res, c);
        }
        return res;
    }
};
```

BitBrave, 2019-07-17