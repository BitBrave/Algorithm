# LeetCode(37. Sudoku Solver)题解
------
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    Empty cells are indicated by the character '.'.


![A sudoku puzzle...](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)


![...and its solution numbers marked in red.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

Note:

    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.

## 解题思路
Hard，给一个9*9的矩阵，其中每行每列和各3*3的小区域中有预先填写一些数。要求将剩下的空格填完，满足数组的要求。

一个思路就是使用DFS，当遇到一个空格，查看其行、列和小区域的其他值，确定可以填的数，填入一个之后进入下一个空格，如果这样下去可以成功直接结束算法。如果中途某个空格发现无法填数，则表示失败，返回上级递归。

代码如下：

Runtime: 28 ms, faster than 26.39% of C++ online submissions for Sudoku Solver.
Memory Usage: 13.8 MB, less than 14.64% of C++ online submissions for Sudoku Solver.

```C++
class Solution {
public:
    void fillableVal(vector<char> &tmp, vector<vector<char>>& board, int row, int col){
        bool val[9] = {true, true, true, true, true, true, true, true, true};
        int li, lj;
        // col
        for(int i=0; i<9; i++){
            if(board[i][col]!='.') val[board[i][col]-'1'] = false;
        }
        // row
        for(int j=0; j<9; j++){
            if(board[row][j]!='.') val[board[row][j]-'1'] = false;
        }
        // local area
        li = (row / 3) * 3;
        lj = (col / 3) * 3;
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++)
                if(board[li+i][lj+j]!='.') val[board[li+i][lj+j]-'1'] = false;
        }

        tmp.clear();
        for(int i=0; i<9; i++){
            if(val[i]) tmp.push_back('1'+i);
        }
        return;
    }
    bool SudoKu(vector<vector<char>>& board, int row, int col){
        if(col==9) {
            row += 1;
            col = 0;
        }
        if(row>=9) return true;
        if(board[row][col]!='.') return SudoKu(board, row, col+1);
        
        vector<char> tmp;
        int len;
        
        fillableVal(tmp, board, row, col);
        len = tmp.size();
        
        for(int k=0; k<len; k++){
            board[row][col] = tmp[k];
            if(SudoKu(board, row, col+1)) return true;
        }
        board[row][col] = '.';
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        SudoKu(board, 0, 0);
        return;
    }
};
```

BitBrave，2019-05-23
