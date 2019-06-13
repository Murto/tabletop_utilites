import math
import sys

def inflate(gold):
  return (gold + 1) * math.log(gold + 1)

assert (len(sys.argv) > 1), "An amount of gold must be given"
gold = float(sys.argv[1])
print("Inflated gold: %.2f" % inflate(gold))
