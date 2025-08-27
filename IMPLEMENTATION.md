-------------------------------------------------------------------------------------------------------------------------

# 🧮 TDD-Driven String Calculator

A Python implementation of the **String Calculator**, developed strictly using **Test-Driven Development (TDD)**.  
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

## GHERKIN based scenarios (Based on Requirements)

- **Feature: String Calculator**
-     As a user, I want to add numbers from a string input. So that I can get their sum while supporting custom delimiters, newlines, and validation rules
- Background:
-     Given a StringCalculator instance

- **Scenario 1: Add an empty string**.
  `Given the input string is ""
   When I call add()
   Then the result should be 0.`

- **Scenario 2: Add a single number**
  `Given the input string is "5"
   When I call add()
   Then the result should be 5`

- **Scenario 3: Add two numbers separated by a comma**
   `Given the input string is "1,2"
    When I call add()
    Then the result should be 3`

- **Scenario 4: Add multiple numbers**
   `Given the input string is "1,2,3,4"
    When I call add()
    Then the result should be 10`

- **Scenario 5: Support newline as delimiter**
   `Given the input string is "1\n2,3"
    When I call add()
    Then the result should be 6`

- **Scenario 6: Use a custom single-character delimiter**
   `Given the input string is "//;\n1;2;3"
    When I call add()
    Then the result should be 6`

- **Scenario 7: Use a custom multi-character delimiter**
   `Given the input string is "//[***]\n1***2***3"
    When I call add()
    Then the result should be 6`

- **Scenario 8: Ignore numbers greater than 1000**
   `Given the input string is "2,1001"
    When I call add()
    Then the result should be 2`

- **Scenario 9: Raise exception for negative numbers**
   `Given the input string is "-1,2,-3"
    When I call add()
    Then a ValueError should be raised with message "negatives not allowed: -1,-3"`


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

## 4️⃣ Usage Examples

```python
from string_calculator import StringCalculator

calc = StringCalculator()

print(calc.add(""))          # 0
print(calc.add("5"))         # 5
print(calc.add("1,2,3"))     # 6
print(calc.add("1\n2,3"))    # 6
print(calc.add("//;\n1;2"))  # 3
print(calc.add("//[***]\n1***2***3"))  # 6
```


Negative number case:
```python
try:
    calc.add("1,-2,3,-4")
except ValueError as e:
    print(e)  # negatives not allowed: -2,-4
```

---

## 5️⃣ TDD Process Followed

1. Red: Write the smallest failing test.
    Example: "" → 0

2. Green: Write the minimal implementation to pass the test.
    Add condition if numbers == "": return 0

3. Refactor: Improve code without breaking tests.

4. Repeat cycle for each new requirement:
      Single number
      Two numbers
      Multiple numbers
      Newline delimiter
      Custom delimiter
      Negative number exception
      Ignore numbers > 1000
      Long delimiters

Each feature was introduced only after a test demanded it.

## 6️⃣ Files

- string_calculator.py – implementation of StringCalculator
- test_string_calculator.py – unit tests with pytest
- .github/workflows/ – automation of quality checks
  
        - main-workflow.yml – tests + coverage
        - limit-complexity.yml – CCN enforcement
        - no-dups.yml – duplicate code check
        - lint.yml – linting rules
- README.md – documentation (this file)


    
