
# F1: Rewrites from Week 1 exercises
def classify_number(n):
    """Returns 'positive, even', etc."""
    if n == 0:
        return "zero"
    sign = "positive" if n > 0 else "negative"
    parity = "even" if n % 2 == 0 else "odd"
    return f"{sign}, {parity}"

def fizzbuzz(n):
    """Returns None with no crash, or Fizz/Buzz/FizzBuzz/n."""
    if not isinstance(n, int):
        return None
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)

def grade_stats(grades):
    """Returns a dict with min, max, average and passed."""
    if not grades:
        return {"min": None, "max": None, "average": None, "passed": []}
    return {
        "min": min(grades),
        "max": max(grades),
        "average": sum(grades) / len(grades),
        "passed": [g for g in grades if g >= 50]
    }


# F2: format_price
def format_price(amount, currency="JOD", decimals=2):
    """Returns formatted price string."""
    return f"{amount:.{decimals}f} {currency}"


# F3: min_max
def min_max(numbers):
    """Returns two values as a tuple (smallest, largest), without using min() or max()."""
    if not numbers:
        return (None, None)
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return (smallest, largest)


# F4: parse_year and calculate_age
def parse_year(text):
    """Returns an int or None."""
    try:
        return int(text)
    except (ValueError, TypeError):
        return None

def calculate_age(birth_year, current_year=2026):
    """Returns the age."""
    return current_year - birth_year


# F5: count_words and top_words
import string

def count_words(text):
    """The first function builds a word -> count dict."""
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_words(counts, n=3):
    """Returns the n most common words as a list of tuples, and calls nothing else."""
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n]


# F6: Scope drill

"""
Scope drill prediction:
total = 100
def add_bonus(amount):
    total = amount + 10  # This creates a local variable 'total', leaving global 'total' untouched.
    return total
result = add_bonus(5)
print(total, result)

Prediction: 100 15
Explanation: Without the 'global total' statement, assigning to 'total' inside 
the function creates a local variable. The global variable 'total' remains 100, 
and 'result' gets 15.
"""
total = 100
def add_bonus(amount):
    total = amount + 10
    return total

if __name__ == "__main__":
    print("=== Testing F1 to F5 ==->")
    print("classify_number(4):", classify_number(4))
    print("fizzbuzz(15):", fizzbuzz(15))
    print("grade_stats([40, 60, 80]):", grade_stats([40, 60, 80]))
    print("format_price(3, 'USD', 0):", format_price(3, "USD", 0))
    print("min_max([4, 1, 9]):", min_max([4, 1, 9]))
    print("parse_year('2000'):", parse_year("2000"))
    
    print("\n=== Testing F6 (Scope drill) ==->")
    result = add_bonus(5)
    print("Global total:", total)
    print("Function result:", result)
    print("Explanation: Inside add_bonus, assigning to 'total' creates a local variable 'total'. The global 'total' remains 100, while 'result' takes 15.")
