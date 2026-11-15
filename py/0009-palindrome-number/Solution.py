class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        if a<0:
            return False
        for i in range(len(a)//2):
            if a[i] == a[-(i+1)]:
                continue
            else:
                return False
        return True
        
        