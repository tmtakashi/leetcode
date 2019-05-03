class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        if len(s) == 0:
            return True

        opening = set('({[')
        matches = set([('(', ')'), ('{', '}'), ('[', ']')])
        stack = []

        if s[0] not in opening:
            return False

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if (stack.pop(), paren) not in matches:
                    return False

        return stack == []
