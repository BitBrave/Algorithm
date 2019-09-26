# LeetCode(223. Rectangle Area)题解

Find the total area covered by two **rectilinear** rectangles in a **2D** plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![Rectangle Area](https://assets.leetcode.com/uploads/2018/10/22/rectangle_area.png)

**Example:**

```
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
```

**Note:**

Assume that the total area is never beyond the maximum possible value of **int**.

## 解题思路

求两个矩阵的面积和，矩形之间有可能重叠。

这个题乍一看很简单，两个矩形面积分别算出来再减去重叠部分的面积就可以了。但是真正分析重叠的时候又会有点复杂。不过实际上也确实很简单。两个矩形无非三种状态，相交、相离、包含。其中相离和包含比较容易判断和计算，但是相交的情况就比较复杂了。可以这样分别讨论，但是情况有点多。

我们可以这样想，两个矩形的重叠部分也一定是个矩形，那么直接求出重叠矩阵的左下角和右上角矩阵不就可以了么。那么如何求呢，这个重叠矩阵左下角的坐标值，x，y一定是两个矩阵中各自坐标的较大值，而右上角坐标值一定是两个矩阵对应位置的较小值，这样就求出来了。

但是注意，如果两个矩阵是分离的，那这个重叠矩阵是不存在的，求出的坐标左下角肯定高于右上角，因此需要判断一下，如果右上角减左下角为负数的话，重叠矩阵的面积设为0即可。

代码如下，时间复杂度$O(1)$，空间复杂度$O(1)$:

`Runtime: 72 ms, faster than 8.08% of Python3 online submissions for Rectangle Area.`

`Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Rectangle Area.`

```Python
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C-A) * (D-B) + (G-E) * (H-F)
        # overlap
        x1, y1 = max(A, E), max(B, F)
        x2, y2 = min(C, G), min(D, H)
        
        return area - max(0, x2 - x1) * max(0, y2 - y1)
```

BitBrave, 2019-09-26