# LeetCode(137. Single Number II)题解
------
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

    Input: [2,2,3,2]
    Output: 3
Example 2:

    Input: [0,1,0,1,0,1,99]
    Output: 99

## 解题思路
给出一个数组，其中一个数出现了1次，其余所有数出现了三次，要求找出出现1次的数。并且尽量在线性时间和常量空间内得到结果。

这个题是136的升级版，原来是其余数出现两次，可以使用异或的办法，因为相同数异或为0，而0异或任何数都等于原来的数。这个题变成了有三个一样的数，因此就不能简单的使用异或问题了。

可以这样思考，把所有数都想象成二进制形式。那么对于每一位二进制位数上的数，假设出现只考虑出现三次的数，那么对应位置上的数一定一样，即如果是1就出现3次，是0页出现3次。因此位数上的值之和一定可以整除3. 现在加入只出现1次的，如果对应位上为1而别的数对应为0，那么肯定不能整除3，如果别的位置上为1，那么对应为之和也不能整除3，如果对应位上为0，那么不管别的数对应位上是什么，其和一定是可以整除3的。

因此，结论如下，数组中所有数，对应二进制位上之和如果能整除3，表示只出现1次的数在对应位上为0，如果对应二进制位上之和不能整除3，表示只出现1次的数在对应为上为1. 这个结论同样适用于，其余数出现N次，只有一个数出现1次的情况。

代码如下：

Runtime: 8 ms, faster than 97.53% of C++ online submissions for Single Number II.
Memory Usage: 9.5 MB, less than 89.74% of C++ online submissions for Single Number II.

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> bits(32, 0);
        int res = 0, count = 0, len = nums.size();
        for(int i=0; i<len; i++){
            for(int j=0; j<32; j++){
                bits[j] += (nums[i] >> j) & 1;
            }
        }
        for(int i=0; i<32; i++){
            res += (bits[i]%3 == 0) ? 0 : (1 << i);
        }
        return res;
    }
};
```

BitBrave, 2019-07-16