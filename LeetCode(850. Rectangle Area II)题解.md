# LeetCode(850. Rectangle Area II)题解

We are given a list of (axis-aligned) `rectangles`.  Each `rectangle[i] = [x1, y1, x2, y2] `, where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the `i`th rectangle.

Find the total area covered by all `rectangles` in the plane.  Since the answer may be too large, **return it modulo 10^9 + 7**.

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)

**Example 1:**

```
Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
```

**Example 2:**

```
Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
```

**Note:**

- `1 <= rectangles.length <= 200`
- `rectanges[i].length = 4`
- `0 <= rectangles[i][j] <= 10^9`
- `The total area covered by all rectangles will never exceed `2^63 - 1` and thus will fit in a 64-bit signed integer.`

## 解题思路

给出一些矩阵，求出这些矩阵的面积之和（有的矩阵之间有重叠）。

首先考虑两个矩阵，只有三种情况，相交、相离、想含。其中相离合相含是比较好分析的，相交则有些复杂。但是这三种皆可以将两个矩阵分成几个不相交的矩阵，如相交可以分成三个（一个原始矩阵，另一个矩阵分割为两个）。

因此，我们可以维护一个List或者Vector，存储不相交的矩阵。将所有输入的矩阵通过分割全部转为相离的矩阵存入这个数组，最后只需计算这些矩阵的面积和即可。

如何来构建并维护这个数组呢？分别遍历这些矩阵，当输入一个矩阵时，分别判断这个矩阵是否与List中的每个矩阵相交相离或包含，如果除了相离之外的其他关系，就将输入的矩阵进行分割，再分别判定分割完的矩阵与其他数组内矩阵的位置关系，直到分割完的矩阵与数组内所有矩阵都处于相离关系。每次在判断第i+1个矩阵的时候，数组内矩阵会最多增加4i+4个。最终上限为N个矩阵的话有 $ 2N^2 - 1$个。

这里有一个对应的解法，[点击进入](https://leetcode.com/problems/rectangle-area-ii/discuss/138028/Clean-Recursive-Solution-Java)。

代码如下，时间复杂度$O(n^2)$，空间复杂度$O(n^2)$。

`Runtime: 124 ms, faster than 6.09% of C++ online submissions for Rectangle Area II.`

`Memory Usage: 64.5 MB, less than 25.00% of C++ online submissions for Rectangle Area II.`

```C++
class Solution {
    vector<vector<int>> V;
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int res = 0;
        int mod = pow(10, 9) + 7;
        int a, b;
        
        for(vector<int> rec : rectangles) addRectangle(rec, 0);
        for(vector<int> v : V){
            a =  (v[2]-v[0]) % mod;
            b =  (v[3]-v[1]) % mod;
            res = (res + ((long)a * (long)b) % mod) % mod;  
        } 
        return res;
    }
    
    // 判断rec与V中第start开始的矩阵位置情况，并决定是否需要进入start+1的情况。
    void addRectangle(vector<int> rec, int start){
        if(start >= V.size()){
            V.push_back(rec);
            return;
        }
        // 相交？
        if(rec[0] > V[start][2] or rec[2] < V[start][0] or rec[1] > V[start][3] or rec[3] < V[start][1]) return addRectangle(rec, start + 1);
        
        // 左边相交？
        if(rec[0] < V[start][0]) addRectangle(vector<int>({rec[0], rec[1], V[start][0], rec[3]}), start + 1);
        // 右边相交？
        if(rec[2] > V[start][2]) addRectangle(vector<int>({V[start][2], rec[1], rec[2], rec[3]}), start + 1);
        // 下边相交？
        if(rec[1] < V[start][1]) addRectangle(vector<int>({max(rec[0], V[start][0]), rec[1], min(rec[2], V[start][2]), V[start][1]}), start + 1);
        // 上边相交？
        if(rec[3] > V[start][3]) addRectangle(vector<int>({max(rec[0], V[start][0]), V[start][3], min(rec[2], V[start][2]), rec[3]}), start + 1);
        
        return;
    }
};
```

BitBrave, 2019-09-027
