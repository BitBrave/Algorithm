# LeetCode(11. Container With Most Water)题解

------

原文如下：

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and n is at least 2.

![The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

## 题目分析：

题目是LeetCode内一个Medium难度的题目，并不难。要求从给定的条件中找出最大容量的容器组成。如果抽离出现实，就是要求给定一个数组A = [a1, a2, ..., an]，寻找一个M = max abs(i-j)* min(ai, aj) (i,j = 1,2, ..., n)。

## 思路一O(n2)：

题目并未给定时间复杂度的要求，一个最简单的思路就是遍历，比较任意两个数之间的大小，时间复杂度O(n2)。代码如下：

```c++
class Solution {

public:
    int maxArea(vector<int>& height) {
        int M = 0, len = height.size();
        for(int i=0; i< len; i++){
            for(int j = i; j<len; j++){
                M = M>(j-i)*min(height[i], height[j])? M:(j-i)*min(height[i], height[j]);
            };
        };
        return M;
    }
};
```

## 思路二O(nlogn)：

一个可以提速的办法是，基于这样的一个事实：ai与aj(i<\j)组成的值为abs(i-j)*min(ai,aj)，而在i与j之中的任何低于min(ai,aj)的ak肯定不会在是整个数组中作为最大容量时的选择，因为假如最大的容量组成为M = abs(p-k)*min(ak, ap)，基于i<\k<\j, ak<=min(ai, aj)那么有如下几种情况。

    p<i<j: M <= abs(p-j)*min(aj, ap)。
    i<j<p: M <= abs(p-i)*min(ai, ap)。
    i<=p<=j: M <= min(abs(i-p)*min(ai, ap), abs(p-j)*min(aj, ap))。
    
因此，我们可以记录数组内元素和初始位置的关系，然后将数组降序排序，得到新的数组B = \[b1, b2, ..., bn]，依次遍历。
    初始化left=min(b1的初始位置p1, b2的初始位置p2)，right= max(b1的初始位置p1, b2的初始位置p2)，M = abs(p1-p2)*b2。
    依次向下遍历，在位置pi。
    如果left<pi<right: M = M，跳过。
    如果pi<left<right: M = max(M, (right-pi)*B[i])，更新 left = pi
    如果left<right<pi: M = max(M, (pi-left)*B[i])，更新 right = pi
    

这里要注意，只要pi在当前\[left, right]区间之外，都要进行更新（important），不管M是否需要更新，因为B降序排序，A\[pi]总是剩下的最大的，因此其间的都应该不考虑。

注意B\[i] = A\[pi], 所以C++代码实现时，可以利用数组B只存储位置，按照A内的元素大小排序位置。不过我这里是使用Vector建立了一个二维数组，大小A.size()*2，内部存储位置与元素值。自定义比较函数。代码如下：

```c++
class Solution {

public:
    static bool cmp(const vector<int> &a, const vector<int> &b){
        return a[1] > b[1];
    };
    
    int maxArea(vector<int>& height) {
        if(height.size() <= 1) return 0;
        
        vector<vector<int>> B(height.size(), vector<int>(2,0));
        // O(n)
        for(int i = 0; i < height.size(); i++) {
            B[i][0] = i;
            B[i][1] = height[i];
        };
        // O(nlogn)
        sort(B.begin(), B.end(), cmp);
        // O(n)
        int left = min(B[0][0], B[1][0]), right = max(B[0][0], B[1][0]), M;
        M = (right - left) * min(B[0][1], B[1][1]);
        for(int i = 2; i<B.size(); i++){
            int pi = B[i][0];
            if(left < pi && pi < right) continue;
            else if (pi < left){
                M = max(M, (right - pi) * B[i][1]);
                left = pi;
            }
            else {
                M = max(M, (pi - left) * B[i][1]);
                right = pi;
            };
        };
        return M;
    };
};
```

当然，代码美观一点的话，也可以这样写。

```c++
class Solution {
    
public:
    static bool cmp(const vector<int> &a, const vector<int> &b){
        return a[1] > b[1];
    };
    
    int maxArea(vector<int>& height) {
        if(height.size() <= 1) return 0;
        
        vector<vector<int>> B(height.size(), vector<int>(2,0));
        // O(n)
        for(int i = 0; i < height.size(); i++) {
            B[i][0] = i;
            B[i][1] = height[i];
        };
        // O(nlogn)
        sort(B.begin(), B.end(), cmp);
        // O(n)
        int left = min(B[0][0], B[1][0]), right = max(B[0][0], B[1][0]), M;
        M = (right - left) * min(B[0][1], B[1][1]);
        for(int i = 2; i<B.size(); i++){
            int pi = B[i][0];
            if(left < pi && pi < right) continue;
            
            M = (pi < left)? max(M, (right - pi) * B[i][1]) : max(M, (pi - left) * B[i][1]);
            left = min(left, pi);
            right = max(right, pi);
        };
        return M;
    };
};
```

**PS: 版权所有，翻版必究（所有的解法完全都是自己想出来的，很开心）。**
BitBrave, 2019-04-16