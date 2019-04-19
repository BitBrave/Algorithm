# LeetCode(16. 3Sum Closest)题解

------

## 题意理解
从一个数组内找出三个数，其和与target的差值最小，假定这个和的值是唯一的，比如找离1最近的数，如果最小的距离是1，那么0和2都满足条件，但是在数组内只会出现一种情况。

## 解决思路
与15题一样，首先将数据变为有序，比如升序排序，时间复杂度O(nlogn)，然后再从头到尾指定一个位置i，再找两个指针从有序数组的left和right一起比较。时间复杂度O(n2)。总的时间复杂度O(n2)。

步骤如下：
    1. 将数组nums升序排序，长度为len，并从左到右依次选定一个为位置i，初始化i=0；O(nlogn)
    2. 设置r = target - nums[i]，left = i + 1, right = nums[len  - 1]
    3. 使用res来记录到目前为止与target最近的距离是多少，使用rec记录对应三个数的和
    4. 计算nums[left] + nums[right] 是否等于r，如下处理：
        a 如果等于r，表示可以完全匹配，此时直接返回target即可。；
        b 如果大于r，说明三个数的和大于target，此时为了更接近target需要降低，right--；
        c 如果小于r，说明三个数的和小于target，此时为了更接近target需要增大，left++；
        PS：移动的过程中，如果发现nums[left] = nums[left+1]之类的情况，表示这个数重复了，而我们之前已经比较过这个数了，所以此时可以直接跳过。
    5. i++，如果与前一个数一样，则continue
    6. 当i==len-2时，返回函数 O(n2)
    
代码如下：

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int res = INT_MAX, rec = 0, len = nums.size();
        
        // sort O(nlogn)
        sort(nums.begin(), nums.end());
        
        int left = 0, right = 0, r = 0;
        for(int i = 0; i < len - 2; i++){
            left = i + 1;
            right = len - 1;
            r = target - nums[i];

            while(left < right){
                rec = res < abs(r - nums[left] - nums[right])? rec: nums[left] + nums[right] + nums[i];
                res = min(res, abs(r - nums[left] - nums[right]));
                
                if(r > nums[left] + nums[right]){
                    left++;
                    while(left < right && nums[left] == nums[left-1]) left++;
                }
                else if(r < nums[left] + nums[right]) {
                    right--;
                    while(right > left && nums[right] == nums[right+1]) right--;
                }
                else return target;
            }
            
            while(i + 1 < len - 2 && nums[i] == nums[i + 1]) i++; 
        }
        
        return rec;
    }
};
```

有一个提速的，比如已经有nums[left] + nums[left + 1] > r或者nums[right] + nums[right - 1] < r，那么后续left再++或right--肯定不会获得更短的距离，所以可以直接返回。但是在LeetCode内好像没什么作用。
```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int res = INT_MAX, rec = 0, len = nums.size();
        
        // sort O(nlogn)
        sort(nums.begin(), nums.end());
        
        int left = 0, right = 0, r = 0;
        for(int i = 0; i < len - 2; i++){
            left = i + 1;
            right = len - 1;
            r = target - nums[i];

            while(left < right){
                //////// you can add it to speed-up
                **if(nums[left] + nums[left + 1] > r) {
                    rec = res < abs(r - nums[left] - nums[left + 1])? rec: nums[left] + nums[left + 1] + nums[i];
                    res = min(res, abs(r - nums[left] - nums[left + 1]));
                    break;
                }
                if(nums[right] + nums[right - 1] < r) {
                    rec = res < abs(r - nums[right - 1] - nums[right])? rec: nums[right - 1] + nums[right] + nums[i];
                res = min(res, abs(r - nums[right - 1] - nums[right]));
                    break;
                }**
                /////////
                rec = res < abs(r - nums[left] - nums[right])? rec: nums[left] + nums[right] + nums[i];
                res = min(res, abs(r - nums[left] - nums[right]));
                
                
                if(r > nums[left] + nums[right]){
                    left++;
                    while(left < right && nums[left] == nums[left-1]) left++;
                }
                else if(r < nums[left] + nums[right]) {
                    right--;
                    while(right > left && nums[right] == nums[right+1]) right--;
                }
                else return target;
            }
            
            while(i + 1 < len - 2 && nums[i] == nums[i + 1]) i++; 
        }
        
        return rec;
    }
};
```