# # class Invoice: #class are object of data and function within them 

# #     def greeting(self):    # when using classes you need to have self in the pram()
# #         return 'Hi there'


# # # Instasation (check spelling)
# # inv_one = Invoice()
# # print(inv_one.greeting())

# # inv_two = Invoice()
# # print(inv_two.greeting())
# # ever thing in python is a object and you needed to class them

# class Invoice:

#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100)
# snapchat = Invoice('SnapChat', 200)

# print(google.formatter())



# #####Property#####

# class Invoice:

#     def __init__(self, client, total):
#         self._client = client
#         self._total = total

#     def formatter(self):
#         return f'{self._client} owes: ${self._total}'

#     @property
#     def client(self):
#         return self._client

#     @client.setter
#     def client(self, client):
#         self._client = client

#     @property
#     def total(self):
#         return self._total

# google = Invoice('Google', 100)

# print(google.client)

# google.client = 'Yahoo'

# print(google.client)

# ########## dunder __str__ ########

# class Invoice:
#   def __str__(self):
#     return "This is the invoice class!"


# inv = Invoice()
# print(str(inv))

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self):
#     return f"Invoice from {self.client} for {self.total}"


# inv = Invoice('Google', 500)
# print(str(inv))

# ####### Dunder methods in python __repr__########


# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self):
#     return f"Invoice from {self.client} for {self.total}"

#   def __repr__(self):
#     return f"Invoice({self.client}, {self.total})"


# inv = Invoice('Google', 500)
# print(str(inv))
# print(repr(inv))

# ####### how to buil a custom iterator class in python######

# class Lineup:
#     def __init__(self, players):
#         self.players = players
#         self.last_player_index = (len(self.players) - 1)

#     def __iter__(self):
#         self.n = 0
#         return self

#     def get_player(self, n):
#         return self.players[n]

#     def __next__(self):
#         if self.n < self.last_player_index:
#             player = self.get_player(self.n)
#             self.n += 1
#             return player
#         elif self.n == self.last_player_index:
#             player = self.get_player(self.n)
#             self.n = 0
#             return player


# astros = [
#   'Springer',
#   'Bregman',
#   'Altuve',
#   'Correa',
#   'Reddick',
#   'Gonzalez',
#   'McCann',
#   'Davis',
#   'Tucker'
# ]

# astros_lineup = Lineup(astros)
# process = iter(astros_lineup)

# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))



# ###### Iterators vs Generators ######


# class InfiniteLineup:
#     def __init__(self, players):
#         self.players = players

#     def lineup(self):
#         lineup_max = len(self.players)
#         idx = 0

#         while True:
#             if idx < lineup_max:
#                 yield self.players[idx]
#             else:
#                 idx = 0
#                 yield self.players[idx]

#             idx += 1

#     def __repr__(self):
#         return f'InfiniteLineup({self.players})'

#     def __str__(self):
#         return f"InfiniteLineup with the players: {', '.join(self.players)}"


# astros = [
#   'Springer',
#   'Bregman',
#   'Altuve',
#   'Correa',
#   'Reddick',
#   'Gonzalez',
#   'McCann',
#   'Davis',
#   'Tucker'
# ]

# full_lineup = InfiniteLineup(astros)
# astros_lineup = full_lineup.lineup()

# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))
# print(next(astros_lineup))

# print(repr(full_lineup))

# print(str(full_lineup))



##### class vs Instance attributes##############
"""And so the difference between a class attribute and an instance attribute really comes down to the name, I think it was named very well, a class attribute is an attribute that belongs to the class definition. So it's hardcoded directly into the class and then you can call it whenever you need it."""



class Website:     # this is a instance attribute
  def __init__(self, title):
    self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)


class DifferentWebsite:    # this is a class attribute
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)