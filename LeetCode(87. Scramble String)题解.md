# LeetCode(87. Scramble String)题解
------
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

    Input: s1 = "great", s2 = "rgeat"
    Output: true
Example 2:

    Input: s1 = "abcde", s2 = "caebd"
    Output: false

## 解题思路

这是一个Hard题，要求说给出两个字符串s1和s2，其中s1字符串可以从不同的位置进行拆分，变成一个完全二叉树（任何一个非叶子节点都有两个孩子节点），然后制定一个非叶子节点时，将其两个孩子节点及其子树交换位置，然后从左到右叶子节点组成一个新的字符串，要求判断s2是不是可以由这样的方式通过s1来生成。

初一看这个题是没有什么头绪的。但是仔细想想，我们会发现假设s2就是s1生成的，那么s1一定采用了某种构建二叉树的方式。第一次在整个s1的某个位置砍一刀分成两个子串成为根节点的两个子节点，然后两个子串又各自按照相同的方式拆分，最后一些位置的节点交换一下位置就可以了。那么我们可以想象得到，**s1如果被拆分为两个子串a和b，那么a中的字符不管最后怎么拆分和交换节点，最后a中的字符串一定全部在b中字符组成的字符串的前面或者后面。**也可以这样说，s2如果一定是s1生成的。那个在s2中一定存在一个拆分的位置，将其分为两个子串a1和b1，其中a1中所有字符的在s1中的对应位置要么全部在b1的所有字符在s1中对应位置的前面，要么全部在后面，因为这相当于将s1拆分为两个子串。然后各自的子串就按照一样的方式比较。

因此算法可以使用DP，递归执行，只有当最后s1和s2都只有一个或两个字符时，可以直接比较，否则直接依次将s2从左到右进行拆分（假设这就是s1拆分的位置），看看能不能由s1形成。能就直接结束返回true，否则就一直遍历到最后，如果直到最后都发现不能则返回false。

这里有一个重要的函数就是比较两个字符串是不是一样的，即用来判断两个字符串是不是由相同种类和数量的字符组成的。比如"abb"和"bab"是一样的，而"abb"和"aab"就不一样。这个方式我首先是使用了map，将s1变成map，记录每个字符的数量，然后用s2的每个字符去erase这个map，最后查看是否empty。这个可以ac，但是有点耗时。

一个可以加速的方式是直接用s2的每个字符去在s1中寻找对应的元素并删除，最后看s1是否是empty。

也可以使用STL的sort函数，将两个string进行排序之后比较是否一样。这后两种方法可以有效提速和减小内存。

使用map的代码如下：

```c++
class Solution {
public:
    bool isSame(string s1, string s2){
        map<char, int> mp;
        int len = s1.size();
        map<char, int>::iterator iter;
        for(int i=0; i<len; i++){
            iter = mp.find(s1[i]);
            if(iter != mp.end()) mp[s1[i]] += 1;
            else mp[s1[i]] = 1;
        }
        
        for(int i=0; i<len; i++){
            iter = mp.find(s2[i]);
            if(iter == mp.end()) return false;
            mp[s2[i]]--;
            if(mp[s2[i]] <=0) mp.erase(s2[i]);
        }
        return true;
    }
    
    bool isScramble(string s1, string s2) {
        if(!isSame(s1, s2)) return false;
        
        int len = s2.size();
        if(len<=2) return true;
        
        bool ret = false;

        for(int i=1; i<len; i++){
            ret = isScramble(s1.substr(0,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(i,len-i), s2.substr(i,len-i));
            if(ret) return true;
            
            ret = isScramble(s1.substr(len-i,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(0,len-i), s2.substr(i,len-i));
            if(ret) return true;
        }
        
        return false;
    }
};
```

使用string的比较的代码如下：

```c++
class Solution {
public:
    bool isSame(string s1, string s2){
        int len = s1.size();
        int pos;
        for(int i=0; i<len; i++){
            pos = s1.find(s2[i]);
            if(pos==-1) return false;
            s1.erase(pos, 1);
        }
        return s1.empty();
    }
    
    bool isScramble(string s1, string s2) {
        if(!isSame(s1, s2)) return false;
        
        int len = s2.size();
        if(len<=2) return true;
        
        bool ret = false;

        for(int i=1; i<len; i++){
            ret = isScramble(s1.substr(0,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(i,len-i), s2.substr(i,len-i));
            if(ret) return true;
            
            ret = isScramble(s1.substr(len-i,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(0,len-i), s2.substr(i,len-i));
            if(ret) return true;
        }
        
        return false;
    }
};
```

使用sort的代码如下：

```c++
class Solution {
public:
    bool isSame(string s1, string s2){
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        return s1==s2;
    }
    
    bool isScramble(string s1, string s2) {
        if(!isSame(s1, s2)) return false;
        
        int len = s2.size();
        if(len<=2) return true;
        
        bool ret = false;

        for(int i=1; i<len; i++){
            ret = isScramble(s1.substr(0,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(i,len-i), s2.substr(i,len-i));
            if(ret) return true;
            
            ret = isScramble(s1.substr(len-i,i), s2.substr(0,i));
            if(ret) ret = ret & isScramble(s1.substr(0,len-i), s2.substr(i,len-i));
            if(ret) return true;
        }
        
        return false;
    }
};
```

BitBrave，2019-05-04。