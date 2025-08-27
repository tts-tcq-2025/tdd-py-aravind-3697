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
        
