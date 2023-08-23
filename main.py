from presentation import GUI

from service import *

player_service: PlayerService = PlayerService()
match_service: MatchService = MatchService()

wn = GUI(player_service, match_service)

wn.mainloop()

