# LeetCode(84. Largest Rectangle in Histogram)题解
------
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)

![The largest rectangle is shown in the shaded area, which has area = 10 unit.](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)

Example:

    Input: [2,1,5,6,2,3]
    Output: 10

## 解题思路
求给定的矩形集合内，在宽都为1，依次排列在一起，得到的最大的公共矩阵面积。

我能想到的就是一个O(n2)的暴力枚举，果然不出意外的TLE了。

然后上网搜了搜别人的解法。

### [局部峰值法](http://fisherlei.blogspot.com/2012/12/leetcode-largest-rectangle-in-histogram.html)理论时间复杂度O(n2)，空间复杂度O(1)。但进行了优化。

从左到右遍历数组M，到达位置i，如果当前值大于接下来的一个，就求出当前数组在包含i在内的矩阵的公共最大面积。否则直接跳过。这是为什么可以AC呢？首先就是这个肯定可以得到正确答案，因为一个最优的答案中，边界值相邻的矩阵一定是低于边界的矩阵的或者就在矩阵集合的边界上。而局部峰值就涵盖了前面较低矩阵的时候的计算，因为其值一定小于加上后面高的矩阵的值。因此等于兼枝。但是如果数组是递减的，就只能老老实实一个个试了。

代码如下：

Runtime: 8 ms, faster than 99.77% of C++ online submissions for Largest Rectangle in Histogram.
Memory Usage: 9.9 MB, less than 92.71% of C++ online submissions for Largest Rectangle in Histogram.

```c++
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        int res = 0, len = height.size(), s;
        for(int i=0; i<len; i++){;
            if((i+1)<len && height[i]<=height[i+1]) continue;
            s = height[i];
            for(int j=i; j>=0; j--){
                s = min(s, height[j]);
                res = max(res, s*(i-j+1));
            }
        }
        return res;
    }
};
```

### [递增栈](http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html)，时间复杂度O(n)，空间复杂度O(n)。

从左到右遍历矩阵数组M，设计一个stack存储位置元素，遇到当前位置i，查看M[i]，栈空，就入栈，如果不空查看M[i]是否比栈顶元素对应的矩阵小。如果大于，就i入栈，如果小于就出栈直到剩下的栈顶元素k对应的矩阵值M[k]小于M[i]。然后以最后退出的栈顶元素乘上(i-k-1)，这个过程中总是记录对应乘积的最大值.

正确定证明：可以知道这个栈是递增栈。每次遇到需要出栈的情况，第一次一定是栈顶元素的位置和当前遍历到的元素位置相邻，因为如果不相邻，那么这个栈顶元素应早就需要出栈了。然后一直出栈到栈顶元素比当前元素低，那么这个过程中一直计算的最大值实际上是矩阵均比M[i]高的矩阵形成的最大面积。出栈之后如果栈不为空，表示从栈顶元素对应的位置和当前遍历的位置之间都是大于这两个的矩阵，宽就为这样之差再减1。如果栈空，表示当前遍历的值得矩阵比前面所有的都小，宽为当前位置。就这样一直到最后。因为低的围成的面积一定是小于高的围成的面积。但是也不一定，如果低的很远，那么靠宽也有可能得到。因此，需要在最后矩阵后面的元素内再添加0。这样原本的最后一个元素可以入栈然后出栈，从而将矮的也能够计算出来。因为所有的元素只会操作一次，因此时间复杂度是O(n)。

代码如下：

Runtime: 16 ms, faster than 68.22% of C++ online submissions for Largest Rectangle in Histogram.
Memory Usage: 10.7 MB, less than 21.35% of C++ online submissions for Largest Rectangle in Histogram.

```c++
class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
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
};
```

BItBrave，2019-06-19

