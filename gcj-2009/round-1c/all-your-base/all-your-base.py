import sys

def translate(message):
    # Number of unique characters in message
    base = len(set(message))

    #Digit assignment priority [1, 0, 2, 3, ..., base-1]
    digits = [1, 0]
    digits.extend(list(range(2, base)))
    digits.reverse() # reverse so we can pop efficiently

    # Greedy algorithm to translate the message
    # As we encounter characters, assign all instances
    # of it in the string to the highest priority digit
    chars_seen = set()
    for char in message:
        if char in chars_seen:
            continue
        chars_seen.add(char)
        char_to_replace = digits.pop()
        message = [char_to_replace if x == char else x for x in message]

    # The aliens do not work in unary
    if base < 2:
        base = 2

    # Convert to the appropriate base to find the minimum # of seconds
    seconds = 0
    for digit in message: 
        seconds *= base
        seconds += int(digit)
    return seconds 

alien_messages = map(list,map(str,sys.stdin.read().split()[1:]))
case_number = 1
for message in alien_messages:
    print("Case #" + str(case_number) + ":", translate(message))
    case_number += 1

