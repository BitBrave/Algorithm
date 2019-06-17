# LeetCode(79. Word Search)题解
------
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

    board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.


# 解题思路
给一个记录多个字符的二维矩阵，再给出一个字符串，从矩阵中任意一个位置开始搜索，上下左右皆可，每个位置只能走一遍最多。查看是否可以在矩阵中找到这样一个字符串，找到返回true，没有返回false。

使用DFS，当前位置不符合返回true，否则从上下左右中继续寻找下一个。比如设置一个函数，传入参数矩阵，一个对应的位置矩阵，当前要比较的矩阵的位置，当前要比较的字符。有以下几种情况。

位置已经遍历过了，返回false。

位置还没有被遍历：

1 字符不合适，返回false
2 向上走，能OK就返回true。否则向下走，能OK就返回true，向左走，能OK就返回true，向右走，能OK就返回true，否则返回false。

代码如如下：
Runtime: 296 ms, faster than 26.74% of C++ online submissions for Word Search.
Memory Usage: 159.2 MB, less than 11.37% of C++ online submissions for Word Search.


```C++
class Solution {
public:
    bool dfs(vector<vector<char>>& board, vector<vector<bool>>& pos, int row, int col, int i, int j, string word, int sta, int len){
        if(sta>=len) return true;
        if(i<0 || i>=row) return false;
        if(j<0 || j>=col) return false;
        if(pos[i][j] == false) return false;
        if(board[i][j]!=word[sta]) return false;
        
        pos[i][j] = false;
        if(dfs(board, pos, row, col, i-1, j, word, sta+1, len)) return true;
        if(dfs(board, pos, row, col, i, j-1, word, sta+1, len)) return true;
        if(dfs(board, pos, row, col, i+1, j, word, sta+1, len)) return true;
        if(dfs(board, pos, row, col, i, j+1, word, sta+1, len)) return true;
        pos[i][j] = true;
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size(), col = board[0].size(), len = word.size();
        vector<vector<bool>> pos(row, vector<bool>(col, true));
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(dfs(board, pos, row, col, i, j, word, 0, len)) return true;
            }
        }
        return false;
    }
};
```

BitBrave, 2019-06-017