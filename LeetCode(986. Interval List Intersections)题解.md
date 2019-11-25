# LeetCode(986. Interval List Intersections)题解

Given two lists of **closed** intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

*(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)*

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)**

```
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
```

 

**Note:**

1. `0 <= A.length < 1000`
2. `0 <= B.length < 1000`
3. `0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9`

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

## 解题思路

给出两个区间数组，每个数组内按照坐标轴顺序给出了一些不相合的区间。现在求这两个数组的区间的子集，即重合的区间。

这个题很简单，可以直接使用双指针法，从两个数组的开头分别分配一个指针，然后逐步向右，每一步都进行两个区间的比较，如果有交集就记录下来，没有就算了。然后将区间中右边界更靠坐的区间放弃，选择对应数组内的下一个即可。

代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 52 ms, faster than 77.47% of C++ online submissions for Interval List Intersections.`

`Memory Usage: 15.8 MB, less than 80.00% of C++ online submissions for Interval List Intersections.`

```c++
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> ret;
        int lenA = A.size(), lenB = B.size();
        int i = 0, j = 0;
        while(i < lenA and j < lenB){
            if(A[i][0] > B[j][1]) j++;
            else if(A[i][1] < B[j][0]) i++;
            else{
                ret.push_back(vector<int>({max(A[i][0], B[j][0]), min(A[i][1], B[j][1])}));
                if(A[i][1] < B[j][1]) i++;
                else j++;
            } 
        }
        return ret;
    }
};
```



BitBrave，2019-11-25