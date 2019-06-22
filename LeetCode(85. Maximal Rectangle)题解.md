# LeetCode(85. Maximal Rectangle)题解
------
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

    Input:
    [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
    Output: 6


## 解题思路
给出一个矩阵，里面有的为1有的为0，求出全部为1的公共矩阵最大面积。

实在是想不出来。于是网上搜了搜解法，这里给各位大佬跪了。

[详细解答](https://www.cnblogs.com/lupx/archive/2015/10/20/leetcode-85.html)

上述的帖子内，DP的left和right的解释有些问题，因为会无法处理像漏斗状的1的形状的面积。改进如下：

### [DP]理论时间复杂度O(n2)，空间复杂度O(n)。
这个并不算是常规普通的DP，他用了三个数组，然后每次按行遍历。height记录遍历到当前行上时，每一列的1的个数（必须到当前行时1连续的数目，比如如果当前行的对应列的值为0，那么height记录为0），left记录遍历到当前行时对应列的值在所有行中从0列到当前位置的最后一个第一次遇到的1的位置。right记录遍历到当前行时对应列的值在所有行中从最后一列到当前位置的最后一个第一次遇到的0的位置。

一行遍历完成后，计算height[j]*(right[j]-left[j])的最大值记录即可。

这里left和right的赋值需要斟酌，在计算时，如果查到对应的height为0，即当前遇到了0，那么之前的左边界右边界就全部作废了。将设置left[j] = 0; right[j] = COL;意味着一切重新开始。(我真是优秀)

代码如下：

Runtime: 20 ms, faster than 95.62% of C++ online submissions for Maximal Rectangle.
Memory Usage: 10.4 MB, less than 96.17% of C++ online submissions for Maximal Rectangle.

```c++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return 0;
        int row = matrix.size(), col = matrix[0].size();
        int res = 0, leftBound, rightBound = 0;
        vector<int> height(col, 0), left(col, 0), right(col, col);
        
        for(int i=0; i<row; i++){
            leftBound = 0;
            rightBound = col;
            
            for(int j=0; j<col; j++){
                if(matrix[i][j]=='1') {
                    height[j]++;
                    left[j] = max(left[j], leftBound);
                }
                else{
                    height[j] = 0;
                    left[j] = 0; right[j] = col;
                    leftBound = j + 1;
                }
            }
            
            for(int j=col-1; j>=0; j--){
                if(matrix[i][j]=='1') right[j] = min(right[j], rightBound);
                else rightBound = j;
            }
            for(int j=col-1; j>=0; j--) res = max(res, height[j] * (right[j] - left[j]));
        }
        return res;
    }
};
```

### [递增栈法]，时间复杂度O(n2)，空间复杂度O(n)。

这一题跟84题放一块是有道理。如果只看一行的话，这其实就是一个简化版的84题，可以直接使用84题的解法。

因此，还是按行遍历，同样使用height数组记录遍历到当前行时每一列在当前连续的1的个数，然后使用84题的解法即可。

代码如下(速度稍慢，因为有入栈出栈)：

Runtime: 24 ms, faster than 84.22% of C++ online submissions for Maximal Rectangle.
Memory Usage: 13 MB, less than 8.15% of C++ online submissions for Maximal Rectangle.

```c++
class Solution {
public:
    //84
    int largestRectangleArea(vector<int> height) {
        height.push_back(0);
        int res = 0, len = height.size(), tmp;
        stack<int> s;
        for(int i=0; i<len; i++){
            if(s.empty() || height[s.top()]<=height[i]) s.push(i);
            else{
                tmp = s.top(); s.pop();
                res = max(res, height[tmp]*(s.empty() ? i : i - s.top() - 1));
                i--;
            }   
        }
        return res;
    }
    //85
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return 0;
        int row = matrix.size(), col = matrix[0].size();
        int res = 0;
        vector<int> height(col, 0);
        
        for(int i=0; i<row; i++){            
            for(int j=0; j<col; j++){
                if(matrix[i][j]=='1') height[j]++;
                else height[j] = 0;       
            }
            res = max(res, largestRectangleArea(height));
        }
        return res;
    }
};
```

BItBrave，2019-06-22

