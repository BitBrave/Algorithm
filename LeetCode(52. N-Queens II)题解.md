# LeetCode(52. N-Queens II)题解
------
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

    Input: 4
    Output: [
    [".Q..",  // Solution 1
    "...Q",
    "Q...",
    "..Q."],

    ["..Q.",  // Solution 2
    "Q...",
    "...Q",
    ".Q.."]
    ]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

## 解题思路(与51题一模一样)
Hard，这道题的要求是N皇后问题：放置n的皇后在n*n的棋盘上，使其任意两个皇后不能相互攻击。给定整数n，返回所有可能情况，其中‘Q’表示皇后，‘.’表示空位置。

两个皇后不能相互攻击，即要求这两个皇后不在同一行、同一列及同一斜线上。

可以使用一个N维数组记录每一行上的皇后位置，使用递归计算。递归到当前行时，从1到n查看是否可以放皇后，放置的条件就是不能与前面的皇后在同一列（可以比较值是否相同，相同就在同一列），不能在同一个斜线上（当前行与当前列的差值相同则在同一个\斜线，当前行与当前值的和相同则在同一个/斜线）。

代码如下，速度有点慢，懒得优化了：

Runtime: 28 ms, faster than 13.38% of C++ online submissions for N-Queens II.
Memory Usage: 16.4 MB, less than 6.86% of C++ online submissions for N-Queens II.

```c++
class Solution {
public:
    bool isValid( vector<int> tmp, int pos, int len, int n){
        for(int i=0; i<len; i++){
            if(tmp[i]==pos) return false;
            if((len-pos) == (i-tmp[i])) return false;
            if((len+pos) == (i+tmp[i])) return false;
        }
        return true;
    }
    int solveNQueens_(int n, vector<int> tmp, int len){
        if(len==n) return 1;
        int res = 0;
        for(int i=0; i<n; i++){
            if(!isValid(tmp, i, len, n)) continue;
            tmp[len] = i;
            res += solveNQueens_(n, tmp, len+1);
        }
        return res;
    }
    int totalNQueens(int n) {
        if(n==0) return 0;
        
        vector<int> tmp(n);
        
        return solveNQueens_(n, tmp, 0);
    }
};
```

BitBrave，2019-05-29.