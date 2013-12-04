import sys
num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
    words = sys.stdin.readline().split()
    words.reverse()
    print("Case #" + str(case) + ":"," ".join(words))

