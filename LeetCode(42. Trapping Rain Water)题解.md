# LeetCode(42. Trapping Rain Water)题解
------
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


![The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

## 题意理解
Hard，要求给定一个数组，表示在坐标轴内从左到右按照其值在y轴上组合成的一个形状，中间的组成一个凹陷的，计算其凹陷的大小，意思就是像一个个池塘，计算其能容纳多少水。

这个题可以使用stack的方式解决，时间复杂度O（n）。栈记录遇到的值，计算每次遇到值和之前的之间形成的大小，计算可以增加容纳的水。从左到右遍历数组，用一个值res记录可以容纳的水，初始化res=0。这里用一个小trick，我们入栈不入原始值，而是入坐标，从左到右遍历，遇到一个数b，坐标j，方式如下：

0 如果元素为0，直接跳过
1 如果栈为空，表示还未有边界，应该是第一个数，直接入栈。
2 查看栈顶元素i对应的数a，有如下几种情况

2-1 a小于等于b，表示a与b之间没有别的边界，直接res += （j-i-1）*a。然后弹出i，因为这之间的计算完毕，如果栈空则压入j。否则接着查看栈的新的栈顶元素k和对应的值c，就看新的栈顶元素是否比b大（应该是比b大的，栈记录的值都是递减的），如果是b大，计算新增加的容量，res += （c-a）*（j-k-1），然后弹出接着像之前的那样操作。如果是c大，这就计算res += （b-a）*（j-k-1），然后压入j。
2-2 a大于b，则直接res += （b）*（j-i-1），然后压入j。

代码如下：

Runtime: 8 ms, faster than 93.22% of C++ online submissions for Trapping Rain Water.
Memory Usage: 9.6 MB, less than 55.99% of C++ online submissions for Trapping Rain Water.

```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0, len = height.size();
        stack<int> S;
        int tmp;
        for(int i=0; i<len; i++){
            if(height[i]==0) continue;
            if(S.empty()){
                S.push(i);
                continue;
            }
            tmp = 0;
            while(true){
                if(S.empty()) {
                    S.push(i);
                    break;
                }
                if(height[S.top()]>height[i]){
                    res += (height[i]-tmp) * (i-S.top()-1);
                    S.push(i);
                    break;
                }
                res += (height[S.top()]-tmp) * (i-S.top()-1);
                tmp = height[S.top()];
                S.pop();
            }
        }
        return res;
    }
};
```

优化之后,速度没有提升，但是好看了一点：

Runtime: 8 ms, faster than 93.22% of C++ online submissions for Trapping Rain Water.
Memory Usage: 9.5 MB, less than 56.83% of C++ online submissions for Trapping Rain Water.

```C++
class Solution {
public:
    int trap(vector<int>& height) {
        int len = height.size();
        int tmp, res = 0;
        
        if(len<3) return res;
        
        stack<int> S;
        S.push(0);
        
        for(int i=1; i<len; i++){
            tmp = 0;
            while(!S.empty() && height[S.top()]<=height[i]){
                res += (height[S.top()]-tmp) * (i-S.top()-1);
                tmp = height[S.top()];
                S.pop();
            }
            if(!S.empty()) res += (height[i]-tmp) * (i-S.top()-1);
            S.push(i);
        }
        return res;
    }
};
```

BitBrave，2019-5-24。完全自己的思路，nice