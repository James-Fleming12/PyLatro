class PlayingCard:

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.suit} {self.rank}"

class TarotCard:

    def __init__(self, name: str, command: str):
        self.name = name
        self.command = command

    def __str__(self) -> str:
        return f"{self.name}"

class Joker:

    def __init__(self, name: str, price: int, command: str):
        self.name = name
        self.price = price
        self.command = command

    def __str__(self) -> str:
        return f"{self.name}"