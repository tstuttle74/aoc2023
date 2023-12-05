lines = list(open('day4-input.txt'))

matches = []
for line in lines:
    parts = line.split(':')
    num_lists = parts[1].split('|')

    def num_set(num_str):
        return set([int(num) for num in num_str.strip().split()])

    winners = num_set(num_lists[0])
    my_numbers = num_set(num_lists[1])
    matches.append(len(winners & my_numbers))


def pts(m):
    return 0 if m == 0 else 1 if m == 1 else 2 * pts(m - 1)


pts_list = [pts(m) for m in matches]
# part 1
# correct answer: 23441
print('sum of pts', sum(pts_list))

# part 2
card_pts = []
# add indexes to matches
for i, m in enumerate(matches):
    card_pts.append((i, m))
# holds counts of each card
card_counts = [0] * len(card_pts)
# initialize stack w/ all cards
stack = list(card_pts)
# process stack
while len(stack):
    # get a card index and matches
    card_index, card_match = stack.pop()
    if card_match:
        offset = card_index + 1
        card_copies = card_pts[offset: offset + card_match]
        # add card copies to stack
        stack.extend(card_copies)
    # increment card count
    card_counts[card_index] += 1

print('sum of cards', sum(card_counts))