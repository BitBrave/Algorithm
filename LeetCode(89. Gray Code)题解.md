# LeetCode(89. Gray Code)题解
------
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

    Input: 2
    Output: [0,1,3,2]
    Explanation:
    00 - 0
    01 - 1
    11 - 3
    10 - 2

    For a given n, a gray code sequence may not be uniquely defined.
    For example, [0,2,3,1] is also a valid gray code sequence.

    00 - 0
    10 - 2
    11 - 3
    01 - 1
Example 2:

    Input: 0
    Output: [0]
    Explanation: We define the gray code sequence to begin with 0.
                A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
                Therefore, for n = 0 the gray code sequence is [0].

## 解题思路
灰色代码是一个二进制数字系统，其中两个连续的值只相差一位。给定一个非负整数n表示代码中的总比特数，打印灰色代码序列。灰色代码序列必须以0开头。

直白的解释就是，对给定的n，设计n个01组成的序列，一共2的n次方个，一次排列，使得每个序列之间只相差一个字符。

可以使用类似于递归的办法解决（一个for循环就可以）。假设n-1的情况下有2的n-1次方个序列已经排好了，那个扩展到n的时候。首先将0加到所有序列之上，形成一个2的n-1次方个的序列集，按顺序存储。然后将所有开头的0换成1，倒顺序存储到序列集内。如此即完成了2的n次方的组合。

代码如下：

Runtime: 4 ms, faster than 92.85% of C++ online submissions for Gray Code.
Memory Usage: 8.6 MB, less than 57.17% of C++ online submissions for Gray Code.

```c++
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        int len = 1, t = 0;
        res.push_back(0);
        for(int i=0; i<n; i++){
            t = pow(2, i);
            for(int j=len-1; j>-1; j--) res.push_back(t + res[j]);
            len *= 2;
        }
        return res;
    }
};
```

BItBrave，2019-06-19

