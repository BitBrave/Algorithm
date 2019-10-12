# LeetCode(858. Mirror Reflection)题解

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered `0`, `1`, and `2`.

The square room has walls of length `p`, and a laser ray from the southwest corner first meets the east wall at a distance `q` from the `0`th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

**Example 1:**

```
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
```

**Note:**

1. `1 <= p <= 1000`
2. `0 <= q <= p`

## 解题思路

有一个正方形的房间，有一束光从左下角射入，保证最后一定会到达其余三个角中的一个，求出能到达的第一个角的位置编号。

先说说我的解法，完全是最死板的方法，计算每一次反射的落点，可以知道光线在传播的过程中与正方形的边形成的三角形是相似的，并且光线无论何时都与正方形的横边的夹角是一样的，与竖边的夹角也是始终不变的。因此在知道光线的前两个在墙壁上的落点，就可以知道其下一个落点。

就这样，使用一个函数，输入前两个落点，返回光线第三个落点，然后判断这个落点是不是角。

特别注意，特别注意，特别注意！用C++或者python实现的时候，因为数据精度的问题，明明正确答案，总是会因为精度限制导致不能相等，从而不能AC，我花了好多时间在这上面debug。最后用python用一个比较笨的法子，使用round函数四舍五入，当然在这之前要扩大范围。最后算是AC了。

`Runtime: 52 ms, faster than 6.06% of Python3 online submissions for Mirror Reflection.`

`Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Mirror Reflection.`

```python
# my solution algorithm
class Solution(object):
    p = 0.0
    x, y = 0.0, 0.0
    tan_a, tan_b = 0.0, 0.0
    def findNextPoint(self, a, b, c, d):
        global p, x, y, tan_a, tan_b
    
        if d == 0: 
            if a < c:
                if (p-c)*tan_a < p:  x = p; y = (p-c) * tan_a
                else: x = c + p * tan_b; y = p
            else:
                if c*tan_a < p: x = 0; y = c * tan_a
                else: x = c - p * tan_b; y = p
        elif d == p:
            if a < c:
                if (p-c)*tan_a < p: x = p; y = p - (p-c) * tan_a
                else: x = c + p * tan_b; y = 0
            else:
                if c*tan_a < p: x = 0; y = p - c * tan_a
                else: x = c - p * tan_b; y = 0
        elif c == 0:
            if b < d:
                if (p-d)*tan_b < p: x = (p-d)*tan_b; y = p
                else: x = p; y = d + p * tan_a
            else:
                if d*tan_b < p: x = d * tan_b; y = 0
                else: x = p; y = d - p * tan_a
        elif c == p: 
            if b < d:
                if (p-d)*tan_b < p: x = p - (p-d) * tan_b; y = p 
                else: x = 0; y = d + p * tan_a 
            else:
                if d*tan_b < p: x = p - d * tan_b; y = 0
                else: x = 0; y = d - p * tan_a
        return
        
    def mirrorReflection(self, p_, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        global p, x, y, tan_a, tan_b
        a, b, c, d = 0, 0, p_, q
        if d == p_: return 1

        p = p_
        tan_a = q / p
        tan_b = p / q; 
        while True:
            self.findNextPoint(a, b, c, d)

            x = round(x*10000000) / 10000000.0
            y = round(y*10000000) / 10000000.0

            if x == p and y == 0: return 0
            elif x == p and y == p: return 1
            elif x == 0 and y == p: return 2
            a, b, c, d = c, d, x, y
        return -1
```

以上我用笨办法一步步做出来的，后来参考网上的资料发现这个题有更简单的办法。一般来说，数学算法题都是可以使用比较精妙的办法解决的。参考资料在此，[点击链接](https://www.cnblogs.com/grandyang/p/10646040.html)。

思路就是，翻转光线太麻烦，直接翻转房间，偶数房间翻转是与原始房间镜面对称的，而奇数房间翻转是与原始房间相同的。同时，根据p/q的比值（要进行化简），分别确定正方形像右和向上的翻转次数，从而确保光线可以直接沿直线到达右上角。然后根据此时右上角的房间的角编号确定是角。

总体来说如下：

​	1、p为奇数，q为奇数，右上角编号为1；

​	2、p为奇数，q为偶数，右上角编号为0；

​	3、p为偶数，q为奇数，右上角编号为2；

这里要注意，是没有q和p同时为偶数的，这是因为同时为偶数的时候，p和q可以化简，直到两个不全为偶数。比如4和2与2和1其实是一样的，因此，可以先得到p和q的最大公约数，然后各自除去这个公约数，再按照上述判断。

这样优化之后，时间复杂度O(1), 空间复杂度O(1)，代码如下。

`Runtime: 0 ms, faster than 100.00% of C++ online submissions for Mirror Reflection.`

`Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Mirror Reflection.`

```C++
class Solution {   
public:
    int gcd(int a, int b){
        return (a % b == 0) ? b : gcd(b, a % b);
    }
    int mirrorReflection(int p, int q) {
        int r = gcd(p, q);
        p = p / r;
        q = q / r;

        return 1 - p % 2 + q % 2; 
    }
};
```

BitBrave，2019-10-08