# LeetCode(75. Sort Colors)题解
------
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?

## 解题思路
Medium，将一个代表红（0）、白（1）、蓝（2）的三个数字组成的数组M进行排序，使得其按照012的顺序存放。

这个题说白了就是一个排序问题，可以使用最普通的各种排序算法，时间复杂度O（nlogn），稍微聪明一点的方式就是可以将所有的数遍历一遍，然后记录012的各自的个数。最后再按照个数给数组的每个地方赋值。

那怎么在常量空间消耗内只使用一次遍历就可以达到目的呢？

有一个办法，从左到右遍历数组，我们用两个数a，b记录0和1在当前已经遍历的数组（边遍历边排序）中的各自最后一个数的位置。初始化a=b=-1，表示还没开始。假设当前数组走到了i。

有以下三种情况

1 M[i] == 2，此时不用管，直接i++

2 M[i] == 1，此时查看b的值，
    
    如果b=-1，说明之前还没有遇到1，前面的数组中没有1，这时候查看a的值，
        如果a=-1，表示前面的数组也没有0，那就全是2了，将M[i]与M[0]交换，b=0然后i++
        如果a!=-1，表示前面已经有0了，交换M[i]和M[a+1]，然后b=a+1，i++
    如果b!=-1，说明之前已经有1了，那就好办，直接交换M[i]和M[b++]，然后i++；

3 M[i] == 0，此时查看a的值

    如果a=-1，说明之前还没有遇到0，前面的数组中没有0，这时候可以直接将M[i]与M[0]交换，设a=0，然后查看M[i]的值。
        如果M[i]=1，表示之前的数组中有1了，然后将M[i]与M[b+1]交换，b++，i++
        如果M[i]=2或0，表示前面没有1，直接i++
    如果a!=-1，说明之前已经有0了，那就好办，直接交换M[i]和M[++a]，然后查看M[i]的值
        如果M[i]=1，表示之前的数组中有1了，然后将M[i]与M[b+1]交换，b++，i++
        如果M[i]=2或0，表示前面没有1，直接i++

代码如下：

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sort Colors.
Memory Usage: 8.7 MB, less than 13.93% of C++ online submissions for Sort Colors.

```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int len = nums.size();
        int a = -1, b = -1;
        for(int i=0; i<len; i++){
            if(nums[i]==2) continue;
            if(nums[i]==1){
                b = b==-1 ? a : b;
                swap(nums[++b], nums[i]);
            }
            else{
                swap(nums[++a], nums[i]);
                if(nums[i]==1) swap(nums[++b], nums[i]);
            }
        }
        return;
    }
};
```

BitBrave, 2019-06-10