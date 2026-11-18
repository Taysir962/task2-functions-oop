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
 ## 3. AI Tools Usage Disclosure
AI assistance (Google Gemini) was used during the development of this project for:
- **SQLite Database Integration:** Designing the relational schema (`orders` and `order_items` tables) in `create_db.py` and implementing the database reader in `order_manager/manager.py`.
- **Report Formatting & Troubleshooting:** Aligning the CLI output format in `order_manager/main.py` with the required specification and resolving local Python/Git execution issues.

All code was reviewed, tested locally, and verified before submission. 
