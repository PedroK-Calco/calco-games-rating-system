from presentation import GUI
from data import PlayerRepository, MatchRepository
from service import PlayerService, MatchService

player_repository: PlayerRepository = PlayerRepository()
player_service: PlayerService = PlayerService(player_repository)
match_repository: MatchRepository = MatchRepository(player_repository)
match_service: MatchService = MatchService(match_repository)

wn = GUI(player_service, match_service)

wn.mainloop()

