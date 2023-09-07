"""
Joe Ovenden
06/07/2020

A calculator designed for the game poker quest. 

In poker quest you have to battle various monsters in a turn based, playing cards combat
system. Each turn you, and the monster(s) get dealt a certain number of cards. To use
an attack, you have to cards that match some criteria.

Examples for criteria could be:
     Pair - You must use a pair of cards to use this attack
     Three of a kind - You must use three cards of the same rank to use this attack
     Cards adding up to X
     4 Cards of rank Q or higher
     etc.

This calculator estimates the odds of some criteria passing when dealt a certain number of
cards by dealing a large number of hands and counting how many of them pass the criteria.
"""
from copy import deepcopy
from random import randint
from math import log


class Card:
     ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
     suits = ["clubs","diamonds","hearts","spades"]
     def __init__(self, rank, suit):
          self.rank = rank
          self.suit = suit

     def get_value(self):
          # Returns integer value of card
          try:
               value = int(self.rank)
          except ValueError:
               if self.rank == "A":
                    value = 11
               else:
                    value = 10
          return value

     def display(self):
          print(self.rank, "of", self.suit)        # Prints rank and suit

     def get_index(self):
          return Card.ranks.index(self.rank)     # Returns index of rank within Card.ranks


class Deck:
     def __init__(self):
          self.make_fulldeck()
          self.reset()

     def reset(self):
          self.cards = deepcopy(self.full_deck)   # Resets cards in deck to a full deck

     def make_fulldeck(self):
          # Builds a full deck
          self.full_deck = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

     def display(self):
          print("---Displaying deck---")
          for card in self.cards:
               card.display()
          print("---------------------")


class Hand:
     def __init__(self):
          self.reset()

     def get_ranks(self):
          return [card.rank for card in self.cards]
     
     def get_values(self):
          return [card.get_value() for card in self.cards]

     def deal(self, deck, n):
          # Deals n cards from the deck to the hand
          deck_count = len(deck.cards)
          for i in range(n):
               position = randint(0, deck_count - 1)
               self.cards.append(deck.cards.pop(position))
               deck_count -= 1

     def reset(self):
          self.cards = []     # Empties the hand

     def display(self):       # Displays hand
          print("---Displaying hand---")
          for c in self.cards:
               c.display()
          print("---------------------")
          

class Program:
     def __init__(self):
          self.Main()

     def criteria_check(self, hand):
          # Checks hand against criteria and returns true if passes criteria, false otherwise
          success = self.check_n_of_a_kind(hand, 3)
          if self.print:
               hand.display()
               print(success)
          return success

     def check_n_of_a_kind(self, hand, n):
          # Checks if there is any three of a kind within the hand
          ranks_count = [hand.get_ranks().count(rank) for rank in Card.ranks]
          return max(ranks_count) >= n

     def check_sumToX(self, hand, X):
          # Checks if the values of the cards add up to X
          return sum(hand.get_values()) >= X

     def check_RankOrLower(self, hand, rank, n):
          # Checks if hand contains at least n or more cards of a certain rank of lower
          rank_index = Card.ranks.index(rank)
          count = sum(card.get_index() <= rank_index for card in hand.cards)
          return count >= n

     def check_RankOrHigher(self, hand, rank, n):
          # Checks if hand contains at least n or more cards of a certain rank of higher
          rank_index = Card.ranks.index(rank)
          count = sum(card.get_index() >= rank_index for card in hand.cards)
          return count >= n

     def display_results(self, success_count, trial_count):
          success_rate = round((success_count / trial_count) * 100, 1)
          print("Out of", trial_count, "trials,", success_count, "were a success.")
          print("This is a success rate of", str(success_rate) + "%.")
          
     def Main(self):
          # Prints out success rate after each number of trials in trial_printouts
          trial_printouts = [1000, 3000, 5000, 10000, 15000, 20000, 30000, 40000, 50000]
          deck = Deck()
          hand = Hand()
          trials = 50000
          self.print = False
          success_count = 0
          card_count = 7
          for i in range(trials):
               hand.deal(deck, card_count)
               if self.criteria_check(hand) is True:
                    success_count += 1
               deck.reset()
               hand.reset()
               if (i + 1) in trial_printouts:
                    self.display_results(success_count, i + 1)
     
if __name__ == "__main__":
     P = Program()
