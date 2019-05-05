# LeetCode(31. Next Permutation)题解
------
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

## 解题思路

题目是Medium难度。将vector存的数组合而成变为一个新的更大的数，并且是可以组合最大的数内的最小的。比如123只能变成132。

思路就是，从后往前走，遇到一个比已遍历数中最大的数要小的数（直接看从后往前走是不是升序，遇到第一个不符合情况的即可），就将这个数与已遍历数中比其大的中最小的进行交换，然后将已遍历数进行升序排序即可。如果直到走到头都没有，则这个vector是降序排列的，那么只要将其倒序即可。

代码如下：

```c++
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if(len<=1) return;
        int m;
        for(int i=len-1; i>0; i--){
            if(nums[i]<=nums[i-1]) continue;
            for(int j=len-1; j>i-1; j--){
                if(nums[j]<=nums[i-1]) continue;
                swap(nums[j], nums[i-1]);
                sort(nums.begin()+i, nums.end());
                return;
            }
        }
        for(int left=0, right=len-1; left<right; left++, right--){
            swap(nums[left], nums[right]);
        }
        return;
    }
};
```