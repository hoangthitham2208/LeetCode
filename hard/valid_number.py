class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        if not s:
            return False

        has_num = has_dot = has_e = False

        for i in range(n):
            if s[i].isdigit():
                has_num = True
            elif s[i] == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif s[i] in 'eE':
                if has_e or not has_num or i == n - 1:
                    return False
                has_e = True
                has_num = False
            elif s[i] in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
                if i == n - 1 or not s[i + 1].isdigit() and s[i + 1] != '.':
                    return False
            else:
                return False

        return has_num
