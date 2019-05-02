# LeetCode(55. Jump Game)题解
------
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                jump length is 0, which makes it impossible to reach the last index.

## 解题思路

Medium题，给一个数组，从左向右开始，每一个位置上的元素代表着从当前位置可以向前走的最大步数。问是否存在一种方法可以从左走到右。存在返回True，不存在返回False。一种思路是直接使用递归，类似于DFS，但这样会超时，虽然代码简洁优美，但没什么卵用。

一个值得注意的事就是，当数组内所有数都大于0，意味着数组肯定可以走到最右边，因为一步步走就可以了。那么就只需要判断0存在的情况下能不能越过。如果一个元素为0，代表走到这个位置就不能移动了。所以，我们可以在这个元素之前寻找一个值，其可以越过这个0，如果越过了，就直接走最远的地方（贪心），然后剩下的情况跟刚刚一样。如果找完所有的都不能越过这个0，那么就说明不存在一条路。返回False。

代码如下：

```c++
class Solution {
public:
    int findzeropos(vector<int>& nums, int sta, int size){
        while(sta<size){
            if(nums[sta++]==0) return --sta;
        }
        return sta;
    }
    bool canJump(vector<int>& nums) {
        if(nums.size()<=1) return true;
        int p = 0, len = nums.size(), zero_p = 0;
        zero_p = findzeropos(nums, 0, len);
        if(zero_p>=len-1) return true;
        
        for(int i=zero_p-1; i>=0; i--){
            if(++p<nums[i]){
                i = findzeropos(nums, i+nums[i], len);
                if(i>=len-1) return true;
                p=0;
            }
        }
        return false;
    }
};
```

BitBrave，2019-05-02