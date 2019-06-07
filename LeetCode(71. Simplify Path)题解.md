# LeetCode(71. Simplify Path)题解
------
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

    Input: "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

    Input: "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

    Input: "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

    Input: "/a/./b/../../c/"
    Output: "/c"
Example 5:

    Input: "/a/../../b/../c//.//"
    Output: "/c"
Example 6:

    Input: "/a//b////c/d//././/.."
    Output: "/a/b/c"

## 解题思路
Medium， 给出一个字符串代表路径，然后返回对应的最简短的绝对路径。并且要以/开头，如果有字符的话，不能以/结尾

这个题对我来说有点难。主要是不知道怎么判断/../和/./。

但是处理的思路如下：

1 遍历字符串，将所有的//或者多个挨着的/删除为只有一个，因为是重复的
2 字符串中所有的/./类型的变为/
3 遇到/..，应该回退一个路径

代码如下（很多可以优化的地方，懒得）：

Runtime: 4 ms, faster than 99.34% of C++ online submissions for Simplify Path.
Memory Usage: 10.8 MB, less than 63.21% of C++ online submissions for Simplify Path.

```c++
class Solution {
public:
    string simplifyPath(string path) {
        string res = "", tmp;
        int len = path.size(), sta = 0, end = 0, t;
        if(len == 0) return res;
        if(path[0] != '/') {
            path = '/' + path;
            len++;
        }
        if(path[len-1]!='/'){
            path += '/';
            len++;
        }
        for(int i=1; i<len; i++){
            if(path[i-1]=='/' && path[i]=='/'){
                path.erase(i, 1);
                i--;
                len--;
            }
            else if(i>1 && path[i-2]=='/' && path[i-1]=='.' && path[i]=='/'){
                path.erase(i-1, 2);
                i -= 2;
                len -= 2;
            }
        }
        end = path.find('/', sta);
        while(end!=-1){
            if(end-2==sta && path[sta]=='.' && path[sta]=='.'){
                sta = end + 1;
                end = path.find('/', sta);
                t = res.rfind('/', res.size()-2);
                
                if(t!=-1) res = res.substr(0, t+1);
                continue;
            }
            res += path.substr(sta, end-sta+1);
            sta = end + 1;
            end = path.find('/', sta);
        }
        res += path.substr(sta);
        if(res.size()>1 && res[res.size()=='/']) res = res.substr(0, res.size()-1);
        if(res=="") res = "/";
        return res;
    }
};
```

BitBrave, 2019-06-07
