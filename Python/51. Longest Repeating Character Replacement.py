class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] not in mp:
                mp[s[right]] = 0
            mp[s[right]] += 1
            #if length of window minus frequency of the most occurring character is greater than k
            #i.e. number of replacements required are greater than k
            while((right - left) + 1) - max(mp.values()) > k:
                left += 1
                mp[s[left]] -= 1
            res = max(res, (right - left) + 1)
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABBA", 2))
    print(sol.characterReplacement("AABABBA", 1))