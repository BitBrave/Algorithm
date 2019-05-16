# LeetCode(36. Valid Sudoku)题解
------
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

[A partially filled sudoku which is valid.](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

    Input:
    [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true
Example 2:

    Input:
    [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being 
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.

## 解题思路
一个Medium题，给一个9*9的数组，其中每行每列和每个3*3的小区域都要符合数独规则。判断这样的一个input是否合法。给定的数组内有数组和"·"，其中"·"表示空，不用填充，直接跳过不用管。

这个主要就是如何计算小区域的坐标。

对于行来说，横坐标为i，纵坐标为0到8（每次增1）

对于列来说，横坐标为0到8，纵坐标为i（每次增1）

对于小区域来说，左上角为（i，j）则其余每个位置为（i+内部行位置，j+内部列位置）

然后直接各自的区域内是否有重复即可。

代码如下：

Runtime: 8 ms, faster than 99.98% of C++ online submissions for Valid Sudoku.
Memory Usage: 9.4 MB, less than 98.82% of C++ online submissions for Valid Sudoku.

```c++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool pos[10];

        // Raw
        for(int i=0; i<9; i++){
            memset(pos,0,sizeof(pos));
            for(int j=0; j<9; j++){
                if(board[i][j]=='.') continue;
                if(pos[board[i][j]-'0']) return false;
                pos[board[i][j]-'0'] = true;
            }
        }
        //Col
        for(int j=0; j<9; j++){
            memset(pos,0,sizeof(pos));
            for(int i=0; i<9; i++){
                if(board[i][j]=='.') continue;
                if(pos[board[i][j]-'0']) return false;
                pos[board[i][j]-'0'] = true;
            }
        }
        //Region3*3
        for(int i=0; i<=6; i+=3){
            for(int j=0; j<=6; j+=3){
                memset(pos,0,sizeof(pos));
                for(int ii=0; ii<3; ii++){
                    for(int jj=0; jj<3; jj++){
                        if(board[i+ii][j+jj]=='.') continue;
                        if(pos[board[i+ii][j+jj]-'0']) return false;
                        pos[board[i+ii][j+jj]-'0'] = true;
                    }
                }
            }
        }
        return true;
    }
};
```

BitBrave, 2019-05-14
