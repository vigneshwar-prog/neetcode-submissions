class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_string = ""
        for char in s:
            if char>='A' and char<='Z':
                clear_string += chr(ord(char)+32)
            elif char>='a' and char<='z' or char>='0' and char<='9':
                clear_string += char
        if clear_string == clear_string[::-1]:
            return True
        return False
