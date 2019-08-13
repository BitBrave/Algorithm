# LeetCode(135. Candy)题解
------
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

Example 1:

    Input: [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

    Input: [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
                The third child gets 1 candy because it satisfies the above two conditions.
            
## 解题思路
一些孩子排成队列，每个孩子有一个值。现在要给每个孩子一些糖果，每个孩子至少有一个，值更高的孩子得到的糖果要比旁边的孩子多。问最少可以给几颗糖果。

这是一个典型的Greedy题目。可以首先遍历数组，通过波谷设为1然后向两边涨就可以了，遍历各种情况，一个一个判断就可以了。

但是要注意只要有波峰才必须要比自己小的节点大，如果是一样的话，可以都最小，或者不一样，注意辨别。

这个时间复杂度O(n)，因为每个值只遍历了两遍。

代码如下：

Runtime: 20 ms, faster than 97.93% of C++ online submissions for Candy.
Memory Usage: 10.8 MB, less than 15.38% of C++ online submissions for Candy.

```c++
class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size(), res = 0;
        if(len <= 1) return len;
        vector<int> Res(len, 0);
        int i=0, j = 0, lasti = -1;
        while(i<len){
            if(i==0 && i+1<len){
                if(ratings[i]<=ratings[i+1]){
                    Res[i] = 1;
                    for(j=i+1; j<len; j++){
                        if(ratings[j]>ratings[j-1]){
                            Res[j] = Res[j-1] + 1;
                        }
                        else if(ratings[j] == ratings[j-1]){
                            Res[j] =  1;
                        }
                        else break;
                    }
                    i = j;
                }
                else i++;
            }
            if(i==len-1 && i>0){
                if(ratings[i-1]>=ratings[i]){
                    Res[i] = 1;
                    for(j=i-1; j>=0; j--){
                        if(ratings[j]>ratings[j+1]){
                            Res[j] = max(Res[j], Res[j+1] + 1);
                        }
                        else if(ratings[j] == ratings[j+1]){
                            Res[j] = max(Res[j], 1);
                        }
                        else break;
                    }
                    break;
                }
            }
            if(i>0 && i+1<len){
                if(ratings[i]<=ratings[i+1]){
                    Res[i] = 1;
                    for(j=i-1; j>=0; j--){ // left
                        if(ratings[j]<ratings[j+1]) break;
                        Res[j] = (ratings[j+1] == ratings[j]) ? max(1, Res[j]) : max(Res[j+1] + 1, Res[j]);
                    }
                    for(j=i+1; j<len; j++){ // right
                        if(ratings[j]<ratings[j-1]) break;
                        Res[j] = ratings[j-1] == ratings[j] ? 1 : Res[j-1] + 1;
                    }
                    i = j;
                }
                else i++;
            }
        }
        for(i=0; i<len; i++) res += Res[i];
        return res;
    }
};
```

PS： this problem waste me much time, but it proves that I can do it!

BitBrave, 2019-08-12