"""Leet code problems from Aug, 2024"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            return self.handle(digits, len(digits) - 1)
        else:
            digits[-1] += 1
            return digits

    def handle(self, digits, idx):
        """
        Helper function to recursively handle the case if the last
        digit is 9
        """
        if idx == 0:
            digits[idx] = 0
            digits.insert(0, 1)
            return digits
        elif (idx - 1) == 0 and digits[idx - 1] == 9:
            digits[idx] = 0
            digits[idx - 1] = 0
            digits.insert(0, 1)
            return digits
        elif digits[idx - 1] != 9:
            digits[idx] = 0
            digits[idx - 1] += 1
            return digits
        else:
            digits[idx] = 0
            self.handle(digits, idx - 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([8, 9, 9, 9]))
