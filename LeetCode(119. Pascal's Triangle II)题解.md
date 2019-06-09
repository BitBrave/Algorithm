# LeetCode(119. Pascal's Triangle II)题解
------
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


![In Pascal's triangle, each number is the sum of the two numbers directly above it.](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Example:

    Input: 3
    Output: [1,3,3,1]
Follow up:

    Could you optimize your algorithm to use only O(k) extra space?

## 解题思路
Easy，就是简单计算一下杨辉三角（帕斯卡三角）在给定的第N行的数而已。其中第N行由上一行的数相邻相加得到2到n-1的数。最两边为1.第一行为1.

一个简单的for循环就可以了。

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Pascal's Triangle II.
Memory Usage: 8.5 MB, less than 46.65% of C++ online submissions for Pascal's Triangle II.

```c++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1, 1);
        for(int i=2; i<rowIndex+1; i++){
            for(int k=i-1; k>0; k--) res[k] += res[k-1];
        }
        
        return res;
    }
};
```

BitBrave, 2019-06-09