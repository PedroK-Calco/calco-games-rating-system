from tkinter import *
from service import PlayerService, MatchService
from popo import Player, Match


def _on_focus(e):
    e.widget.delete(0, END)


class GUI(Tk):
    def __init__(self, player_service: PlayerService, match_service: MatchService):
        super().__init__()
        self._player_ser: PlayerService = player_service
        self._match_ser: MatchService = match_service
        self._current_match: Match | None = None

        self.title("Pool Rating Test Interface")
        self.config(pady=20, padx=20)

        self._match_maker = Frame(master=self)
        Label(master=self._match_maker, text="Create a Match").grid(row=0, column=0, columnspan=2)

        self._player_1_entry = Entry(master=self._match_maker)
        self._player_1_entry.insert(0, "Player 1 ID")
        self._player_1_entry.bind("<FocusIn>", _on_focus)
        self._player_1_entry.grid(row=1, column=0)

        self._player_2_entry = Entry(master=self._match_maker)
        self._player_2_entry.insert(0, "Player 2 ID")
        self._player_2_entry.bind("<FocusIn>", _on_focus)
        self._player_2_entry.grid(row=1, column=1)

        Button(master=self._match_maker, text="Create Match", command=self._create_match).grid(row=2, column=0,
                                                                                               columnspan=2)

        self._match_maker.pack()

        self._match_finder = Frame(master=self)
        Label(master=self._match_finder, text="Find a Match").grid(row=0, column=0, columnspan=2)

        self._match_id_entry = Entry(master=self._match_finder)
        self._match_id_entry.insert(0, "Match ID")
        self._match_id_entry.bind("<FocusIn>", _on_focus)
        self._match_id_entry.grid(row=1, column=0, columnspan=2)

        Button(master=self._match_finder, text="Find Match", command=self._find_match).grid(row=2, column=0,
                                                                                            columnspan=2)

        self._match_finder.pack()

        self._match_ender = Frame(master=self)
        self._result = IntVar()
        Label(master=self._match_ender, text="End a Match").grid(row=0, column=0, columnspan=2)

        self._player_1_radio = Radiobutton(master=self._match_ender, text="Player 1", variable=self._result, value=1)
        self._player_1_radio.grid(row=1, column=0)

        self._player_2_radio = Radiobutton(master=self._match_ender, text="Player 2", variable=self._result, value=2)
        self._player_2_radio.grid(row=1, column=1)

        Button(master=self._match_ender, text="Submit results", command=self._end_match).grid(row=2, column=0,
                                                                                              columnspan=2)

        self._match_ender.pack()

    def _create_match(self):
        """
        Creates a match between two player id's inserted in the respective entry fields
        """
        player_1_id: int = int(self._player_1_entry.get())
        player_2_id: int = int(self._player_2_entry.get())

        player_1: Player = self._player_ser.get_player(player_1_id)
        player_2: Player = self._player_ser.get_player(player_2_id)

        self._match_ser.create_match(player_1, player_2)

        self._player_1_entry.insert(0, "Player 1 ID")
        self._player_2_entry.insert(0, "Player 2 ID")

    def _find_match(self):
        """
        Retrieves a Match object from the match repository and assigns it GUI's match attribute
        """
        match_id: int = int(self._match_id_entry.get())

        self._current_match = self._match_ser.get_match(match_id)
        self._player_1_radio.config(text=f"1: {self._current_match.player_one.name}")
        self._player_2_radio.config(text=f"2: {self._current_match.player_two.name}")

    def _end_match(self):
        """
        Finalizes a match by submitting a winning player to the match service.
        Then updates and stores the new player data to the database
        """
        if self._current_match is not None:
            winner_id: int = 0

            match self._result.get():
                case 1:
                    winner_id = self._current_match.player_one.user_id
                case 2:
                    winner_id = self._current_match.player_two.user_id

            new_player_data = self._match_ser.conclude_match(self._current_match, winner_id)

            for k, v in new_player_data.items():
                self._player_ser.update_player(k, v)

            self._player_ser.save_player_data()

            self._match_id_entry.delete(0, END)
            self._player_1_radio.config(text="Player 1")
            self._player_2_radio.config(text="Player 2")
