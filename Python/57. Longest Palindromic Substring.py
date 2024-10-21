class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            len_odd = self.expandAroundCenter(s, i, i)
            len_even = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len_odd, len_even)
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            
        return s[start : end + 1]

    def expandAroundCenter(self, s : str, left : int, right : int) -> int:
        if not s or left > right:
            return 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("noon"))
    print(sol.longestPalindrome("racecar"))
    print(sol.longestPalindrome("moon"))