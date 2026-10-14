"""Beginner examples for searching and validating text with regex."""

import re


# A regular expression (regex) is a pattern used to find or work with text.
# The r"..." form creates a raw string, so backslashes reach the regex engine
# without Python treating them as escape sequences first.


# -----------------------------------------------------
# 1. Search for a word
# -----------------------------------------------------
message = "Python is fun to learn."
match = re.search(r"fun", message)

print("--- Search ---")
if match:
    print("Found:", match.group())
    print("Start and end positions:", match.span())


# -----------------------------------------------------
# 2. Common character patterns
# -----------------------------------------------------
text = "Call 555-1234 or 212-555-0198."
phone_pattern = r"\d{3}-\d{4}"
print("\n--- Find all matches ---")
print("Phone-like values:", re.findall(phone_pattern, text))

# Useful pattern pieces:
#   .       any character (except newline by default)
#   \d      a digit; \D means a non-digit
#   \w      a letter, digit, or underscore; \W means a non-word character
#   \s      whitespace; \S means non-whitespace
#   [abc]   one character from a, b, or c
#   [A-Z]   one uppercase English letter
#   ^       start of text; $ means end of text
#   *       zero or more; + means one or more; ? means optional
#   {3}     exactly three; {2,5} means between two and five


# -----------------------------------------------------
# 3. Capture groups
# -----------------------------------------------------
phone_text = "Contact: 415-555-0136"
phone_match = re.search(r"(\d{3})-(\d{3})-(\d{4})", phone_text)

print("\n--- Capture groups ---")
if phone_match:
    print("Whole phone number:", phone_match.group(0))
    print("Area code:", phone_match.group(1))
    print("Middle part:", phone_match.group(2))
    print("Last part:", phone_match.group(3))


# -----------------------------------------------------
# 4. Replace and split text
# -----------------------------------------------------
sentence = "Python   makes   coding easier"
clean_sentence = re.sub(r"\s+", " ", sentence)
words = re.split(r"\s+", clean_sentence)

print("\n--- Replace and split ---")
print("Cleaned sentence:", clean_sentence)
print("Words:", words)


# -----------------------------------------------------
# 5. Simple input validation
# -----------------------------------------------------
email = "learner@example.com"
# This beginner pattern checks a basic shape; it is not a complete email
# standard validator. Real email validation can require more detailed rules.
email_pattern = r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$"

print("\n--- Basic email-shaped text check ---")
if re.fullmatch(email_pattern, email):
    print(f"{email!r} matches the basic pattern.")
else:
    print(f"{email!r} does not match the basic pattern.")


# -----------------------------------------------------
# 6. Compiled patterns and case-insensitive matching
# -----------------------------------------------------
word_pattern = re.compile(r"python", re.IGNORECASE)
print("\n--- Compiled pattern ---")
for found_word in word_pattern.findall("Python, python, PYTHON"):
    print("Matched:", found_word)


# Choose a function based on the task:
# - re.search() finds the first match anywhere in text.
# - re.match() checks for a match only at the beginning.
# - re.fullmatch() checks that the entire text matches the pattern.
# - re.findall() returns all matching text as a list.
# - re.sub() replaces matching text.
# - re.split() splits text wherever the pattern matches.
