# LeetCode(861. Score After Flipping Matrix)题解

We have a two dimensional matrix `A` where each value is `0` or `1`.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all `0`s to `1`s, and all `1`s to `0`s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

**Example 1:**

```
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```

**Note:**

1. `1 <= A.length <= 20`
2. `1 <= A[0].length <= 20`
3. `A[i][j]` is `0` or `1`.

## 解题思路

有一个二维矩阵，元素为0和1.给定针对行或者列的操作，将元素依次翻转，0变为1,1变为0.在做了一些翻转操作之后，矩阵有一个得分就是每一行的元素组成的一个二进制数之和。

求这个数最大是多少？

首先，一个二进制数，只要前面的为1，后面全为0也可以变得很大，即1需要尽可能在前面。因此，我们采用一个贪心的Algorithm：首先对每一行进行遍历，只要这一行第一个数为0，就进行翻转，否则就不翻转，因为翻转就 变小了。然后遍历每一列，只要这一列中1的个数少于0的个数，就进行翻转，因为这些数处于同级的关系，要尽可能多的变成1，否则就不翻转。

实验证明是可行的。

代码如下，空间复杂度O(1)，时间复杂度O(n2)。

`Runtime: 4 ms, faster than 67.24% of C++ online submissions for Score After Flipping Matrix.`

`Memory Usage: 9 MB, less than 20.00% of C++ online submissions for Score After Flipping Matrix.`

```C++
class Solution {
    vector<vector<int>> B;
public:
    void flipping(int pos, int dir, int len){
        if(dir == 0){
            for(int i = 0; i < len; i++) B[pos][i] = 1 - B[pos][i];
        }
        else if(dir == 1){
            for(int i = 0; i < len; i++) B[i][pos] = 1 - B[i][pos];
        }
        return;
    }
    int matrixScore(vector<vector<int>>& A) {
        int res = 0, row = A.size(), col = A[0].size();
        B = A;
        for(int i=0; i<row; i++){
            if(B[i][0] == 0) flipping(i, 0, col);
        }
        int t;
        for(int j=0; j<col; j++){
            t = 0;
            for(int i=0; i<row; i++) t += B[i][j];
            if(t*2 < row) flipping(j, 1, row);
            
            // Compute
            t = 0;
            for(int i=0; i<row; i++) t += B[i][j];
            res += t * pow(2, col - 1 - j);
        }
        return res;
    }
};
```

BitBrave, 2019-09-29