class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_word = str(x)
        for i in range(len(x_word)//2):
            if x_word[i] != x_word[len(x_word)-i-1]:
                return False
        return True