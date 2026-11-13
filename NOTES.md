# Project Notes & Documentation

## 1. Difficulties & Solutions
- **Module Imports Across Directories:** Managing relative imports and path resolutions between subdirectories (`functions`, `oop`, `order_manager`) was initially tricky. This was successfully resolved by adjusting `sys.path` dynamically or executing scripts from the root directory to maintain clean module boundaries.
- **Data Validation & Exception Handling:** Ensuring that invalid inputs (such as negative prices, missing customer names, or non-integer quantities) were properly caught and stored in the rejected orders list without crashing the program required rigorous exception handling using `try/except` blocks.

## 2. F6 Scope Answer (Scope Drill)
- **Code snippet:**
  ```python
  total = 100
  def add_bonus(amount):
      total = amount + 10
      return total
  result = add_bonus(5)
  print(total, result)