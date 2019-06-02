# LeetCode(60. Permutation Sequence)题解
------
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
Example 1:

    Input: n = 3, k = 3
    Output: "213"
Example 2:

    Input: n = 4, k = 9
    Output: "2314"

## 解题思路
Medium，给出一个n，将1到n的排列按照组成的数字大小升序排列，取出第K个。

这个题可以暴力遍历，将所有数都记录出来，再取出第K个就可以了。但可以更聪明一点。因为生序排列的话，一定是1XXXXX有n-1！种，然后2XXXXX有n-1！种，然后3XXXXX，4XXXXX.....，因此我们可以用K-(n-1)!，不断减直到下一个为负数为止，这样就可以确定第K个排列数的第一个数字是几。以此类推，在剩下的数里按照上述方式递归。直到最后一个，当n=1的时候，返回这个数即可。

代码如下：

Runtime: 4 ms, faster than 92.50% of C++ online submissions for Permutation Sequence.
Memory Usage: 8.5 MB, less than 54.59% of C++ online submissions for Permutation Sequence.

```c++
class Solution {
public:
    int factorial(int n){
        if (n<=1) return 1;
        return n * factorial(n-1);
    }
    string getKPermutation(vector<char> Vec, int n, int k, string res){
        if(n == 1) return res + Vec[0];
        int tmp = factorial(n-1), c = 0;
        c = k / tmp;
        k = k % tmp;
        if(k % tmp == 0){
            c--;
            k = tmp;
        }

        res += Vec[c];
        Vec.erase(Vec.begin() + c);
        return getKPermutation(Vec, n-1, k, res);
    }
    string getPermutation(int n, int k) {
        vector<char> Vec(n);
        for(int i=0; i<n; i++) Vec[i] = i + 49;
        return getKPermutation(Vec, n, k, "");
    }
};
```

BitBrave, 2019-06-02