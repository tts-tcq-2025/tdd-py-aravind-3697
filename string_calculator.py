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
        if not numbers.startswith("//"):
            return ",", numbers
        header, body = numbers.split("\n", 1)
        delimiter = self._parse_header(header)
        return delimiter, body

    def _parse_header(self, header: str) -> str:
        if header.startswith("//[") and header.endswith("]"):
            return header[3:-1]  # multi-character delimiter
        return header[2:]        # single-character delimiter

    def _split_numbers(self, numbers: str, delimiter: str) -> list[str]:
        return numbers.replace(delimiter, ",").replace("\n", ",").split(",")

    def _parse_numbers(self, tokens: list[str]) -> list[int]:
        numbers = [int(t) for t in tokens if t]
        return self._filter_large_numbers(numbers)

    def _filter_large_numbers(self, numbers: list[int]) -> list[int]:
        return [n for n in numbers if n <= 1000]

    def _check_negatives(self, nums: list[int]):
        negatives = self._find_negatives(nums)
        if negatives:
            raise ValueError(f"negatives not allowed: {','.join(map(str, negatives))}")

    def _find_negatives(self, nums: list[int]) -> list[int]:
        return [n for n in nums if n < 0]
