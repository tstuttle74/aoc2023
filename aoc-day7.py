import functools

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def hand_value(counts):
    card_counts = sorted(counts.values(), reverse=True)
    # 5 of kind, full house or four of a kind
    if len(counts) < 3:
        return card_counts[0] # 5, 4 or 3
    # 3 of a kind or two pair
    if len(counts) == 3:
        return card_counts[0] - 1 # 2 or 1
    # 1 pair or high card
    else:
        return card_counts[0] - 2 # 0  or -1

def higher_card(a, b):
    for i in range(5):
        if a[i] != b[i]:
            return cards.index(a[i]) - cards.index(b[i])
    return 0

def replace_jokers(counts):
    no_jokers = dict(counts)
    num_jokers = no_jokers.pop('J', None)
    if num_jokers is None:
        return counts
    elif num_jokers == 5:
        return {'A': 5}
    # sort the counts by value
    sorted_counts = sorted(no_jokers.items(), key=lambda x: x[1], reverse=True)
    # get the most frequent card
    most_freq_card = sorted_counts[0][0]
    # increment the most freq card by # of jokers
    no_jokers[most_freq_card] += num_jokers
    return no_jokers

def compare(a, b):
    [a_hand, _, a_count] = a
    [b_hand, _, b_count] = b
    # pt 1
    # a_val = hand_value(a_count)
    # b_val = hand_value(b_count)
    # pt 2
    a_val = hand_value(replace_jokers(a_count))
    b_val = hand_value(replace_jokers(b_count))
    if a_val == b_val:
        return higher_card(a_hand, b_hand)
    return a_val - b_val


lines = list(open('inputs/day7.txt'))
#lines = list(open('inputs/day7-sample-2.txt'))

hands = []
for line in lines:
    [hand, bid] = line.strip().split()
    hands.append((hand, bid, {}))

for hand, _, count in hands:
    for c in hand:
        count[c] = count.get(c, 0) + 1

sorted_hands = sorted(hands, key=functools.cmp_to_key(compare))
hand_power = [(i+1)*int(rank[1]) for i, rank in enumerate(sorted_hands)]
print(sum(hand_power))