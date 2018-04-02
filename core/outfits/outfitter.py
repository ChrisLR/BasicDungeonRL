import random

from core.outfits import base_packages, starter_packages


class OutfitterService(object):
    def __init__(self, game):
        self.game = game

    def get_base_package(self, game_object):
        return random.choice([
            pack for pack in base_packages
            if pack.check_if_applicable(game_object)
        ])

    def get_starter_package(self, game_object):
        choices = [
            pack for pack in starter_packages
            if pack.check_if_applicable(game_object)
        ]
        if choices:
            return random.choice(choices)
        return None

    def outfit_starting_player(self, game_object):
        packages = (self.get_base_package(game_object),
                    self.get_starter_package(game_object))

        for package in packages:
            if package is not None:
                package.apply(self.game, game_object)
