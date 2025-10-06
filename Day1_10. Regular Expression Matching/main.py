from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            # Nếu p đã hết, s cũng phải hết
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Trường hợp có '*' ở sau
            if j + 1 < len(p) and p[j + 1] == '*':
                # 0 lần ký tự trước '*', hoặc >=1 lần nếu first_match
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                # Không có '*': phải khớp ký tự hiện tại rồi tiến tiếp
                return first_match and match(i + 1, j + 1)

        return match(0, 0)

print(Solution().isMatch("aa", "a"))    # False
print(Solution().isMatch("aa", "a*"))   # True
print(Solution().isMatch("ab", ".*"))   # True
