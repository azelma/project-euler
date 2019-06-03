def rank_and_suit(card):
  return list(card)

def suit(card):
  return rank_and_suit(card)[1]

def rank(card):
  return rank_and_suit(card)[0]

def rank_score(card):
  current_rank= rank(card)
  if current_rank == 'A':
    return 14
  elif current_rank == 'K':
    return 13
  elif current_rank == 'Q':
    return 12
  elif current_rank == 'J':
    return 11
  elif current_rank == 'T':
    return 10
  else:
    return int(current_rank)

def same_suit(hand):
  first_suit = suit(hand[0])
  for card in hand:
    if suit(card) != first_suit:
      return False
  return True

def consecutive_values(hand):
    first_value = rank_score(hand[0])
    for i in range(1, 5):
        if rank_score(hand[i]) != first_value + i:
            return False
    return True

def rank_frequencies(hand):
    result = {}
    for card in hand:
        current_rank =  rank(card)
        if current_rank in result:
            result[current_rank] += 1
        else:
            result[current_rank] = 1
    return result

def hand_type(hand, frequencies):
  hand = sorted(hand, key=rank_score)
  if consecutive_values(hand):
    if same_suit(hand):
        if rank(hand[0]) == 'T':
            return 'royal_flush'
        else:
            return 'straight_flush'
    else:
        return 'straight'
  elif same_suit(hand):
      return 'flush'
  else:
      values = sorted(frequencies.values())
      if values == [1, 4]:
        return 'four_of_a_kind'
      elif values == [2, 3]:
        return 'full_house'
      elif values == [1, 1, 3]:
        return 'three_of_a_kind'
      elif values == [1, 2, 2]:
        return 'two_pairs'
      elif values == [1, 1, 1, 2]:
        return 'one_pair'
      else:
        return 'high_card'

def winning_hand(hands):
  hand_ranking = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind',
     'straight', 'flush', 'full_house', 'four_of_a_kind', 'straight_flush',
    'royal_flush']
  frequencies = [rank_frequencies(hands[0]), rank_frequencies(hands[1])]
  type_1 = hand_type(hands[0], frequencies[0])
  type_2 = hand_type(hands[1], frequencies[1])
  if hand_ranking.index(type_1) > hand_ranking.index(type_2):
    return hands[0]
  elif hand_ranking.index(type_1) < hand_ranking.index(type_2):
    return hands[1]
  else:
    sorted_hands = [sorted(hands[0], key=lambda x: rank_score(x) + frequencies[0][rank(x)] * 100), sorted(hands[1], key=lambda x: rank_score(x) + frequencies[1][rank(x)] * 100)]
    for i in range(1,5):
        if rank_score(sorted_hands[0][-i]) > rank_score(sorted_hands[1][-i]):
            return hands[0]
        elif rank_score(sorted_hands[0][-i]) < rank_score(sorted_hands[1][-i]):
            return hands[1]

count =  0

input = input.split("\n")
print len(input)
for hand in input:
    cards = hand.split(' ')
    player_1 = cards[:5]
    player_2 = cards[5:]
    if winning_hand([player_1, player_2]) == player_1:
        count += 1
print count
