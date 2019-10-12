# LeetCode(851. Loud and Rich)题解

In a group of N people (labelled `0, 1, 2, ..., N-1`), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `x`, simply "person `x`".

We'll say that `richer[i] = [x, y]` if person `x` definitely has more money than person `y`.  Note that `richer` may only be a subset of valid observations.

Also, we'll say `quiet[x] = q` if person x has quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the least quiet person (that is, the person `y` with the smallest value of `quiet[y]`), among all people who definitely have equal to or more money than person `x`.

 

**Example 1:**

```
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
```

**Note:**

1. `1 <= quiet.length = N <= 500`
2. `0 <= quiet[i] < N`, all `quiet[i]` are different.
3. `0 <= richer.length <= N * (N-1) / 2`
4. `0 <= richer[i][j] < N`
5. `richer[i][0] != richer[i][1]`
6. `richer[i]`'s are all different.
7. The observations in `richer` are all logically consistent.

## 解题思路

有一些人，在数组richer给定一些关系，richer[0]所代表的人比richer[1]所代表的人更加富有，而quiet则表示满足感，quiet[i]表示人i的满足感。现在要求，通过richer中给出的关系，找出对应的i人的比i富有或者和i一样富有的人中满足感最低的人j，填入answer中，返回答案数组。

这个题初读起来有点拗口，但是理顺题意之后还是比较简单的。可以直接使用DFS进行求解。利用richer建立一个有向图，其中如果a人比b人更富有，就从b到a连接一条边。使用Graph记录这样一个图关系。因为这个富有的关系是递进的，因此不可能会出现环的关系。

然后使用DFS，选定一个人开始在图里面搜寻，选定满足感最低的人，填入结果数组中，如果直接全部遍历的话，一个人的时间复杂度是理论上O(n2)，所有人的加起来就是O(n3)。

但这里有一个Trick，如果一个比我更富有的人的答案已经出来了，那么这条路的后续我走到这里其实已经不用再去看后面的了，直接和这个人比较即可，这样其实只需要整体只需要O(n2)的时间就可以得到结果。

具体代码如下，时间复杂度O(n2)，空间复杂度O(n2)。

`Runtime: 112 ms, faster than 53.02% of C++ online submissions for Loud and Rich.`

`Memory Usage: 29.6 MB, less than 100.00% of C++ online submissions for Loud and Rich.`

```C++
class Solution {
    vector<vector<bool>> G;
    vector<bool> visit;
    vector<int> res;
public:
    void DFS(int p, int len, vector<int>& quiet){
        if(visit[p] == true) return;
        
        for(int i=0; i<len; i++){
            if(G[p][i] == false) continue;
            DFS(i, len, quiet);
            if(quiet[res[i]] < quiet[res[p]]) res[p] = res[i];
        }
        visit[p] = true;
        return;
    }
    
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        int len = quiet.size();
        
        res = vector<int>(len, 0);
        G = vector<vector<bool>>(len, vector<bool>(len, false));
        
        visit = vector<bool>(len, false);
        
        for(int i=0; i<len; i++) res[i] = i;
        
        len = richer.size();
        for(int i=0; i<len; i++) G[richer[i][1]][richer[i][0]] = true;   
        
        // DFS
        len = quiet.size();
        for(int i=0; i<len; i++) DFS(i, len, quiet);   
        
        return res;
    }
};
```

BitBrave，2019-10-11