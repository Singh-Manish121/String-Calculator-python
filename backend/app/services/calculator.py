import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter_pattern = ",|\n"

    # Check for custom delimiter
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        if len(parts) != 2:
            raise ValueError("Invalid input: missing numbers after delimiter")
        delimiter_line, numbers = parts

        if delimiter_line.startswith("//["):
            delimiter = re.findall(r"\[(.*?)\]", delimiter_line)
            if not delimiter:
                raise ValueError("Invalid custom delimitor format")
        else:
            delimiter = [delimiter_line[2:]]

        delimiter_pattern = "|".join(map(re.escape, delimiter))

    parts = re.split(delimiter_pattern, numbers)

    if any(p == "" for p in parts):
        raise ValueError("Invalid input: consecutive or trailing delimiters")

    nums = [int(p) for p in parts]

    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
    
    nums = [n for n in nums if n <= 1000]
    return sum(nums)
