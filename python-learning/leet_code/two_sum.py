# 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。


#   双循环暴力求解，时间复杂度o(n^2),空间复杂度o(n)
class Solution1:
    def twoSum(self,nums:list[int],target:int) ->list[int]:
        n=len(nums)
        for i in range(n):      # for循环， in后面要用range(次数)
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return(i,j)
s1=Solution1()        # 实例化：s=实例对象()括号必须加
ans1=s1.twoSum([2,3,4,5],9)
print("Solution1\n",ans1)


# 哈希字典，键值对求解，时间复杂度o(n),空间复杂度o(n)
class Solution2:
    def twoSum(self,nums:list[int],target:int) ->list[int]:
        hashmap={}
        for idx,num in enumerate(nums):     #
            need=target-num
            if need in hashmap:
                return(hashmap[need],idx)
            hashmap[num]=idx
s2=Solution2()
ans2=s2.twoSum([3,4,5,6],8)
print("Solution2\n",ans2)

