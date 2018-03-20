from core.game.manager import Game
from core.coreobject import CoreObject
from core import factories

if __name__ == '__main__':
    core = CoreObject()
    core.create(Game)
    new_game = Game(core)
    factory = factories.Facade(core)
    system.game = new_game
    new_game.start()
