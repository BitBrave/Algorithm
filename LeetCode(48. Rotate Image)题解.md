# LeetCode(48. Rotate Image)题解
------
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

    Given input matrix = 
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]
Example 2:

    Given input matrix =
    [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
    ], 

    rotate the input matrix in-place such that it becomes:
    [
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
    ]


## 解题思路
Medium，将一个矩阵顺时针旋转90度，要求不能分配新的内存，即只能在原来的矩阵上操作，这其实是有一点难度。

但是，想通了其实异常简单。比如原来矩阵中（i，j）位置的元素在新的矩阵中为（j，n-1-i），而（j，n-1-i）对应的是（n-1-i，n-1-j），而（n-1-i，n-1-j）对应的是（n-1-j，i），（n-1-j，i）对应的是（i，j）相当于四个一循环，因此，直接将这四个换一下即可。

但是需要注意，因为是一次换了四个，所以不能简单地循环整个矩阵，遇到一个数就换，因为有可能之前已经换完了。如果都换一次的话，最后其实是又变成原样子了。
因此需要在遍历矩阵的时候判断当前值是否需要换，如果已经换了就不用换了。

这里我采用的策略如下：从左到右，按行遍历矩阵，当到（i，j）的时候，判断（j，n-1-i）、（n-1-i，n-1-j）、（n-1-j，i）是否在（i，j）的左上边或者上边，如果是的话说明这一组数已经换过了，直接跳过，否则就没换。

C++代码如下（C++确实比Python快）：

Runtime: 4 ms, faster than 98.21% of C++ online submissions for Rotate Image.
Memory Usage: 9.2 MB, less than 38.55% of C++ online submissions for Rotate Image.

```C++
class Solution {
public:
    bool isrotate(int i, int j, int a, int b){
        return a<i || (a==i && b<j);
    }     
    void rotate(vector<vector<int>>& matrix) {
        int l = matrix.size();
        int tmp;
        
        for(int i=0; i<l; i++){
            for(int j=0; j<l; j++){
                if(isrotate(i, j, j, l-1-i)||isrotate(i, j, l-1-i, l-1-j)||isrotate(i, j, l-1-j, i)) continue;
                tmp = matrix[l-1-j][i];
                matrix[l-1-j][i] = matrix[l-1-i][l-1-j];   
                matrix[l-1-i][l-1-j] = matrix[j][l-1-i];
                matrix[j][l-1-i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
        return;
    }
};
```

python代码如下（注意&|的括号问题）：

Runtime: 48 ms, faster than 20.15% of Python3 online submissions for Rotate Image.
Memory Usage: 13.2 MB, less than 43.67% of Python3 online submissions for Rotate Image.

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def isrotate(i, j, a, b):
            return (a<i) | ((a==i) & (b<j))
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l):
            for j in range(l):
                if(isrotate(i, j, j, l-1-i)|isrotate(i, j, l-1-i, l-1-j)|isrotate(i, j, l-1-j, i)): continue
                tmp = matrix[l-1-j][i]
                matrix[l-1-j][i] = matrix[l-1-i][l-1-j]   
                matrix[l-1-i][l-1-j] = matrix[j][l-1-i]
                matrix[j][l-1-i] = matrix[i][j]
                matrix[i][j] = tmp

        return
```

BitBrave，2019-5-19