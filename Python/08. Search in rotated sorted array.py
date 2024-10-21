class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while(l <= r ):
            mid = (l + r) // 2
            if(nums[mid] == target):
                return mid
            #Check if left half is sorted
            if nums[l] <= nums[mid]:
                if  target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            #Right half is sorted
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))