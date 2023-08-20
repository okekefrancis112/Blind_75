# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def helper(L,R):
#             local_cntr=0
#             while L>=0 and R<len(s) and s[L]==s[R]:
#                 local_cntr+=1
#                 L-=1
#                 R+=1
#             return local_cntr
#         cntr = 0
#         for i in range(len(s)):
#             cntr+=helper(i,i)
#             cntr+=helper(i,i+1)
#         return cntr

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

        return res