class Solution:
    def isPalindrome(self, s: str) -> bool:
        singleStr = ''
        # for char in s:
        #     if char.isalnum():
        #         singleStr += char
        singleStr = ''.join(char.lower() for char in s if char.isalnum())
        firstp = 0
        secondp = len(singleStr)-1

        for i in range((len(singleStr))//2):
            if singleStr[firstp] != singleStr[secondp]:
                return False
            else:
                firstp += 1
                secondp -= 1
                # print(firstp,secondp)
        return True


        