"""
Cases to handle. Ranked by importance:
1: character other than + - e .
3: e has no digits before or after
2: + - is not at beggining of all if no e, and not at beggining of section if has e
4: doubles of + - . and no e and doubles of e
5:  + and - in same and no e
6: ?
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
