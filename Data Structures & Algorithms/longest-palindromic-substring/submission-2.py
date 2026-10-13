class Solution:
    def longestPalindrome(self, s: str) -> str:
        lbest, rbest = 0, 0
        n = len(s)
        for i in range(n):
            l, h = i-1, i+1
            curr = 1
            while l >= 0 and h < n:
                if s[l] != s[h]:
                    break
                else:
                    curr += 2
                    l -= 1
                    h += 1
            
            if curr > rbest - lbest:
                lbest, rbest = l+1, h-1

        for i in range(1, n):
            l, h = i-1, i
            curr = 0
            while l >= 0 and h < n:
                if s[l] != s[h]:
                    break
                else:
                    curr += 2
                    l -= 1
                    h += 1
            
            if curr > rbest - lbest:
                lbest, rbest = l+1, h-1
        
        return s[lbest:rbest+1]

        
            