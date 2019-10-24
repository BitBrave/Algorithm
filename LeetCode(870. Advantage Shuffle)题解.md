## LeetCode(870. Advantage Shuffle)题解

Given two arrays `A` and `B` of equal size, the *advantage of A with respect to B* is the number of indices `i` for which `A[i] > B[i]`.

Return **any** permutation of `A` that maximizes its advantage with respect to `B`.

**Example 1:**

```
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
```

**Example 2:**

```
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
```

**Note:**

1. `1 <= A.length = B.length <= 10000`
2. `0 <= A[i] <= 10^9`
3. `0 <= B[i] <= 10^9`

 ## 解题思路

给定两个等长的数组A和B，其中A的优势就是A中对应位置的元素大于B中对应位置的元素的数量。现在对A重排列，最大化A的优势。如果有多个答案，返回其中任意一个即可。

这个题直观上就可以使用Greedy做，我们对于B中的一个元素B[i]，如果A中有比它大的元素，那么我们只选择比它大的元素中最小的那个即可，这样可以最大限度地保留A能覆盖其它B中元素的可能性。

因此，算法如下，将A，B都升序排序。然后分别遍历AB中的元素，A中使用i，B中使用j。初始化i=0，j=0.

然后如下判断——

- i==len(A)，表明已经遍历完成了，直接结束算法。

- A[i]>B[j]，表示此时可以覆盖，直接i = i+1，j = j+1.
- A[i]<=B[j]，表示此时不能覆盖，就在不超过len(A)的情况下不断增加i，判断A[i]是否可以大于B[j]，如果到最后都不能大于，则表明A中剩下的数已经都不能大于B中任何数了，就直接结束算法。如果走到一个i的值，有A[i]大于B[j]，就直接使用这个与最开始的i进行交换即可。然后i = i+1，j = j+1.

代码如下，排序时间复杂度O(nlogn)，加上判断的时间O(n)，总的时间复杂度为O(nlogn)，但是因为最后返回的数组要按照B的顺序，因此要把A重新排位置，这就需要一开始记住B原数组的位置，因此需要使用一个数组记录，空间复杂度O(n)。

`Runtime: 156 ms, faster than 90.29% of C++ online submissions for Advantage Shuffle.`

`Memory Usage: 14.3 MB, less than 100.00% of C++ online submissions for Advantage Shuffle.`

```C++
vector<int> B_;
bool cmp(int a, int b){
    return B_[a] < B_[b];
}

class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        int len = A.size();
        int i, j, b = len - 1;
        
        vector<int> ret(len, -1), p(len, -1);
        B_ = B;
        for(i=0; i<len; i++) p[i] = i;
        sort(A.begin(), A.end());
        sort(p.begin(), p.end(), cmp);
        
        i = j = 0;
        while(i < len){
            while(i < len && A[i] <= B[p[j]]) ret[p[b--]] = A[i++];
            if(i < len) ret[p[j++]] = A[i++];
        }
        return ret;
    }
};
```

BitBrave,2019-10-24