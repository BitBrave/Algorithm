# LeetCode(215. Kth Largest Element in an Array)题解
------
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
Example 2:

    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

Note: 
    You may assume k is always valid, 1 ≤ k ≤ array's length.

## 解题思路
给出一个无序数组，找出其中第K大的数。

最简单的方式就是排序，然后直接返回第K大的数，时间复杂度是O(nlogn). 使用STL函数可以AC。

代码如下

```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size()-k];
    }
};
```

但是这样太简单了，肯定有更好的办法。一个就是DC。类似于快排。随便选一个数，比其大的数放在左边，比其小的数放在右边。如果左边的数有K-1个的话，就直接返回现在选中的数，如果左边的数大于K-1，就缩短数组，直接在左边数组中找。如果小于K-1个，就表示第K大的数在右边，就在右边数组内寻找第K-len(left)大的数。理想情况下的时间复杂度O(logn),最差是O(n2).但一般情况下，时间复杂度是O(logn)

PS: 需要注意有重复的数，因此在计算的时候需要记录相同的数。

代码如下：

Runtime: 88 ms, faster than 6.01% of C++ online submissions for Kth Largest Element in an Array.
Memory Usage: 12.4 MB, less than 5.08% of C++ online submissions for Kth Largest Element in an Array.

```c++
class Solution {
public:
    int findKthLargest_(vector<int>& nums, int sta, int end, int k){
        if(sta>end) return -1;
        int left = 0, right = 0, same_count = 1;
        int i, j;

        for(i = sta+1, j = end; i<j; ){
            if(nums[i]>nums[sta]){
                if(nums[j]<nums[sta]){
                    i++; j--;
                    left++; right++;
                }
                else if(nums[j]>nums[sta]){
                    i++;
                    left++;
                }
                else{
                    i++;
                    left++;
                    same_count++;
                }
            }
            else if(nums[i]<nums[sta]){
                if(nums[j]>nums[sta]){
                    swap(nums[i], nums[j]);
                    i++; j--;
                    left++; right++;
                }
                else if(nums[j]<nums[sta]){
                    j--;
                    right++;
                }
                else{
                    swap(nums[i], nums[j]);
                    i++; j--;
                    left++; right++;
                    same_count++;
                }
            }
            else if(nums[i]==nums[sta]){
                i++;
                left++;
            }
        }
        //cout<<left<<"+"<<right<<endl;
        if(i==j){
            if(nums[i]>nums[sta]){
                swap(nums[sta], nums[i]);
                left += 2;
            }
            else if(nums[i]<nums[sta]){
                swap(nums[sta], nums[i-1]);
                i--;
                left++; right++;
            }
            else{
                left += 2;
            }
        }
        else if(i>j){
            left++;
            swap(nums[sta], nums[i-1]);
            i--;
        };
        
        if(k<left-same_count){
            return findKthLargest_(nums, sta, sta+left-2, k);
        }
        else if(k>left-1){
            return findKthLargest_(nums, sta+left, end, k-left);
        }
        return nums[i];
    }   
    int findKthLargest(vector<int>& nums, int k) {
        int len = nums.size();
        
        return findKthLargest_(nums, 0, len-1, k-1);
    }
};
```

BitBrave, 2019-07-30