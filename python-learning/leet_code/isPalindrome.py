# 判断是否为回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


# Solution1
# 转换为字符串
class Solution1:
    def isPalindrome(self,x:int)->bool:
        if x<0:
            return False
        s=str(x)
        return s==s[::-1]
s1 = Solution1()
print("--------Solution1-----------")
print(s1.isPalindrome(121))     # True
print(s1.isPalindrome(-121))    # False
print(s1.isPalindrome(10))      # False
print(s1.isPalindrome(0))       # True
print(s1.isPalindrome(12321))   # True


# Solution2
# 不转字符
class Solution2:
    def isPalindrome(self,x:int)->bool:
        if x<0:
            return False
        lis=[]
        while x!=0:
            lis.append(x%10)
            x=x//10
        return lis[:]==lis[::-1]
print("--------Solution2-----------")
s2=Solution2()
print(s2.isPalindrome(121))     # True
print(s2.isPalindrome(-121))    # False
print(s2.isPalindrome(10))      # False
print(s2.isPalindrome(0))       # True
print(s2.isPalindrome(12321))   # True
