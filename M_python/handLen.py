def handLen(hand):
    hand_length = 0
    for letter in hand:
        hand_length += hand[letter]
    
    return hand_length

print(handLen({"d":1, "g":3, "t":1, "u":1, "f":1, "o":1}))