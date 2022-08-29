class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []
        while(x > 0):
            digits.append(x % 10)
            x //= 10
        for i in range(len(digits) // 2):
            if digits[i] != digits[-i-1]:
                return False
        return True


test_set = [1, 557933, 415541, 234567899998765432, 12345321, 989898989, 00000000000000]
sol = Solution()
print(sol.isPalindrome(1))
print(sol.isPalindrome(0))
print(sol.isPalindrome(122))
print(sol.isPalindrome(121))