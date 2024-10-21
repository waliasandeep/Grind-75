from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #dict = defaultdict(list)
        dict = {}
        for word in strs:
            char_arr = [0] * 26
            for char in word:
                char_arr[ord(char) - ord("a")] += 1
            
            key = tuple(char_arr)
            if key not in dict.keys():
                dict[key] = []
            dict[key].append(word)
        
        return dict.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))