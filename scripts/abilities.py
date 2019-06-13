import random

def ability_roll():
    total = -6
    min_roll = 6
    for _ in xrange(4):
        roll = random.randint(1, 6)
        if (roll < min_roll):
            total += min_roll
            min_roll = roll
        else:
            total += roll
    return total

scores = []
for _ in xrange(6):
    scores.append(ability_roll())
print(" ".join(str(x) for x in scores))
print("Sum: %s" % sum(scores))
