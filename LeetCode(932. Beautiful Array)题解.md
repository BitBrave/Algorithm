# LeetCode(932. Beautiful Array)题解

For some fixed `N`, an array `A` is *beautiful* if it is a permutation of the integers `1, 2, ..., N`, such that:

For every `i < j`, there is **no** `k` with `i < k < j` such that `A[k] * 2 = A[i] + A[j]`.

Given `N`, return **any** beautiful array `A`.  (It is guaranteed that one exists.)

 

**Example 1:**

```
Input: 4
Output: [2,1,4,3]
```

**Example 2:**

```
Input: 5
Output: [3,1,2,5,4]
```

 

**Note:**

- `1 <= N <= 1000`

## 解题思路

给出一个数N，要求返回一个由1,2,3,4,...N的数组，这个数组必须是一个漂亮数组。即，任意A[i]和A[j]之间，即i<k<j，都有A[i]+A[j]!=2\*A[k]。

这个题可以使用DC的办法解决。首先假设一个数组B是漂亮数组，那么B中的元素整体加减一个元素和整体乘上除上一个数得到的数组仍然是一个漂亮数组。因为如果B[i]+B[j] != 2\*B[k]，那么.

- B[i]+a+B[j]+a != 2\*(B[k]+a)
- B[i]\*a+B[j]\*a != 2\*(B[k]\*a)

而观察可知，中间元素的两倍一定是一个偶数，因此只要保证B[i]+B[j] 等于一个奇数一定就可以满足k位置元素的要求了。

那么可以假设这样一个数组A，元素分别是1,2,3,...N。我们将其分成两组数，在左边分别放奇数1,3,5,7, ...,一共(N+1)/2个，右边放上2,4,6,8,...一共N/2个。假设这两个数组内部是漂亮数组，那么这两个数组左右组合起来，也一定是一个漂亮数组。

观察左边，将所有元素+1得到2,4,6,8,...，再除二就得到一个1,2,3,4,...共(N+1)/2的和一开始一样的数组。

观察右边，将所有元素除二就得到一个1,2,3,4,...共N/2的和一开始一样的数组。

这两个数组和一开始一样，只不过规模变小，并且只要这两个数组构成了漂亮数组，左边的只需要所有元素乘2-1，右边乘2，组合在一起就是初始问题的解。

因此一个N的问题就变成了一个(N+1)/2和N/2的两个规模的问题。

这个问题可以使用递归的办法解决,代码如下，时间复杂度O(nlogn)，空间复杂度O(1).

`Runtime: 16 ms, faster than 31.48% of C++ online submissions for Beautiful Array.`

`Memory Usage: 19.8 MB, less than 100.00% of C++ online submissions for Beautiful Array.`

```C++
class Solution {
public:
    vector<int> beautifulArray(int N) {
        if(N == 0) return vector<int>();
        if(N == 1) return vector<int>({1});
        vector<int> left = beautifulArray((N+1)/2), right = beautifulArray(N/2), ret;
        for(int a : left) ret.push_back(a*2-1);
        for(int a : right) ret.push_back(a*2);
        return ret;
    }
};
```

但是上述递归还是花费太多时间了因为折半的时候对于N=1,2,3这样的低阶计算了很多次，一个办法是将对应的答案存储起来，最后时间复杂度只需要O(N)，但需要O(N)的空间复杂度(1+2+4+...+N)。

这里还有一个优化的办法，观察数组有以下性质，假设有一个N+1的漂亮数组，现在删除掉其中的N+1，剩下的额仍旧是漂亮数组，因为如果不是的话，那么加上N+1之后也就不是了。因此推论出，一个为N的漂亮数组，可以依次删除N,N-1,N-2等数得到一个更低阶的漂亮数组。

因此，一个N的问题是这样增长过来的，以左边和右边数组的各自的元素长度计算来说分别是说。

- 1,1->2,2->4,4->4,4->...->m,m。直到2*m>=N.

因此，这个题可以从左边为1个元素，右边为1个元素开始，逐步增加。每次增加，到达M时，都将当前数组的元素整体乘2-1作为M+1数组的左边，整体*2作为M+1的右边。知道数组长度大于等于N就停下，然后从中删除那些大于N的元素即可。

这样的时间复杂度O(n)，空间复杂度O(1)。（均不计算答案的空间）。代码如下。

`Runtime: 4 ms, faster than 99.72% of C++ online submissions for Beautiful Array.`

`Memory Usage: 8.8 MB, less than 100.00% of C++ online submissions for Beautiful Array.`

```c++
class Solution {
public:
    vector<int> beautifulArray(int N) {
        vector<int> V({1,2}), ret;
        int M = 2;
        while(M < N){
            V.insert(V.end(), V.begin(), V.end());
            for(int i=0; i<M; i++) V[i] = V[i] * 2 -1;
            for(int i=M; i<2*M; i++) V[i] = V[i] * 2;
            M *= 2;
        }
        for(int i=0; i<M; i++){
            if(V[i] <= N) ret.push_back(V[i]);
        }
        return ret;
    }
};
```

BitBrave，2019-11-13