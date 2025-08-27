class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter, numbers = self._extract_delimiter(numbers)
        tokens = self._split_numbers(numbers, delimiter)
        nums = self._parse_numbers(tokens)
        self._check_negatives(nums)

        return sum(nums)

    def _extract_delimiter(self, numbers: str) -> (str, str):
        """Extract custom delimiter (single or multi-character) or default to comma."""
        if numbers.startswith("//"):
            header, body = numbers.split("\n", 1)

            if header.startswith("//[") and header.endswith("]"):
                # Multi-character delimiter: //[***]
                delimiter = header[3:-1]   # strip `//[` and trailing `]`
            else:
                # Single-character delimiter: //;
                delimiter = header[2:]

            return delimiter, body
        return ",", numbers

    def _split_numbers(self, numbers: str, delimiter: str) -> list[str]:
        """Normalize delimiters (custom + newline → comma) and split."""
        return numbers.replace(delimiter, ",").replace("\n", ",").split(",")

    def _parse_numbers(self, tokens: list[str]) -> list[int]:
        """Convert tokens to int and filter out >1000."""
        return [int(t) for t in tokens if t and int(t) <= 1000]

    def _check_negatives(self, nums: list[int]):
        """Raise error if negatives exist."""
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {','.join(map(str, negatives))}")
