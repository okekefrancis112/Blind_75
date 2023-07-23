from typing import bool


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_next_valid_index(string, index):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                    index -= 1
                elif backspace_count > 0:
                    backspace_count -= 1
                    index -= 1
                else:
                    break
            return index

        s_index = len(s) - 1
        t_index = len(t) - 1

        while s_index >= 0 or t_index >= 0:
            s_index = find_next_valid_index(s, s_index)
            t_index = find_next_valid_index(t, t_index)

            if s_index >= 0 and t_index >= 0 and s[s_index] != t[t_index]:
                return False

            if (s_index >= 0) != (t_index >= 0):
                return False

            s_index -= 1
            t_index -= 1

        return True

