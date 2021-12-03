from TicTacGame import TicTacGame
from TicTacSettings import TicTacSettings

while 1:
    settings = TicTacSettings()
    settings.set_user_settings()
    default_game = TicTacGame(settings)
    default_game.play_once()
