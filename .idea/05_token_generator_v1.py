"""Component 3 (random tokens) v1
Generates random choice of token in random order"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]

# Testing loop to generate 20 tokens.
for item in range(20):
    token = random.choice(tokens)
    print(token) # can wrap output making it easier to screenshot