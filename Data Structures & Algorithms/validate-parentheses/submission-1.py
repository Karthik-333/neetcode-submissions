class Solution:
    def isValid(self, s: str) -> bool:
        # l=0
        # r=len(s)-1
        # while l>r:    
        #     if s[l]!=s[r]:
        #         return False
        # return True        
        stack=[]
        closeToOpen={'}':'{',']':'[',')':'('}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                    