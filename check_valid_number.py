"""
Cases to handle. Ranked by importance:
1: character other than + - e .
2: e has no digits before or after
3: + - is not at beggining of all if no e, and not at beggining of section if has e
4: doubles of + - . and no e and doubles of e
5:  + and - in same and no e
6: ?
"""
acceptable_chars = ['0','1','2','3','4','5','6','7','8','9','+','-','e','.']
ints = ['0','1','2','3','4','5','6','7','8','9']
acceptable_symbs = ['+','-','e','.']
plu_min = ['+', '-']
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #1: character other than + - e .
        for char in s:
            if char in acceptable_chars:
                continue
            else:
                return False

        #2: e has no digits before or after
        e_check_floater = s
        e_check_floater.replace('+', '')
        e_check_floater.replace('-', '')
        e_check_floater.replace('.', '')
        if e_check_floater.startswith( 'e' ) or e_check_floater.endswith( 'e' ):
            return False

        #3: + - is not at beggining of all if no e, and not at beggining of section if has e
        plu_min_check_floater = s
        plu_min_check_floater.replace('.', '')
        e_case_plu_min_check_floater = []
        if any((plmn in plu_min) for plmn in s):
            if 'e' in s:
                e_case_plu_min_check_floater = plu_min_check_floater.split('e')
                for part in e_case_plu_min_check_floater:
                    if (not part.startswith( 'e' )) or (not part.endswith( 'e' )):
                        return False
            if (not plu_min_check_floater.startswith( 'e' )) or (not plu_min_check_floater.endswith( 'e' )):
                return False

        #4: doubles of + - . and no e and doubles of e
        plu_count = 0
        min_count = 0
        e_count = 0
        per_count = 0
        for char in s:
            if char == "+":
                plu_count = plu_count + 1
            elif char == "-":
                min_count = min_count + 1
            elif char == "e":
                e_count = e_count + 1
            elif char == ".":
                per_count = per_count + 1
            if plu_count > 1 or min_count > 1 or e_count > 1 or per_count > 1:
                return False

        #5:  + and - in same and no e
        if plu_count > 0 and min_count > 0 and e_count == 0:
            return False

        return True
user_input = input("Enter an input to be checked for validity: ")
is_int = Solution.isNumber(user_input, user_input)
if is_int == True:
    print("'" + user_input + "' is a valid number")
else:
    print("'" + user_input + "' is NOT a valid number")
