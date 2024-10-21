class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count_palindromes = 0
        for i in range(len(s)):
            self.countAroundCenter(s, i, i)
            self.countAroundCenter(s, i, i + 1)
        
        return self.count_palindromes
    def countAroundCenter(self, s: str, left: int, right: int) -> None:
        if not s or left > right:
            return
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.count_palindromes += 1
            left -= 1
            right += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("racecar"))
    print(sol.countSubstrings("racecars"))
    print(sol.countSubstrings("fsdksdf"))

