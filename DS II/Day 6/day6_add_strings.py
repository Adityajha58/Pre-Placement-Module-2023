class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1s = []
        for c in num1:
            num1s.insert(0, int(c))
        
        num2s = []
        for c in num2:
            num2s.insert(0, int(c))

        i = 0
        j = 0
        carry = 0

        results = []
        while i < len(num1s) and j < len(num2s):
            digit = (num1s[i] + num2s[j] + carry) % 10
            carry = (num1s[i] + num2s[j] + carry) // 10
            results.insert(0, str(digit))
            i += 1
            j += 1

        while i < len(num1s):
            digit = (num1s[i] + carry) % 10
            carry = (num1s[i] + carry) // 10
            results.insert(0, str(digit))
            i += 1

        while j < len(num2s):
            digit = (num2s[j] + carry) % 10
            carry = (num2s[j] + carry) // 10
            results.insert(0, str(digit))
            j += 1

        if carry > 0:
            results.insert(0, str(carry))
                    
        return "".join(results)
            