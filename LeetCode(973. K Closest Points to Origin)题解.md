# LeetCode(973. K Closest Points to Origin)题解

We have a list of `points` on the plane.  Find the `K` closest points to the origin `(0, 0)`.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

**Example 1:**

```
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
```

**Note:**

1. `1 <= K <= points.length <= 10000`
2. `-10000 < points[i][0] < 10000`
3. `-10000 < points[i][1] < 10000`

## 解题思路

给一系列点，求出其里原点最近的K个点。（距离为欧几里得距离）

这个最简单的方式就是将所有点按照欧几里得距离进行排序，然后选取前K个即可。

这样时间复杂度为O(NlogN)，空间复杂度O(1)，代码如下。

`Runtime: 852 ms, faster than 6.33% of C++ online submissions for K Closest Points to Origin.`

`Memory Usage: 189.1 MB, less than 10.94% of C++ online submissions for K Closest Points to Origin.`

```c++
bool cmp(vector<int> a, vector<int> b){
    return a[0]*a[0]+a[1]*a[1] < b[0]*b[0]+b[1]*b[1];
}
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        sort(points.begin(), points.end(), cmp);
        return vector<vector<int>>(points.begin(), points.begin()+K);
    }
};
```

但是这样明显不是最优的，因为其实只需要前K个，而我们将所有的元素都进行了排序。因此我们可以使用Heap的方式，维护一个最大堆，然后遍历每一个坐标，在堆内元素少于K的时候，直接将点入堆，如果达到了K就判断坐标和堆顶元素的距离大小，如果小于堆顶元素就入堆，然后pop出最大堆，否则就放弃这个坐标。最后堆内的K个元素就是题目的解。

代码如下，时间复杂度O(NlogK)，空间复杂度O(K)。

`Runtime: 496 ms, faster than 12.29% of C++ online submissions for K Closest Points to Origin.`

`Memory Usage: 103.5 MB, less than 14.06% of C++ online submissions for K Closest Points to Origin.`

```c++

bool cmp(vector<int> a, vector<int> b){
    return a[0]*a[0]+a[1]*a[1] < b[0]*b[0]+b[1]*b[1];
}
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<vector<int>> ret({points[0]});
        make_heap(ret.begin(), ret.end(), cmp);
        int k = 1, len = points.size();
        for(int i=1; i<len; i++){
            if(k == K and cmp(ret[0], points[i])) continue;
            ret.push_back(points[i]);
            k++;
            push_heap(ret.begin(), ret.end(), cmp);
            if(k > K){
                //cout<<"dayul"<<ret[0][1]<<endl;
                pop_heap(ret.begin(), ret.end(), cmp);
                ret.pop_back();
                k--;
            }
        }
        return ret;
    }
};
```



BitBrave，2019-11-26