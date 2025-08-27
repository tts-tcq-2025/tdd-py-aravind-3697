class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1].replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")
        nums = numbers.split(",")
        return sum(int(n) for n in nums)
        nums = [int(n) for n in numbers.split(",") if int(n) <= 1000]
negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {','.join(map(str, negatives))}")
        return sum(nums)


        
