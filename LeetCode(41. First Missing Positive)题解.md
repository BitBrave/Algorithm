# LeetCode(41. First Missing Positive)题解
------
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

    Input: [1,2,0]
    Output: 3
Example 2:

    Input: [3,4,-1,1]
    Output: 2
Example 3:

    Input: [7,8,9,11,12]
    Output: 1
Note:

    Your algorithm should run in O(n) time and uses constant extra space.

## 解题思路
Hard，主要是题意有点难以理解。这题要求的是从一个未排序的数组中找第一个丢失掉的连续正数（从1开始找），比如[3,4,-1,1]丢失的是2，[7,8,9,11,12]丢失的是1。但是要求是时间复杂度o(n)。并且使用常量空间，就是不能额外开辟相同大小的内存。

其实很简单，可以想象，连续的正数这是一个可以利用的点的，下标也是连续的，想办法把这两个联系在一起。可以如下：

从头到尾遍历数组，遇到一个正数k将其放入下标为k-1的位置。但会遇到，如果k太大或者负数就将其放入最后一个位置，然后将数组要遍历的长度减1，因为这些数都是干扰的没用的但是要占位置，我们就尽量放在最后一个。还有要是数组中有重复的话，我们可以在交换的时候检查，是否k-1位置上已经有k了，如果有的话就将其放在最后一个位置，因为表示这个数多余了，数组长度-1.

要注意，换置的操作方式就是将当前位置的数与k-1的数进行交换，然后将当前位置的数继续换，直到当前位置的数就该在当前位置，才走下一步。

这样换完之后，从左到右，第一个k-1位置上如果不是k，就返回k即可，表示缺少k。其实按照上述的操作，返回当时记录的数组长度+1就可以了，因为遍历到最后一个循环才会退出，而已经遍历过的表明前面的数都肯定变成合法的了。

代码如下：

```c++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int len = nums.size();
        int i = 0;
        while(i<len){
            if(nums[i] == i+1){
                i++;
                continue;
            } 
            
            if(nums[i]<=0 || nums[i]>len || nums[nums[i]-1] == nums[i]){
                swap(nums[len-1], nums[i]);
                len--;
                continue;
            }
            swap(nums[i], nums[nums[i]-1]);
        }
        return len+1;
    }
};
```

BitBrave, 2019-05-24.