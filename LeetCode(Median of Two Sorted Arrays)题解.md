# LeetCode(4. Median of Two Sorted Arrays)题解
原文：
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

	Example 1:
		nums1 = [1, 3]
		nums2 = [2]
	The median is 2.0
	
	Example 2:
		nums1 = [1, 2]
		nums2 = [3, 4]
	The median is (2 + 3)/2 = 2.5

这道题让我们求两个有序数组的中位数，而且限制了时间复杂度为O(log (m+n))，看到这个时间复杂度，自然而然的想到了应该使用二分查找法来求解。但是这道题被定义为Hard也是有其原因的，难就难在要在两个未合并的有序数组之间使用二分法。

很多时候，我们不能只着眼于解决当前问题，不妨将问题**放大**一下，往往会看起来更容易解决一下，这在动态规划里也常常使用。比如这道题，我们不要只看求中位数。可以假设有一个函数findKth，通过输入参数K可以计算两个有序数组中的第K大的元素。那么只需要**执行两次findKth函数，分别另K等于(m+n+1) / 2 和 (m+n+2) / 2 ，然后求其平均值。**回顾一下中位数的定义，如果某个有序数组长度是奇数，那么其中位数就是最中间那个，如果是偶数，那么就是最中间两个数字的平均值。这里对于两个有序数组也是一样的，假设两个有序数组的长度分别为m和n，由于两个数组长度之和 m+n 的奇偶不确定，因此需要分情况来讨论，对于奇数的情况，直接找到最中间的数即可，偶数的话需要求最中间两个数的平均值。第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，对奇偶数均适用。加入 m+n 为奇数的话，那么其实 (m+n+1) / 2 和 (m+n+2) / 2 的值相等，相当于两个相同的数字相加再除以2，还是其本身。

那么findKth如何在两个有序数组中找到第K个元素？首先，为了避免产生新的数组从而增加时间复杂度，我们使用两个变量i和j分别来标记数组nums1和nums2的起始位置。然后来处理一些边缘情况，比如当某一个数组的起始位置大于等于其数组长度时，说明其所有数字均已经被淘汰了，相当于一个空数组了，那么实际上就变成了在另一个数组中找数字，直接就可以找出来了；如果K=1的话，那么我们只要比较nums1和nums2的起始位置i和j上的数字就可以了。

但是，对于一般的情况怎么处理？因为我们需要在两个有序数组中找到第K个元素，为了加快搜索的速度，我们要使用二分法，那么对谁二分呢，数组么？其实要对K二分，意思是我们需要分别在nums1和nums2中查找第K/2个元素，注意这里由于两个数组的长度不定，所以有可能某个数组没有第K/2个数字，所以我们需要先检查一下，数组中到底存不存在第K/2个数字，如果存在就取出来，否则就赋值上一个整型最大值，表示暂时不处理这个数组。如果某个数组没有第K/2个数字，那么我们就淘汰另一个数组的前K/2个数字即可，因为这时候第K个数肯定不会出现在另一个数组的前K/2中。

那有没有可能两个数组都不存在第K/2个数字呢，这道题里是不可能的，因为我们的K不是任意给的，而是给的m+n的中间值，所以必定至少会有一个数组是存在第K/2个数字的。最后就是二分法的核心：**1）比较这两个数组的第K/2小的数字midVal1和midVal2的大小，如果第一个数组的第K/2个数字小的话，那么说明我们要找的数字肯定不在nums1中的前K/2个数字，所以我们可以将其淘汰，将nums1的起始位置向后移动K/2个，并且此时的K也自减去K/2，调用递归。2）如果midVal2更小，我们淘汰nums2中的前K/2个数字，并将nums2的起始位置向后移动K/2个，并且此时的K也自减去K/2，调用递归即可。3）如果midVal1=midVal2，此时不能认为函数已经找到了第K个数而直接返回，因为K的奇偶性不知道，所以此时会出错，比如nums1=[1,2],nums2=[1,3]时，如果按照上述策略，当K=2和K=3时会返回一样的值即1，这是不对的，因为int(3/2)=1，所以，当相等时，需要从1或2情况中随便选一种继续递归。直到K=1或一个数组被完全淘汰为止。**参见代码如下：

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), left = (m + n + 1) / 2, right = (m + n + 2) / 2;
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right)) / 2.0;
    }
    int findKth(vector<int>& nums1, int i, vector<int>& nums2, int j, int k) {
        if (i >= nums1.size()) return nums2[j + k - 1];
        if (j >= nums2.size()) return nums1[i + k - 1];
        if (k == 1) return min(nums1[i], nums2[j]);
        int midVal1 = (i + k / 2 - 1 < nums1.size()) ? nums1[i + k / 2 - 1] : INT_MAX;
        int midVal2 = (j + k / 2 - 1 < nums2.size()) ? nums2[j + k / 2 - 1] : INT_MAX;
        if (midVal1 < midVal2) {
            return findKth(nums1, i + k / 2, nums2, j, k - k / 2);
        } else {
            return findKth(nums1, i, nums2, j + k / 2, k - k / 2);
        }
    }
};
```

上面的解法一直使用的是原数组，同时用了两个变量来分别标记当前的起始位置。我们也可以直接生成新的数组，这样就不要用起始位置变量了，不过拷贝数组的操作可能会增加时间复杂度，也许会超出限制，不过就算当个思路拓展也是极好的。首先我们要判断数组是否为空，为空的话，直接在另一个数组找第K个即可。还有一种情况是当K = 1时，表示我们要找第一个元素，只要比较两个数组的第一个元素，返回较小的那个即可。这里我们分别取出两个数组的第K/2个数字的位置坐标i和j，为了避免数组没有第K/2个数组的情况，我们每次都和数组长度做比较，取出较小值。这里跟上面的解法有些许不同，上面解法我们直接取出的是值，而这里我们取出的是位置坐标，但是思想都是很类似的。

还有一种使用二分法迭代查询的更精妙的思路，有时间再看：<https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/very-concise-ologminmn-iterative-solution-with-detailed-explanation>

BitBrave，2019-04-12
（ps：这个题解我使用<https://www.mdeditor.com/>的在线MarkDown编辑器写了三遍，每次都是写完一刷新就没了，下次千万要保存，我都快崩溃了！damn it！）