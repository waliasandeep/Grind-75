from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("pup", "pup"))
    print(sol.isAnagram("rain", "train"))
    print(sol.isAnagram("tea", "eat"))