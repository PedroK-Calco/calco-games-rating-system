from tkinter import *
from service import PlayerService, MatchService
from popo import Player


class GUI(Tk):
    def __init__(self, player_service: PlayerService, match_service: MatchService):
        super().__init__()
        self._player_ser: PlayerService = player_service
        self._match_ser: MatchService = match_service
        self.title("Pool Rating Test Interface")
        self.config(pady=20, padx=20)

        self._match_maker = Frame(master=self)
        Label(master=self._match_maker, text="Create a Match").grid(row=0, column=0, columnspan=2)

        self._player_1_entry = Entry(master=self._match_maker)
        self._player_1_entry.insert(0, "Player 1 ID")
        self._player_1_entry.grid(row=1, column=0)

        self._player_2_entry = Entry(master=self._match_maker)
        self._player_2_entry.insert(0, "Player 2 ID")
        self._player_2_entry.grid(row=1, column=1)

        Button(master=self._match_maker, text="Create Match", command=self._create_match).grid(row=2, column=0, columnspan=2)

        self._match_maker.pack()

        self._match_ender = Frame(master=self)
        self._result = IntVar()
        Label(master=self._match_ender, text="End a Match").grid(row=0, column=0, columnspan=2)

        self._player_1_radio = Radiobutton(master=self._match_ender, text="Player 1", variable=self._result, value=1)
        self._player_1_radio.grid(row=1, column=0)

        self._player_2_radio = Radiobutton(master=self._match_ender, text="Player 2", variable=self._result, value=2)
        self._player_2_radio.grid(row=1, column=1)

        Button(master=self._match_ender, text="Submit results").grid(row=2, column=0, columnspan=2)

        self._match_ender.pack()

    def _create_match(self):
        player_1_id: int = int(self._player_1_entry.get())
        player_2_id: int = int(self._player_2_entry.get())

        player_1: Player = self._player_ser.get_player(player_1_id)
        player_2: Player = self._player_ser.get_player(player_2_id)

        self._match_ser.create_match(player_1, player_2)

    def _end_match(self):
        pass