# LeetCode(841. Keys and Rooms)题解
------
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.
Note:

    1 <= rooms.length <= 1000
    0 <= rooms[i].length <= 1000
    The number of keys in all rooms combined is at most 3000.


## 解题思路
有一些房间，每个房间有一些可以打开其他房间的钥匙。从0号房间进入，判断能不能通过钥匙进入所有的房间。

这是个很简单的BFS或者DFS题目。房间之间可以通过是否一个有另一个的钥匙而建一个单向边，最后使用便利搜索判断即可，如果能遍历整个图就返回true，否则返回false。

这里我使用了DFS，使用队列记录找到的钥匙，并且建立一个等大的数组，防止将重复的钥匙放入队列。

### 时间复杂度O(n), 空间复杂度O(n).

代码如下

Runtime: 12 ms, faster than 67.50% of C++ online submissions for Keys and Rooms.
Memory Usage: 10.6 MB, less than 100.00% of C++ online submissions for Keys and Rooms.

```c++
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int len = rooms.size(), res = 0;
        vector<bool> V(len, false);
        queue<int> Q;
        
        Q.push(0);
        V[0] = true;
        while(!Q.empty()){
            int nr = Q.front(); Q.pop();
            res += 1;
            //if(res == len) return true;
            for(int i=0; i<rooms[nr].size(); i++){
                if(V[rooms[nr][i]]) continue;
                Q.push(rooms[nr][i]);
                V[rooms[nr][i]] = true;
            }
        }
        return len == res;
    }
};
```

BitBrave, 2019-08-24