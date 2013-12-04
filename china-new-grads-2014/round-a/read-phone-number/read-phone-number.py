import sys
from itertools import groupby

rules = {1: "", 2: "double", 3: "triple",
    4: "quadruple", 5: "quintuple", 6: "sextuple",
    7: "septuple",  8: "octuple",   9: "nonuple",
    10: "decuple"}

digit2word = {1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    0: "zero"}


def encode(number):
  return [(len(list(g)), k) for k, g in groupby(number)]

def interpret_encoding(encoding):
  message = []
  for pair in encoding:
    count = pair[0]
    word = digit2word[pair[1]]
    if count > 1 and count < 11:
      message.extend([rules[count], word]) 
    else:
      message.extend([word] * count)
  return " ".join(message)


def interpret(number, number_format):
  accumulator = 0
  message = []
  for f in number_format:
    message.append(interpret_encoding(encode(number[accumulator:accumulator + f])))
    accumulator += f
  return " ".join(message)


num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
  number, format = map(str, sys.stdin.readline().split())
  number = list(map(int, list(number)))
  format = list(map(int, format.split('-')))
  print("Case #" + str(case) + ":", interpret(number, format))

