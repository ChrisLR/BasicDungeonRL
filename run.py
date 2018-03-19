from core.game.manager import Game
from core.system import System
from core import factories

if __name__ == '__main__':
    system = System()
    new_game = Game(system)
    factory = factories.Facade(system)
    system.game = new_game
    new_game.start()
