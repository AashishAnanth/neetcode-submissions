class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        x = len(a) - 1
        y = len(b) - 1
        carry = 0

        while x >= 0 or y >= 0 or carry:
            total = carry
            if x >= 0:
                total += int(a[x])
                x -= 1
            if y >= 0:
                total += int(b[y])
                y -= 1

            res.append(str(total % 2))
            carry = total // 2
        
        return "".join(reversed(res))

