def updateHand(hand, word):
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1

    return hand_copy

print(updateHand({"d":1, "g":1, "t":1, "u":1, "f":1, "o":1}, "dog"))
