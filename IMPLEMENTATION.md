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


    
