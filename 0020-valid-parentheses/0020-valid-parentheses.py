class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                l.append(s[i])

            elif s[i] in [")", "]", "}"]:
                if len(l) == 0:
                    return False

                x = l.pop(-1)

                if s[i] == ")" and x != "(":
                    return False
                if s[i] == "]" and x != "[":
                    return False
                if s[i] == "}" and x != "{":
                    return False

        return len(l) == 0
