import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        numbers = numbers.replace("\n", ",")
        nums = numbers.split(",")
        return sum(int(n) for n in nums)
