# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 思路：拿第一个字符串作为参考基准，外层循环每次获取基准字符串的一个字符，
# 内循环负责对比每一个字符串相应位置的字符是否相同，相同就把该字符连接到ans上

class Solution:
    def CommenPrefix(self,strs:list[str]):
        if not strs :
            return ""
        n = len(strs)       # 获取内层循环的次数
        m = len(strs[0])    # 外层循环
        ans = ""
        c = ""
        for j in range(m):
            c = strs[0][j]  # 从基准字符串取出字符
            for i in range(1,n):
                if j>=len(strs[i]) or strs[i][j]!=c:  # 判断字符串是否走完或者待判断字符串是否不同
                    return ans
            ans = ans + c   #判断完所有字符串链接一次字符
        return ans        
s=Solution()
print(s.CommenPrefix(["forget","forige","forever"])) # for
print(s.CommenPrefix(["hello"]))    # hello
print(s.CommenPrefix([""]))         # ""




