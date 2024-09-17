"""https://leetcode.com/problems/maximum-product-subarray/"""
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prefix, postfix = 1, 1
        n = len(nums)
        ans = nums[0]
        
        for i in range(0, n):
            if prefix == 0:
                prefix = 1
            if postfix == 0:
                postfix = 1
            prefix *= nums[i]
            postfix *= nums[n - i - 1]
            ans = max(ans, prefix, postfix)
        
        return ans
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))

