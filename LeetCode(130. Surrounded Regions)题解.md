# LeetCode(130. Surrounded Regions)题解
------
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

    X X X X
    X O O X
    X X O X
    X O X X
After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X
Explanation:

    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

## 解题思路
给一个二维矩阵，将其中被X包围的O都给替换成X。

这题可以看做是图的广度遍历。虽然图的深度遍历也可以做，但是对本题而言，会超时。矩阵过大时，递归栈会变得很深。 

思路是： 

因此可以使用队列的方式，将边缘的O全部转化成#，最后遍历矩阵遇到的O说明都是没有和边缘挨着的，是被包围的，最后将O变为X，将#变为O；

代码如下：

Runtime: 24 ms, faster than 98.26% of C++ online submissions for Surrounded Regions.
Memory Usage: 14.2 MB, less than 56.97% of C++ online submissions for Surrounded Regions.

```c++
struct pos{
    int i,j;
    pos(int a, int b){
        i = a; j = b;
    }
};
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int row, col;
        if(board.size() ==0 || board[0].size() == 0) return;
        row = board.size();
        col = board[0].size();
        int u = 0, d = row-1, l = 0, r = col-1; 
        queue<pos> Q;
        for(int i=0; i<col; i++){
            if(board[0][i] == 'O'){
                Q.push(pos(0,i));
                board[0][i] = '#';
            }
            if(board[row-1][i] == 'O'){
                Q.push(pos(row-1,i));
                board[row-1][i] = '#';
            }
        }
        for(int i=1; i<row-1; i++){
            if(board[i][0] == 'O'){
                Q.push(pos(i,0));
                board[i][0] = '#';
            }
            if(board[i][col-1] == 'O'){
                Q.push(pos(i, col-1));
                board[i][col-1] = '#';
            }
        }
        while(!Q.empty()){
            pos t = Q.front(); Q.pop();
            if(t.i>0 && board[t.i-1][t.j] == 'O'){
                board[t.i-1][t.j] = '#';
                Q.push(pos(t.i-1,t.j));             
            }
            if(t.i<row-1 && board[t.i+1][t.j] == 'O'){
                board[t.i+1][t.j] = '#';
                Q.push(pos(t.i+1,t.j));             
            }
            if(t.j>0 && board[t.i][t.j-1] == 'O'){
                board[t.i][t.j-1] = '#';
                Q.push(pos(t.i,t.j-1));             
            }
            if(t.j<col-1 && board[t.i][t.j+1] == 'O'){
                board[t.i][t.j+1] = '#';
                Q.push(pos(t.i,t.j+1));             
            }
        }
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if( board[i][j] == '#') board[i][j] = 'O';
                else if(board[i][j] == 'O') board[i][j] = 'X';
            }
        }
        return;
    }
};
```

BitBrave, 2019-07-07
