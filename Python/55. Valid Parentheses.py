class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != parentheses_map[char]:
                    return False
        
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([])"))