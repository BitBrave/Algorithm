# LeetCode(886. Possible Bipartition)题解

Given a set of `N` people (numbered `1, 2, ..., N`), we would like to split everyone into two groups of **any** size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people numbered `a` and `b` into the same group.

Return `true` if and only if it is possible to split everyone into two groups in this way.

**Example 1:**

```
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
```

**Example 2:**

```
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
```

**Example 3:**

```
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
```

 

**Note:**

1. `1 <= N <= 2000`
2. `0 <= dislikes.length <= 10000`
3. `1 <= dislikes[i][j] <= N`
4. `dislikes[i][0] < dislikes[i][1]`
5. There does not exist `i != j` for which `dislikes[i] == dislikes[j]`.

## 解题思路

给定一组N个人（编号为1，2，...，N），我们想将每个人分成两组，任何规模。每个人都可能不喜欢其他人，因此不应将他们归为一类。形式上，如果dislike[i] = [a，b]，则意味着不允许将编号为a和b的人员放在同一组中。当且仅当可以以这种方式将每个人分成两组时才返回True，否则返回False。

我们假设如果两个人之间相互不喜欢，那么就在这两个人之间连一条线，最终会形成多个图组成的多个图集合。而如果图出现奇数点的环路，则表示不能满足题目要求，因为无法将其分成两个集合，使得连线的两个点在不在同一个组合里。

代码如下，使用一个矩阵记录点之间的相连情况，同时在遍历过程中记录已经找到的点。因此总的时间复杂度为O(n)，空间复杂度O(n2)。

`Runtime: 472 ms, faster than 5.04% of C++ online submissions for Possible Bipartition.`

`Memory Usage: 59.1 MB, less than 28.57% of C++ online submissions for Possible Bipartition.`

```C++
class Solution {
    vector<vector<bool>> G;
    vector<bool> visit;
    vector<int> len;
public:
    bool DFS(int p, int N, int last_p, int num){
        if(visit[p]) return (num-len[p]) & 1;
    
        visit[p] = true;
        for(int i=0; i<N; i++){
            if(G[p][i] == false || i == last_p) continue;
            len[i] = len[p] + 1;
            if(DFS(i, N, p, num + 1)) return true;
        }
        return false;
    }
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        G = vector<vector<bool>>(N, vector<bool>(N, false));
        visit = vector<bool>(N, false);
        len = vector<int>(N, 0);
        len[0] = 0;
        for(vector<int> d : dislikes){
            G[d[0]-1][d[1]-1] = G[d[1]-1][d[0]-1] = true;
        }
        for(int i=0; i<N; i++){
            if(visit[i]) continue;
            if(DFS(i, N, -1, 0)) return false;
        }
        return true;
    }
};
```

BitBrave，2019-10-23