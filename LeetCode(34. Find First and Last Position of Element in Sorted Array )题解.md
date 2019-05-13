# LeetCode(34. Find First and Last Position of Element in Sorted Array
)题解
------
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

## 解题思路
Medium题，要求从一个升序的有序数组内找出某个给定数的起始位置。若没有对应的的数就返回两个-1即可。要求时间复杂度 O(log n).

可以使用2分查找，当中间数比目标值大，意味着所有的目标数不可能出现在右边半个数组内，直接在左边找。当中间数比目标值小，意味着所有的目标数不可能出现在左边的数组内，直接在右边找。当相等的时候，可以判断是不是目标数的一个边界值，如果是的话就直接记录，如果不是就分别在左边和右边找。

注意，这有一种情况，就是分别在左边和右边找的时候，各自又会产生左边界和又边界，最后的结果数组内会记录很多个值，如果数组内所有的数都是一样的，最后会记录下logn个数。但其实在大的数组内只需要最前面和最后面的。因此最后只需要取记录的最前面和最后面即可。

当然还有其它的优化方式，比如用一个label标记当前是否在两边数组内找，或者在记录的时候看看当前数组内是否已经有多个值了（我们只需要两个值）。

代码如下（未优化）：

Runtime: 8 ms, faster than 99.13% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 11.4 MB, less than 5.17% of C++ online submissions for Find First and Last Position of Element in Sorted Array.

```c++
class Solution {
public:
    void search(vector<int>& nums, int left, int right, int target, vector<int>& ret){

        if(left>right){
            ret.push_back(-1);
            return;
        }
        if(left==right){
            if(nums[left]==target) ret.push_back(left);
            else ret.push_back(-1);
            return;
        }

        int mid = (left+right)/2;
  
        if(nums[mid]>target) search(nums, left, mid-1, target, ret);
        else if(nums[mid]<target) search(nums, mid+1, right, target, ret);
        else{
            if(mid==0) ret.push_back(mid);
            else if(nums[mid-1]!=target) ret.push_back(mid);
            else search(nums, left, mid-1, target, ret);
            
            if(mid==nums.size()-1) ret.push_back(mid);
            else if(nums[mid+1]!=target) ret.push_back(mid);
            else search(nums, mid+1, right, target, ret);
        }
        
        return;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0) return vector<int>(2, -1);
        
        vector<int> ret, res;
        search(nums, 0, len-1, target, ret);
        if(ret.size()==1) ret.push_back(ret[0]);
        res.push_back(ret[0]);
        res.push_back(ret[ret.size()-1]);
        return res;
    }
};
```

代码如下（优化）：

Runtime: 8 ms, faster than 99.13% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 11 MB, less than 25.65% of C++ online submissions for Find First and Last Position of Element in Sorted Array.

```c++
class Solution {
public:
    void search(vector<int>& nums, int left, int right, int target, vector<int>& ret){

        if(left>right){
            if(ret.size()==0) ret.push_back(-1);
            return;
        }
        if(left==right){
            if(nums[left]==target) {
                if(ret.size()==0) ret.push_back(left);
                else{
                    if(ret[0]>left) ret[0] = left;
                    if(ret.size()==1) ret.push_back(right);
                    else if(ret[1]<right) ret[1] = right;
                    //cout<<"jiarule" << left<<endl;
                }
            }
            else if(ret.size()==0) ret.push_back(-1);
            return;
        }

        int mid = (left+right)/2;
  
        if(nums[mid]>target) search(nums, left, mid-1, target, ret);
        else if(nums[mid]<target) search(nums, mid+1, right, target, ret);
        else{
            if(mid==0){
                if(ret.size()==0) ret.push_back(mid);
                else ret[0] = mid;
            }
            else if(nums[mid-1]!=target) {
                if(ret.size()==0) ret.push_back(mid);
                else if(ret[0]>mid) ret[0] = mid;
                //cout<<"zuobian"<<mid<<endl;
            }
            else search(nums, left, mid-1, target, ret);
            
            if(mid==nums.size()-1){
                if(ret.size()==1) ret.push_back(mid);
                else ret[1] = mid;
            }
            else if(nums[mid+1]!=target){
                if(ret.size()==1) ret.push_back(mid);
                else if(ret[1]<mid) ret[1] = mid;
                //cout<<"youbian"<<mid<<endl;
            }
            else search(nums, mid+1, right, target, ret);
        }
        
        return;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0) return vector<int>(2, -1);
        
        vector<int> ret;
        search(nums, 0, len-1, target, ret);
        if(ret.size()==1) ret.push_back(ret[0]);
        
        return ret;
    }
};
```

BitBrave, 2019-05-13