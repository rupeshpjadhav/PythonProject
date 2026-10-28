# random module
# The random module generates random numbers and makes random choices.
# Useful for games, simulations, sampling data, and testing.
# The numbers are pseudo-random: they look random, but they come from a repeatable formula.
# For passwords or security tokens, use the secrets module instead.

import random

# Random integer between 1 and 100 (both ends included)
# randint(a, b) includes both a and b, unlike range(), which excludes its end value.
print(random.randint(1, 100))

# Random float between 0.0 and 1.0 (0.0 can appear, 1.0 never does)
print(random.random())

# Random float in a range
# uniform(a, b) returns a float between a and b.
print(random.uniform(1.5, 2.5))

# Choosing one item from a list
# choice() picks a single element at random from a non-empty sequence.
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Choosing several items (with or without repeats)
# choices() picks k items and allows the same item to appear more than once.
print(random.choices(fruits, k=5))          # repeats allowed
# sample() picks k different items. It never repeats an item, and k cannot be larger than the list.
print(random.sample(fruits, k=2))           # no repeats

# Shuffling a list in place
# shuffle() reorders the list itself and returns None. It does not return a new list.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Reproducible results with a seed
# seed() sets the starting point of the random number generator.
# The same seed always produces the same sequence, which helps with testing and debugging.
random.seed(42)
print(random.randint(1, 10))    # the same number every time this seed is used
random.seed(42)
print(random.randint(1, 10))    # same as above

# Simple dice game using random
# A function wraps the random logic so you can reuse it anywhere.
def roll_dice():
    return random.randint(1, 6)   # a six-sided die gives a number from 1 to 6

print("You rolled:", roll_dice())
