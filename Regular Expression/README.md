# Regular Expressions in Python

## Introduction

A Regular Expression, or regex, is a sequence of characters that forms a search pattern. Regular expressions are widely used in various programming languages, including Python, to search, match, and manipulate strings based on specific patterns.

Python’s `re` module provides a powerful set of functions for working with regular expressions. With regex, you can perform tasks like finding specific patterns in text, extracting data, replacing text, and much more. Whether you're working with large datasets, text files, or user inputs, understanding regex can be incredibly valuable.

### Basic Usage

To use regular expressions in Python, you need to import the `re` module. Here's an example of using a regular expression to search for a pattern in a string:

```python
import re

pattern = r"\d+"
text = "The price is $100"
matches = re.findall(pattern, text)

print(matches)  # Output: ['100']

```

# Common Regular Expression Symbols

Here is a breakdown of some of the most common regular expression symbols and their meanings:

1. **`^` (Caret)**
   - **Matches:** The beginning of a line.
   - **Example:** `^Hello` matches any line that starts with "Hello".

2. **`$` (Dollar Sign)**
   - **Matches:** The end of a line.
   - **Example:** `world$` matches any line that ends with "world".

3. **`.` (Dot)**
   - **Matches:** Any single character except newline.
   - **Example:** `a.b` matches "aab", "acb", "a1b", etc., but not "ab".

4. **`\s` (Backslash s)**
   - **Matches:** Any whitespace character (spaces, tabs, newlines).
   - **Example:** `\s+` matches one or more whitespace characters.

5. **`\S` (Backslash Capital S)**
   - **Matches:** Any non-whitespace character.
   - **Example:** `\S+` matches a sequence of non-whitespace characters.

6. **`*` (Asterisk)**
   - **Repeats:** The previous character zero or more times.
   - **Example:** `a*` matches "", "a", "aa", "aaa", etc.

7. **`*?` (Asterisk followed by Question Mark)**
   - **Non-Greedy:** Matches the smallest number of repetitions.
   - **Example:** `a*?` matches as few "a"s as possible.

8. **`+` (Plus Sign)**
   - **Repeats:** The previous character one or more times.
   - **Example:** `a+` matches "a", "aa", "aaa", etc.

9. **`+?` (Plus followed by Question Mark)**
   - **Non-Greedy:** Matches the smallest number of repetitions.
   - **Example:** `a+?` matches as few "a"s as possible.

10. **`[aeiou]` (Square Brackets with Characters)**
    - **Matches:** A single character in the listed set.
    - **Example:** `[aeiou]` matches any vowel.

11. **`[^XYZ]` (Square Brackets with Caret)**
    - **Matches:** A single character not in the listed set.
    - **Example:** `[^XYZ]` matches any character except X, Y, or Z.

12. **`[a-z0-9]` (Range in Square Brackets)**
    - **Matches:** Any character within the specified range.
    - **Example:** `[a-z0-9]` matches any lowercase letter or digit.

13. **`(` (Opening Parenthesis)**
    - **Indicates:** The start of a group, used for capturing or grouping parts of the pattern.
    - **Example:** `(abc)` matches "abc" as a group.

14. **`)` (Closing Parenthesis)**
    - **Indicates:** The end of a group.
    - **Example:** `(\d+)` matches one or more digits and treats them as a group.
