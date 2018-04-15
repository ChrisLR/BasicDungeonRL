from core.abilities import listing


class Facade(object):
    def __init__(self, game):
        self.game = game

    def get_ability_by_name(self, name):
        ability = listing.get_by_name(name)
        if ability is not None:
            return ability(self.game)
        return None

    def get_abilities(self):
        return [ability(self.game) for ability in listing.ability_listing]
