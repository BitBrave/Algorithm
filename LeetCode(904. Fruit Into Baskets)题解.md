# LeetCode(904. Fruit Into Baskets)题解

In a row of trees, the `i`-th tree produces fruit with type `tree[i]`.

You **start at any tree of your choice**, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

**Example 1:**

```
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
```

**Example 2:**

```
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
```

**Example 3:**

```
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
```

**Example 4:**

```
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
```

 

**Note:**

1. `1 <= tree.length <= 40000`
2. `0 <= tree[i] < tree.length`

## 解题思路

给出一个数组，每个元素代表一棵树，树上结的果子的类型就是元素值。现在有两个无限大的篮子。现在随便选一个位置，然后依次向右走边，不能跳过，将采集到的果子装入篮子。但是每个篮子只能装一种果子。现在问，这样能得到最多多少棵树的果子。

这个题仔细思考一下，抽象一下，就是给定一个数组，要求找出由最多两个元素组成的最长的子数组的长度。

因此，可以使用双指针法维持两个指针sta和end，sta记录已经遍历的数组中end位置的元素的前面的边界，end表示当前遍历到的位置。type记录当前遍历数组的最近的符合条件的子数组元素类型数目，val记录当前合法子数组中处理end所指元素中另一个元素（如果有的话），num记录当前遍历数组的最近的符合条件的子数组元素长度，ret则记录最终答案。

- 如果数组长度为1，那么算法就结束了，直接返回1即可。否则从左到右从头遍历数组。
- 初始化sta指向第一个，end都指向第二个，type=1，ret=1，num=1, val = -1。
- 将end与前一个元素比较，如果相同表示这个元素是和之前一样类型，直接end++，num++。
- 若end与前一个不相等，这时候查看type，
- 如果为1，就表示当前合法数组内只有一种类型的值，可以继续加，因此end++，num++，但是元素类型多了一个，所以type++。此时，需要记录end的元素与其它元素的交界，方便后续操作，记录sta=end（注意是end未++的赋值），val=end前一个元素值（即数组的另一个元素）。
- 如果type为2，判断当前值是否是val，如果是就end++，num++，sta=end（注意是end未++的赋值），val=end前一个元素值（即数组的另一个元素）。
- 如果type为2，并且end的元素和val也不一样，那表示当前子数组内元素类型已经有两种了，就不能再加第三种了，因此需要更新信息。ret=max(ret, num)将上一个子数组的长度更新到ret内。新的子数组表示如下：num = end-sta+1，type=2。然后end++。方便后续操作，记录sta=end（注意是end未++的赋值）。然后重复上述第一步执行。



代码如下，时间复杂度O(N)，空间复杂度O(1)。

`Runtime: 124 ms, faster than 93.08% of C++ online submissions for Fruit Into Baskets.`

`Memory Usage: 14.9 MB, less than 93.55% of C++ online submissions for Fruit Into Baskets.`

```c++
class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int ret = 1, num = 1, type = 1, val = -1, len = tree.size();
        int sta = 0, end = 1;
        for(; end<len; end++){
            //cout<<"zoudao"<<tree[end]<<" sta "<<tree[sta]<<" val "<<val<<" dangqian "<< num<<endl;
            if(tree[end] == tree[end-1]) num++;
            else if(type == 1){
                num++;
                type++;
                sta = end;
                val = tree[end-1];
            }
            else if(val == tree[end]){
                num++;
                sta = end;
                val = tree[end-1];
            }
            else{
                ret = max(ret, num);
                num = end - sta + 1;
                sta = end;
                val = tree[end-1];
            }
        }
        return max(ret, num);
    }
};
```



BitBrave，2019-11-15