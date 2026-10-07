class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(c):
            return ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

        a = 0
        b = len(s) - 1
        s = s.lower()
        while a < b:
            if isAlphaNumeric(s[a]):
                if isAlphaNumeric(s[b]):
                    if s[a] != s[b]:
                        return False
                    a+=1
                    b-=1
                else:
                    b-=1
            else:
                a+=1

        return True