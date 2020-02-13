
#########################################
##### Name: Jiaxin Lou              #####
##### Uniqname: loujiax             #####
#########################################


import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")
        
    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")
        
    def test_3_str(self):
        card = cards.Card(3,13)
        self.assertEqual(card.__str__(), "King of Spades")
        
    def test_4_deck(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)
        
    def test_5_deal(self):
        deck = cards.Deck()
        cardinstance = []
        for i in deck.cards:
            cardinstance.append(i.__str__())
        self.assertTrue(str(deck.deal_card()) in cardinstance)
        
    def test_6_deal_fewer(self):
        deck = cards.Deck()
        old_len = len(deck.cards)
        deck.deal_card()
        new_len = len(deck.cards)
        self.assertEqual(old_len-1, new_len)
        
    def test_7_replace_more(self):
        deck = cards.Deck()
        the_card = deck.deal_card()
        old_len = len(deck.cards)
        deck.replace_card(the_card)
        new_len = len(deck.cards)
        self.assertEqual(old_len+1, new_len)
        
    def test_8_replace_not_affected(self):
        deck = cards.Deck()
        the_card = deck.deal_card() # remove a card
        deck.replace_card(the_card) # insert the card
        old_len = len(deck.cards)  #count the card number
        deck.replace_card(the_card) # insert the card again
        new_len = len(deck.cards) # count the card number after replace_card
        self.assertEqual(old_len, new_len)
        

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
