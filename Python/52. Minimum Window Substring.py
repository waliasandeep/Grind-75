from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        have, need = 0, len(t_counter)
        res, resLength = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            right_char = s[r]
            s_counter[right_char] += 1
            if right_char in t_counter and s_counter[right_char] == t_counter[right_char]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                s_counter[s[l]] -= 1
                if s[l] in t_counter and s_counter[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLength != float("inf"):
            return s[l : r + 1]
        else:
            return ""
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.minWindow("AA", "a"))
    print(sol.minWindow("aa", "a"))
                