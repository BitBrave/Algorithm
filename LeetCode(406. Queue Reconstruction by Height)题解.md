# LeetCode(406. Queue Reconstruction by Height)题解
------
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

    Note:
    The number of people is less than 1,100.

 
Example

    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

## 解题思路
给出一个队列数组，每个元素包括两个。前一个是身高，后面是队列中前面比他高或者相等的人数目。

这有一个解题思路<https://leetcode.com/problems/queue-reconstruction-by-height/>

代码如下

Runtime: 136 ms, faster than 13.53% of C++ online submissions for Queue Reconstruction by Height.
Memory Usage: 25.1 MB, less than 9.52% of C++ online submissions for Queue Reconstruction by Height.

```c++
class Solution {
public:
    static bool cmp(vector<int> a, vector<int> b){
        if(a[0] > b[0]) return true;
        if(a[0]==b[0]) return a[1]<b[1];
        return false;
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> res;
        int len = people.size();
        sort(people.begin(), people.end(), cmp);
        
        for(int i=0; i<len; i++){
            if(people[i][1]>=i) res.push_back(people[i]);
            else res.insert(res.begin()+people[i][1], people[i]);
        }
        return res;
    }
};
```

BitBrave, 2019-08-10