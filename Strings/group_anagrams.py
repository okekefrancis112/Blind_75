from collections import Counter, defaultdict
from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list) # mapping charCount to list of Anagrams

#         for s in strs:
#             count = [0] * 26 # a ... z

#             for c in s:
#                 count[ord(c) - ord('a')] += 1

#             res[tuple(count)].append(s)

#         return res.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for k in strs:
            key = "".join(sorted(k))
            d[key].append(k)
        return list(d.values())