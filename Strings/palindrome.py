import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str: str = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        l, r = 0, len(new_str) - 1

        while l < r:
            if not new_str[l]:
                l += 1
            elif not new_str[r]:
                r -= 1
            elif new_str[l] != new_str[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
