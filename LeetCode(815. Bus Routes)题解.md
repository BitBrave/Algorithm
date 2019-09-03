# LeetCode(815. Bus Routes)题解
------
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

    Example:
    Input: 
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    Output: 2
    Explanation: 
    The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

    1 <= routes.length <= 500.
    1 <= routes[i].length <= 500.
    0 <= routes[i][j] < 10 ^ 6.

## 解题思路
有一些公交，每个公交有固定的循环线路，现在给出一个起点站台和结束站台，求出最少的换乘公交数。

这个题可以使用DFS，首先建立一个graph，节点代表一个公交，两个节点间有边表示这两个公交的线路有交叉的地方即意味着可以换乘。建立结束之后可以建立一个源点，从起点站台，所有经过这个站台的公交都与之加上一条边。然后建立一个汇点，所有经过这个站台的公交节点也与之相连。那么这个题就变成了求源点到汇点的最短路径，可使用DFS求得。

如何构建graph呢，可是用一个Map，以站台为key，一个list记录经过这个站台的公交，Map构建完毕之后，每个元素内的value内的公交，两两之间即可换乘。

代码如下，时间复杂度O(n2), 空间复杂度O(n2):

Runtime: 344 ms, faster than 25.12% of C++ online submissions for Bus Routes.
Memory Usage: 35.9 MB, less than 100.00% of C++ online submissions for Bus Routes.

```C++
class Solution {
    map<int, vector<int>> M;
    vector<vector<int>> G;
public:
    void fillMap(vector<vector<int>>& routes, int len){
        for(int i=0; i<len; i++){
            int rlen = routes[i].size();
            for(int j=0; j<rlen; j++){
                if(M.find(routes[i][j]) == M.end()) M[routes[i][j]] = vector<int>(1, i+1);
                else M[routes[i][j]].push_back(i+1);
            }
        }
        return;
    }
    void createGraph(int len, int S, int T){
        map<int, vector<int>>::iterator iter;
        iter = M.begin();
        for(iter = M.begin(); iter != M.end(); iter++) {
            int rlen = iter->second.size();
            if(iter->first == S){
                for(int i=0; i<rlen; i++) G[0][iter->second[i]] = G[iter->second[i]][0] = 1;
            }
            else if(iter->first == T){
                for(int i=0; i<rlen; i++) G[len+1][iter->second[i]] = G[iter->second[i]][len+1] = 1;
            }
            for(int i=0; i<rlen; i++){
                for(int j=0; j<i; j++) G[iter->second[i]][iter->second[j]] = G[iter->second[j]][iter->second[i]] = 1;
            }
        }
        return;
    }
    void print(vector<vector<int>> G, int len){
        for(int i=0; i<len; i++){
            for(int j=0; j<len; j++){
                cout<<G[i][j]<<" ";
            }
            cout<<endl;
        }
        return;
    }
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        if(S == T) return 0;
        int res = -1, len = routes.size();
        G = vector<vector<int>>(len+2, vector<int>(len+2, 0));
        fillMap(routes, len);
        createGraph(len, S, T);
        //print(G, len+2);
        /************************/
        queue<int> Q;
        vector<bool> V(len+2, false);
        Q.push(0);
        V[0] = true;
        while(!Q.empty()){
            int qlen = Q.size();
            while(qlen-- > 0){
                int bus = Q.front(); Q.pop();
                //cout<<"check "<<bus<<endl;
                if(bus == len+1) return res;
                for(int i=0; i<len+2; i++){
                    if(V[i] || G[bus][i] == 0) continue;
                    V[i] = true;
                    Q.push(i);
                    //cout<<"push "<<i<<endl;
                }
            }
            res += 1;
        }
        return -1;
    }
};
```

BitBrave, 2019-09-03