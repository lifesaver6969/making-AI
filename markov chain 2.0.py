""" this version of markov chain can now genrate whole words from a single word prompt now the sentences genrated 
start to make more sence in turms of grammer tho they lack a clear subject and object orentation"""
import random
from collections import defaultdict


def build_model(text):
    model = defaultdict(list)
    for current, nxt in zip(text, text[1:]):
        model[current].append(nxt)
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
    return result


text = input("enter treaning data ")
start = input("enter one carector prompt ")

output = generate(text.lower().split(), start, 10)

if output is None:
    print(f"'{start}' treanning data not suffecent.")
else:
    print("Generated:")
    for i in range(len(output)):
        print(output[i],end = "")
        print(" ",end = "")