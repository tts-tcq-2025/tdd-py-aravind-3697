class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            header, numbers = parts[0], parts[1]
            match = re.match(r"//\[(.+)\]", header)
            if match:
                delimiter = match.group(1)
            else:
                delimiter = header[2:]

        numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")
        tokens = numbers.split(",")
        nums = [int(n) for n in tokens if n and int(n) <= 1000]
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {','.join(map(str, negatives))}")

        return sum(nums)
