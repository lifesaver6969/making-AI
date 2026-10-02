"""this is a prototype of a markov chain currectly it takes only genrates 
one char in future i want it to be able to genrate whole words"""

import random
from collections import defaultdict


def build_model(text):
    text = text.lower()
    model = defaultdict(list)
    for current, nxt in zip(text, text[1:]):
        model[current].append(nxt)  # repeats keep the frequency weighting
    return model


def generate(text, start, count=10):
    model = build_model(text)
    current = start.lower()

    if current not in model:
        return None

    result = []
    for _ in range(count):
        followers = model.get(current)
        if not followers:
            current = random.choice(list(model))
            followers = model[current]
        current = random.choice(followers)
        result.append(current)
    return "".join(result)


text = input("enter treaning data ")
start = input("enter one carector prompt ")

if len(start) != 1:
    print("only one carector")
else:
    output = generate(text, start, 10)
    if output is None:
        print(f"'{start}' treanning data not suffecent.")
    else:
        print("Generated:", output)