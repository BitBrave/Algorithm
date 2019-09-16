# LeetCode(825. Friends Of Appropriate Ages)题解

Some people will make friend requests. The list of their ages is given and `ages[i]` is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

- `age[B] <= 0.5 * age[A] + 7`
- `age[B] > age[A]`
- `age[B] > 100 && age[A] < 100`

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

**Example 1:**

```
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
```

**Example 2:**

```
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```

**Example 3:**

```
Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
```

Notes:

- `1 <= ages.length <= 20000`.
- `1 <= ages[i] <= 120`.

## 解题思路

给出一个列表记录每个人的年龄，然后每个人会根据年龄条件进行朋友请求，求出有多少的朋友请求产生，记住朋友请求并不一定非得是双向的。

这个如果直接使用$O(n^2)$的暴力搜索会超时，因此可以考虑更聪明的办法，Count sort，以年龄为下标记录每个年龄的人各有多少，然后再依次选取两个年龄的人进行比较。

代码如下，时间复杂度$O(n)$，空间复杂度$O(n)$：

`Runtime: 32 ms, faster than 98.30% of C++ online submissions for Friends Of Appropriate Ages.`

`Memory Usage: 11.2 MB, less than 33.33% of C++ online submissions for Friends Of Appropriate Ages.`

```C++
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int len = ages.size(), res = 0;
        vector<int> A(121, 0);
        for(int a : ages) A[a]++;
        
        int i = 0, j = 0;
        for(i=0; i<121; i++){
            for(j=i/2+8; j<i; j++) res += A[j] * A[i];
            if(j == i) res += A[i] * (A[i] - 1);
        }
        return res;
    }
};
```

BitBrave, 2019-09-16

