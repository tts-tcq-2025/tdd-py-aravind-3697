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

## Summary of Requirements

1. In case of Empty string "" → return 0.
2. In case of Single number (Eg. : "1") → return the same single number (Expected Result from Eg. return 1 ).
3. For Two numbers (Eg. "1,2") → return sum of two numbers (Expected sum from example : 3 ).
4. Incase of Unknown number of entries → sum them all.
5. If there's a Newline (\n), this can also separate numbers. (Eg. "1\n2,3" → It should return 6) .
6. Custom delimiter support:
      Expected in Format: "//[delimiter]\n[numbers]", (Eg. "//;\n1;2" → 3).
      Delimiters can also be multiple characters: (Eg. "//[***]\n1***2***3" → 6 ).
7. Incase of Negative numbers, it should throw an exception saying "negatives not allowed: <negatives>".
8. If the Numbers are greater than 1000, then ignore.
9. Overall the code should maintain low complexity and high test coverage.
