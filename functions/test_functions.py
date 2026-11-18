
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from exercises import (
    classify_number, fizzbuzz, grade_stats, 
    format_price, min_max, parse_year, 
    calculate_age, count_words, top_words
)

# --- (sertions) ---
assert classify_number(4) == "positive, even"
assert classify_number(-3) == "negative, odd"
assert classify_number("abc") is None

assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(3) == "Fizz"
assert fizzbuzz(5) == "Buzz"
assert fizzbuzz(7) == "7"
assert fizzbuzz("abc") is None

assert grade_stats([60, 70, 80]) == {"min": 60, "max": 80, "average": 70.0, "passed": [60, 70, 80]}
assert grade_stats([40, 45]) == {"min": 40, "max": 45, "average": 42.5, "passed": []}
assert grade_stats([]) == {"min": None, "max": None, "average": None, "passed": []}

# fixed  format_price: normal, edge, invalid
assert format_price(12.5, "JOD", 2) == "12.50 JOD"
assert format_price(3, "USD", 0) == "3 USD"
assert format_price(0, "USD", 2) == "0.00 USD"
assert format_price("abc", "USD", 2) is None


assert min_max([4, 1, 9]) == (1, 9)
assert min_max([7]) == (7, 7)
assert min_max([]) == (None, None)

# fixed  parse_year: normal, edge, invalid
assert parse_year("2000") == 2000
assert parse_year("2026") == 2026
assert parse_year("-50") is None
assert parse_year("3000") is None

# fixed  calculate_age: normal, edge, invalid
assert calculate_age(2000, 2026) == 26
assert calculate_age(2026, 2026) == 0
assert calculate_age(2030, 2026) is None


text_sample = "Hello world, hello Python!"
counts = count_words(text_sample)
assert counts.get("hello") == 2
assert counts.get("python") == 1
assert count_words("") == {}
assert count_words(123) is None

# fixed  top_words: normal, edge, invalid
assert top_words(counts, 2)[0][0] == "hello"
assert top_words({}, 2) == []
assert top_words(counts, 0) == []
