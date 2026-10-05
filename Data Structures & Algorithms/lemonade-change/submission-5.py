class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                fives -= 1
                if fives < 0:
                    return False
            else:
                if fives >= 3:
                    fives -= 3
                elif tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                else:
                    return False
        
        return True

        