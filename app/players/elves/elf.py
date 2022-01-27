from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument):
        super(Elf, self).__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")