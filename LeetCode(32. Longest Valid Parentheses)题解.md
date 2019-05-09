# LeetCode(32. Longest Valid Parentheses)题解
------
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"
Example 2:

    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"

## 解题思路

Hard题，题目要求给定一串由"("和")"组成的字符串，然后判断这个字符串内最大的合法字符串的长度是多少。

### 解法1（完全自我推断,时间复杂度O(n2), 空间复杂度O(1)）
一个思路是，从每一个位置开始，然后逐步遍历到最后看当前字符串是否是合法的。（当从左到右数，任意位置下，当前的"("的数量是大于等于")"的数量，并且当"("的数量等于")"时，表示这个字符串是相等的。时间复杂度O(n2)

代码如下，非常慢（624ms，faster than 5.73% examples，但内存9.2 MB, less than 99.43%）:

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0, len = s.size();
        int left = 0, right = 0;
        
        for(int i=0; i<len; i++){
            left = 0;
            right = 0;
            for(int j=i; j<len; j++){
                if(s[j]=='(') left++;
                else right++;
                
                if(left==right) ret = max(ret, left+right);
                else if(left<right) break;
            }
        }
        return ret;
    }
};
```

下面的方法均参考别人的解法，理解之后完成代码。

### 解法2(时间复杂度O(n),空间复杂度O(n))
使用栈结构
使用一个栈来存储位置，初始化一个值sta=0，用来记录合法字符串的起点，一个值ret记录目前的最长的有效字符串。从左到右遍历s，遇到左括号就压入位置。遇到右括号时，有以下几种情况。

1 当前栈内为空，表示右括号没有匹配，则丢弃即可。将sta设为当前右括号的下一个位置。
2 当前不为空，且弹出当前字符，此时且栈内为空，表示目前遍历的字符串是匹配的，更新ret = max(ret, i-sta+1)
3 当前不为空，且弹出当前字符，此时且栈内也不为空，表示目前遍历的字符串中栈顶元素所在位置往后数到i都是匹配的，更新ret = max(ret, i-栈顶元素所在位置)

代码如下：
Runtime: 4 ms, faster than 99.94% of C++ online submissions for Longest Valid Parentheses.
Memory Usage: 9.7 MB, less than 98.85% of C++ online submissions for Longest Valid Parentheses.
```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0, sta = 0, len = s.size();
        stack<int> st;
        for(int i=0; i<len; i++){
            if(s[i]=='(') st.push(i);
            else{ // ')'
                if(st.empty()) sta = i+1;
                else{
                    st.pop();
                    ret = max(ret, st.empty() ? i-sta+1:i-st.top());
                }
            }
        }
        return ret;
    }
};
```

### 解法3(时间复杂度O(n),空间复杂度O(n))
使用DP, 建立一个数组与s的长度一致。dp[i]表示从s[0]开始以s[i]作为有效合法字符串的结尾字符时的有效合法字符串最长长度。

首先初始化所有dp元素为0，然后从头到尾遍历s，当遍历到s[i]时，有如下几种情况。

1 s[i]为左括号，直接设置dp[i]==0，因为以左括号结尾的字符串不会是合法字符串。
2 s[i]为右括号，有如下几种情况
2.1 s[i-1]为左括号，表示二者匹配，那么可以直接就在dp[i-2]的基础上+2即可
2.2 s[i-1]为右括号，这表示其可能与前面的某个左括号已经匹配了（形成了"(******)"），那么我们就需要刨除掉这个匹配序列（包括中间的），直接查看s\[i-1-dp\[i-1\]\]，又有如下两种情况。
2.2.1 s\[i-1-dp\[i-1\]\]为左括号，表示其与s[i]匹配，那么可以直接就在dp[i-1]的基础上+2，但这时候还要注意s\[i-1-dp\[i-1\]\]前面可能还有匹配的，因此要再加上dp\[i-1-dp\[i-1\]-1\]。
2.2.2 s[i-1]为右括号，表示二者不匹配，dp[i]等于0即可 

其实还有一种反向的，使用DP, 建立一个数组与s的长度一致。dp[i]表示以s[i]开始的到结尾字符时的有效合法字符串的最长长度。但原理是一模一样的，只是换个方向而已。

代码如下：
Runtime: 8 ms, faster than 98.56% of C++ online submissions for Longest Valid Parentheses.
Memory Usage: 9.6 MB, less than 98.85% of C++ online submissions for Longest Valid Parentheses.
```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0, len = s.size();
        if(len<=1) return 0;
        
        vector<int> dp(len, 0);
        for(int i=0; i<len; i++){
            if(s[i]=='(') dp[i] = 0;
            else{ // ')'
                if(i<1) continue;
                if(s[i-1]=='(') dp[i] = 2 + (i<2 ? 0 : dp[i-2]);
                else dp[i] = i-1-dp[i-1]>=0 &&  s[i-1-dp[i-1]]=='('? (dp[i-1] + 2 + (i-2-dp[i-1]>=0 ? dp[i-2-dp[i-1]] : 0)) : 0;
            }
            ret = max(ret, dp[i]);
        }
        return ret;
    }
};
```

### 解法4(时间复杂度O(n),空间复杂度O(1)) 个人觉得是最棒的思路
从头到尾遍历s，再从尾到头遍历s，二次遍历即可。

首先从左到右，使用left记录遇到的左括号数，right记录遇到的右括号数。当left==right时，更新ret=max(ret, left+right)，当左括号比右括号多时就不管，但是右括号比左括号多的时候就表示这个已经不匹配了，就从当前位置的下一个重新开始计数。

然后从右到左，使用left记录遇到的左括号数，right记录遇到的右括号数。当left==right时，更新ret=max(ret, left+right)，当右括号比比括号多时就不管，但是左括号比右括号多的时候就表示这个已经不匹配了，就从当前位置的下一个重新开始计数。

解释，前后两遍遍历其实是将多余的左括号和右括号的情况都涵盖了进来，当序列中左括号多时，从后往前可以得到最多的。当右括号多时，从左往右可以计算出来。

代码如下：
Runtime: 8 ms, faster than 98.56% of C++ online submissions for Longest Valid Parentheses.
Memory Usage: 9.2 MB, less than 99.43% of C++ online submissions for Longest Valid Parentheses.

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int ret = 0, len = s.size();
        int left = 0, right = 0;
        
        for(int i=0; i<len; i++){
            s[i] == '(' ? left++ : right++;
            if(left==right) ret = max(ret, left*2);
            else if(left<right) {
                left = 0;
                right = 0;
            }
        }
        
        left = 0; right = 0;
        for(int i=len-1; i>=0; i--){
            s[i] == '(' ? left++ : right++;
            if(left==right) ret = max(ret, left*2);
            else if(left>right){
                left = 0;
                right = 0;
            }
        }
        
        return ret;
    }
};
```

BitBrave, 2019-05-08