class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        maxVolume = 0
        while(l < r):
            maxVolume = max(maxVolume, min(height[l], height[r])*(r-l) )
            if(height[l] <= height[r]):
                l += 1
            else:
                r -=1
        return maxVolume
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,3,2,5,25,24,5]))