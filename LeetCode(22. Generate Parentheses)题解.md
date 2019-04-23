# LeetCode(22. Generate Parentheses)题解
------
原文如下：
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]


# 解题思路
这道题虽然是Medium，但是我没有想出来。看了别人的代码才有思路。就是一个卡特兰数（具体意思有点看不下去，[链接在此](https://baike.baidu.com/item/%E5%8D%A1%E7%89%B9%E5%85%B0%E6%95%B0/6125746?fr=aladdin)。针对于这个题，就是给定一个数n，然后返回所有的n对括号，括号必须是符合匹配格式的，即任意一个左括号与对应的右括号之间的括号必须是成对的，且左括号必须在右括号之前。

其实这个题和LeetCode的[20题](https://leetcode.com/problems/valid-parentheses/)有些关联，20题是判断一个给定的括号序列是不是匹配的。在思考的过程中，我想到了判断一个括号序列符合良好匹配的一个更简单的原则：**从左到右计算左括号和右括号的个数，不管在哪一步，只要右括号的数目比左括号多，这个序列一定不是良好匹配的，遍历完成之后，左括号与右括号的数目必须相等，否则序列也是不匹配的。**当时我做20题的时候用到了栈结构，现在想来有点多余了，直接线性遍历一下就可以了(重新写了一下，20题有三种括号，直接使用这种方式是不行的比如"([)]"，所以还是老老实实用栈吧)。

回到本题，如何生成给定n下的所有匹配序列呢？这里可以使用一个递归：利用之前提出的简单判断，我们可以利用DPS进行搜索。假设函数generateParenthesis_，具有如下几个参数，输入的需要生成的括号对数n，当前字符中左括号数目left，右括号数目right，存放字符的数组s，记录结果的数组res。初始化运行函数generateParenthesis_(int n,int 0,int 0,string s = "", vectro\<\string\> res)。可以如下写：

    a）当left==right 且 left == n时，表示当前的符号串符合要求。可以将s存入res，res.push_back(s)，返回；否则向下走。
    b）当left<right 或 left+right>=2*n，表示左括号要么比右括号少，或者二者之后大于要求的对数，前者肯定不匹配了，后者在经历了a的条件后保证了left==right和left==n在b中是不可能存在的，也导致了后者left太多使得最终的字符串也是不匹配的，此时可以直接返回；否则继续向下
    c）到了这一步表示s还可以继续增加符号用来匹配，那我在里可以加一个符号"("或者")"，这里不用分先后次序。如果加"("，s+='('，left++，如果加")"，right++，然后依次运行对应的函数即可。

代码如下：
```c++
class Solution {
public:
    void generateParenthesis_(int n,int left,int right, string s, vector<string> &res){
        if(left == right && left == n){
            res.push_back(s);
            return;
        };
        if(left < right || left + right >= 2 * n) return;
        generateParenthesis_(n, left + 1, right, s + '(', res);
        generateParenthesis_(n, left, right + 1, s + ')', res);
        return;
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string s;
        if(n == 0) return res;
        generateParenthesis_(n, 0, 0, s, res);
        return res;
    }
};
```

PS：这个题按照上述代码可以AC，但是效率比较低，仅仅faster than 6%的examples，同时占用的内存比较大。这是因为上述策略就是一个DPS，本来时间复杂度是O(2^n)，但是因为加入了left\<\right之类的剪枝操作，勉强能AC。应当还有更高效的方式。但是我懒得找了。

BitBrave，2019-04-23。



