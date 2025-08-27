# TDD Driven StringCalculator

Build a StringCalculator functionality that can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.

> DO NOT jump into implementation! Read the example and the starting task below.

- For an empty string it will return 0
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: “1\n2,3” (will equal 6)
  - the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
- Support different delimiters : to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
- Calling Method with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. if there are multiple negatives, show all of them in the exception message.
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

## Tasks



Establish quality parameters:

- Ensure  maximum complexity (CCN) per function == 3

- Ensure 100% line and branch coverage at every step

  

Start Test-driven approach

1. Write the smallest possible failing test: give input `"" assert output to be 0 ` .
2. Write the minimum amount of code that'll make it pass.
3. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.

-------------------------------------------------------------------------------------------------------------------------

# 🧮 TDD-Driven String Calculator

A Python implementation of the **String Calculator Kata**, developed strictly using **Test-Driven Development (TDD)**.  
The project emphasizes clean design, incremental development, and strong quality gates (coverage, complexity, duplication).

---

## 1️⃣ Test Specifications (Based on Requirements)

- **Empty string** → returns `0`
- **Single number** → returns that number  
  - `"1"` → `1`
- **Two numbers** → returns their sum  
  - `"1,2"` → `3`
- **Unknown number of numbers** → sums them all  
  - `"1,2,3,4"` → `10`
- **Newlines allowed as delimiters**  
  - `"1\n2,3"` → `6`
- **Custom delimiters supported**  
  - `"//;\n1;2"` → `3`  
  - `"//[***]\n1***2***3"` → `6`
- **Negative numbers not allowed**  
  - `"1,-2,-3"` → raises `ValueError("negatives not allowed: -2,-3")`
- **Numbers greater than 1000 are ignored**  
  - `"2,1001"` → `2`

---

## 2️⃣ Features Implemented

✔ Empty input returns `0`  
✔ Handles single and multiple numbers  
✔ Comma and newline delimiters  
✔ Custom delimiters of variable length  
✔ Exception on negative numbers with all negatives listed  
✔ Ignores numbers > 1000  
✔ Extensible for future delimiter rules  

---

## 3️⃣ Quality Metrics

- **Cyclomatic Complexity (CCN):**  
  - Each function kept ≤ **3**  
- **Coverage:**  
  - **100% line and branch coverage** enforced using `coverage.py`  
- **Duplication:**  
  - Verified with **jscpd**, threshold set to `0`  

---

## 4️⃣ Architecture
│── string_calculator.py # Core implementation (StringCalculator class)
│── test_string_calculator.py # Unit tests written with pytest
│── README.md # Project documentation

---

## 5️⃣ Usage Examples

```python
from string_calculator import StringCalculator

calc = StringCalculator()

print(calc.add(""))          # 0
print(calc.add("5"))         # 5
print(calc.add("1,2,3"))     # 6
print(calc.add("1\n2,3"))    # 6
print(calc.add("//;\n1;2"))  # 3
print(calc.add("//[***]\n1***2***3"))  # 6

Negative number case:
try:
    calc.add("1,-2,3,-4")
except ValueError as e:
    print(e)  # negatives not allowed: -2,-4

---

6️⃣ TDD Process Followed

Red: Write the smallest failing test.
Example: "" → 0
Green: Write the minimal implementation to pass the test.

Add condition if numbers == "": return 0
Refactor: Improve code without breaking tests.
Repeat cycle for each new requirement:
Single number
Two numbers
Multiple numbers
Newline delimiter
Custom delimiter
Negative number exception
Ignore numbers > 1000
Long delimiters

Each feature was introduced only after a test demanded it.


