import random

from core.outfits import base_packages, starter_packages


class OutfitterService(object):
    @staticmethod
    def get_base_package(game_object):
        return random.choice([
            pack for pack in base_packages
            if pack.check_if_applicable(game_object)
        ])

    @staticmethod
    def get_starter_package(game_object):
        return random.choice([
            pack for pack in starter_packages
            if pack.check_if_applicable(game_object)
        ])

    @classmethod
    def outfit_starting_player(cls, game_object):
        packages = (cls.get_base_package(game_object),
                    cls.get_starter_package(game_object))

        for package in packages:
            package.apply(game_object)
