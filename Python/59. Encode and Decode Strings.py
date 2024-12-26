class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs : list[str]) -> str:
        # write your code here
        ans = ''
        for word in strs:
            ans += str(len(word)) + ';' + word
        return ans
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str : str) -> list[str]:
        ans = []
        # write your code here
        i = 0
        while i < len(str):
            word = ''
            length_int = 0
            length_str = ''
            j = i
            while str[j] != ';':
                length_str += str[j]
                j += 1
            length_int = int(length_str)
            for k in range(j + 1, j + 1 + length_int):
                word += str[k]
            ans.append(word)
            i += len(length_str) + len(word) + 1
        return ans
    
if __name__ in "__main__":
    sol = Solution()
    print(sol.encode(["lint","code","love","you"]))
    print(sol.decode("4;lint4;code4;love3;you"))