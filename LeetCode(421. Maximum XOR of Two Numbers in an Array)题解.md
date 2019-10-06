# LeetCode(421. Maximum XOR of Two Numbers in an Array)题解

Given a **non-empty** array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ *i*, *j* < *n*.

Could you do this in O(*n*) runtime?

**Example:**

```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

## 解题思路

给一个数组，从中找出两个数，使得其异或值最大，返回这个异或之后的结果。

这个题可以使用最简单的，就是挨个比，时间复杂度O(n2)。但是题目提示可以在O(n)时间内完成。

利用异或的特性，我们可以完成这个题目。对于异或运算，可知 `a^b=c <==> a^c=b`。即三个数两两异或可以推出第三个数。因此，可以考虑使用这个性质，用位比较的方式得到答案。

解法如下：

根据题目可知，所有的数都不会超过32位，因此每个数都可以用一个32位的二进制数进行表示。然后从最高位开始，将所有数的最高位放入一个set中，依次将这些最高位与1进行异或运算，如果得到的结果仍旧在set中，说明最终答案的最高位一定为1，否则为0.因为如果在表示set一定有两个数，其异或结果的最终值在最高位一定为1.(由定理可得1 ^ x = b <==> b ^ x = 1, 对与数x, 一定存在一个数b, 使得x ^ b = 1), 否则最高位的答案一定为0.

继续进行下去，假设我们已经知道最终答案的最高k位为prefix, 我们先将数列中所有数的最高k+1位存入Set中. 然后, 我们假设下一位的值为1, 将数列中所有数的最高前k+1位与prefix<<1 + 1进行异或运算, 如果异或得到的结果仍然在Set中, 那么说明最终答案的第k+1位一定为1, 否则, 最高位的答案一定为0.

因为x ^ (prefix<<2+1) = b　<==> x ^ b = prefix<<2+1, 即对于数x, 一定存在一个数b, 使得他们异或的结果为prefix<<2+1.

因此, 我们可以对最终答案的32位进行依次判断, 最终得到异或的最大值.

代码如下，算法的时间复杂度为`O(32n) = O(n)`，空间复杂度为 `o(n)`.

`Runtime: 208 ms, faster than 15.60% of C++ online submissions for Maximum XOR of Two Numbers in an Array.`

`Memory Usage: 40.5 MB, less than 80.00% of C++ online submissions for Maximum XOR of Two Numbers in an Array.`

```C++
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int res = 0, len = nums.size();
        
        for(int k=31; k>=0; k--){
            // fill set
            set<int> S;
            for(int i=0; i<len; i++) S.insert(nums[i]>>k);
            
            // find
            res = res<<1 | 1;
            set<int>::iterator iter;
			for(iter=S.begin(); iter!=S.end(); iter++){
				if(S.find(*iter ^ res) != S.end()) break;
			}
            if(iter == S.end()) res ^= 1;
        }
        return res; 
    }
};
```

BitBrave，2019-10-04