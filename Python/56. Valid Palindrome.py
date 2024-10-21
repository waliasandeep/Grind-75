class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            left_char, right_char = s[l].lower(), s[r].lower()
            if not(self.isAlphaNumeric(left_char)) or not(self.isAlphaNumeric(right_char)):
                if not self.isAlphaNumeric(left_char):
                    l += 1
                if not self.isAlphaNumeric(right_char):
                    r -= 1
            elif left_char != right_char:
                return False
            else:
                l += 1
                r -= 1
        
        return True

    def isAlphaNumeric(self, char) -> bool:
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z") or
                ord("0") <= ord(char) <= ord("9"))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
