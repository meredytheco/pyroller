from collections import OrderedDict
from .. import prepare

class CasinoPlayer(object):
    """Class to represent the player/user. A new
    CasinoPlayer will be instantiated each time the
    program launches. Passing a stats dict to __init__
    allows persistence of player statistics between
    sessions."""

    def __init__(self, stats=None):
        self.stats = OrderedDict([("cash", prepare.MONEY),
                                             ("Blackjack", OrderedDict(
                                                    [("games played", 0),
                                                    ("hands played", 0),
                                                    ("hands won", 0),
                                                    ("hands lost", 0),
                                                    ("blackjacks", 0),
                                                    ("pushes", 0),
                                                    ("busts", 0),
                                                    ("total bets", 0),
                                                    ("total winnings", 0)])),
                                             ("Craps", OrderedDict(
                                                    [('times as shooter', 0),
                                                     ('bets placed', 0),
                                                     ('bets won', 0),
                                                     ('bets lost', 0),
                                                     ('total bets', 0),
                                                     ('total winnings', 0)])),
                                             ("Bingo", OrderedDict(
                                                    [("games played", 0),
                                                    ("cards won", 0),
                                                    ("cards lost", 0),
                                                    ("total bets", 0),
                                                    ("total winnings", 0),
                                                    ("time played", 0),
                                                    ("_last squares", [])])),
                                             ("Keno", OrderedDict(
                                                    [("games played", 0)])),
                                             ("Video Poker", OrderedDict(
                                                    [("games played", 0)])),
                                             ("Pachinko", OrderedDict(
                                                    [('games played', 0),
                                                    ('total winnings', 0),
                                                    ('earned', 0),
                                                    ('jackpots', 0),
                                                    ('gutters', 0),
                                                    ]))
                                            ])

        if stats is not None:
            self.stats["cash"] = stats["cash"]
            for game in self.stats:
                if game != "cash":
                    for stat, default in self.stats[game].items():
                        self.stats[game][stat] = stats[game].get(stat, default)



