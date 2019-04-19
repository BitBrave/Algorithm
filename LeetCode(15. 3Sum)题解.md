# LeetCode(15. 3Sum)题解

------

原文如下：

## 解题思路
题目要求从一个数组中找出不同的三个数的组合，使之和为0。是一个Medium的题目，当然可以使用一个三重循环，时间复杂度O(n3)，但是我们可以有一个更好的方式，时间复杂度O(n2)。

首先处理问题时，可以将数组初步处理一下，比如无序变为有序，再来看问题或许会好一点。这个题目我们可以将数组首先排序，然后再来看，当选定一个数时，再根据这个数来从这个有序数组中选另外的数。方法如下

具体步骤如下：

    1. 将数组nums升序排序，长度为len，并从左到右依次选定一个为位置i，初始化i=0；O(nlogn)
    2. 设置r = 0 - nums[i]，left = i + 1, right = nums[len  - 1]
    3. 计算nums[left] + nums[right] 是否等于r，如下处理：
        a 如果等于r，就将i，left，right三个位置的数记录下来，然后left++，right++；
        b 如果大于r，说明三个数的和大于0，此时需要降低，right--；
        c 如果小于r，说明三个数的和小于0，此时需要增大，left++；
        PS：移动的过程中，如果发现nums[left] = nums[left+1]之类的情况，表示这个数重复了，而我们之前已经比较过这个数了，所以此时可以直接跳过。
    4. i++，如果与前一个数一样，则continue
    5. 当i==len-2时，返回函数 O(n2)
    a trick: 当检测时，如果nums[left] + nums[left + 1] > r 或者 nums[right] + nums[right - 1] < r，就没比较测试后面的了，因为后面的肯定更加不可能满足条件了。直接i++

代码如下

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int len = nums.size();
        
        // sort O(nlogn)
        sort(nums.begin(), nums.end());
        
        int left = 0, right = 0, r = 0;
        for(int i = 0; i < len - 2; i++){
            left = i + 1;
            right = len - 1;
            r = 0 - nums[i];
            while(left < right){
                if(nums[left] + nums[left + 1] > r || nums[right] + nums[right - 1] < r) break;
                
                if(r > nums[left] + nums[right]) left++;
                else if(r < nums[left] + nums[right]) right--;
                else{
                    vector<int> a{nums[i], nums[left], nums[right]};
                    res.push_back(a);
                    left++;
                    right--;
                    while(left < right && nums[left] == nums[left-1]) left++;
                    while(right > left && nums[right] == nums[right+1]) right--;
                }
            }
            
            while(i + 1 < len - 2 && nums[i] == nums[i + 1]) i++; 
        }
        
        return res;
    }
};
```

BitBrave, 2-19-04-19. PS:(**LeetCode上你的stdout也算时间的，所以在提交的时候记得注释掉cout之类的print函数，否则本来accept的都会timelimit exceed的。**)
