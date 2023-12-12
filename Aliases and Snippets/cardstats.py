embed <drac2>
deck = load_json(get_svar("cardStats"))
if len(deck) == 0:
  deck = [
    "3:hearts: `3 of hearts`",
    "4:diamonds: `4 of diamonds`",
    "5:hearts: `5 of hearts`",
    "5:diamonds: `5 of diamonds`",
    "6:clubs: `6 of clubs`",
    "6:spades: `6 of spades`",
    "7:hearts: `7 of hearts`",
    "7:diamonds: `7 of diamonds`",
    "8:clubs: `8 of spades`",
    "8:hearts: `8 of hearts`",
    "9:diamonds: `9 of diamonds`",
    "9:clubs: `9 of clubs`"
  ]

card_results= []
while len(card_results)<12:  # draw 12 cards (6 pairs)
  card = randchoice(deck)  # grab a random card from the deck
  card_results.append(card)  # add it to our list
  deck.remove(card)  # remove it from the deck

desc = """ -desc "Drawing cards..." """

i = 0 
while i < 12:
  desc += f"""-f "__Pair {i//2+1}__|{card_results[i]}\n{card_results[i+1]} \nTotal: {int(card_results[i][0]) + int(card_results[i+1][0])}|inline" """
  i += 2

return f""" -title "Generating Attributes..." {desc} -f "|You can switch any two cards, once, then assign to ability scores in any order. Signature: "{str(signature())} """

</drac2>
