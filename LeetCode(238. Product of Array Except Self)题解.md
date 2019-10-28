# LeetCode(238. Product of Array Except Self)题解

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example:**

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Note:** Please solve it **without division** and in O(*n*).

**Follow up:**
Could you solve it with constant space complexity? (The output array **does not** count as extra space for the purpose of space complexity analysis.)

## 解题思路

给定一个数组，针对每一个元素，返回数组中每个元素对应位置上除了这个元素之外的数组内所有元素的乘积。

乍一看是个很简单的题，但是这个不注意就会出错，首先是乘积，有可能会很大，其次是注意0的存在。如果数组内存在大于一个的0元素，那么所有位置的乘积都是0，但是如果只有一个0元素，那么0元素对应的位置的乘积不为0，其他位置为0，如果没有0元素，那么每个元素对应位置的乘积的值就都有。

所以要做好判断，但是理清了就好做了。

代码如下，时间复杂度O(n)，空间复杂度O(1)。

`Runtime: 36 ms, faster than 98.12% of C++ online submissions for Product of Array Except Self.`

`Memory Usage: 12.5 MB, less than 77.27% of C++ online submissions for Product of Array Except Self.`

```C++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long p = 1, len = nums.size(), n0 = 0;
        vector<int> ret(len, 0);
        for(int i=0; i<len; i++){
            if(nums[i] == 0){
                n0++;
                ret[i] = -1;
            } 
            else p *= nums[i];
        }
        while(len--){
            if(n0 > 1) ret[len] = 0;
            else{
                ret[len] = n0 == 1 ? (ret[len]==-1 ? p:0) :  p/nums[len];
            }
        }
        return ret;
    }
};
```

BitBrave，2019-10-28