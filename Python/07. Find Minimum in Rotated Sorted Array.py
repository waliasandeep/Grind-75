class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,0,1,2]))
    print(sol.findMin([2,1]))