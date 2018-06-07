from bflib.characters.base import Character
from core import bodies, components, flags
from core.gameobject import GameObject
from core.gender import Gender
from core.displaypriority import DisplayPriority
from core.util.colors import Colors


class CharacterFactory(object):
    name = "character"
    type_map = Character
    _player_fg_color = Colors.WHITE
    _player_bg_color = Colors.BLACK
    _player_symbol = "@"
    _player_display_priority = DisplayPriority.Player

    def __init__(self, game):
        self.game = game

    def create_blank_player(self):
        new_character = GameObject(game=self.game, blocking=True)
        new_character.register_component(components.Location())
        new_character.register_component(components.Combat())
        new_character.register_component(components.Inventory())
        new_character.register_component(components.Effects())
        new_character.register_component(components.Vision(20))
        new_character.register_component(components.Player())
        new_character.register_component(components.Skills())
        new_character.register_component(components.Display(
            self._player_fg_color,
            self._player_bg_color,
            self._player_symbol,
            self._player_display_priority
        ))
        new_character.flags.add(flags.GameObjectFlags.Character)

        return new_character

    def set_attributes(self, character, ability_score_set):
        character.register_component(components.CharacterStats(ability_score_set))

    def set_classes(self, character, base_classes):
        character.register_component(components.CharacterClass(base_classes))
        character.register_component(components.Experience(base_classes))

    def set_race(self, character, base_race):
        character.register_component(components.Race(base_race))
        character.register_component(components.Body(assign_racial_body(base_race)))

    def finalize_character(self, character):
        character.register_component(components.Restrictions())
        character.register_component(components.Equipment())
        # TODO People will want to choose this
        character.register_component(components.Gender(Gender.Male))
        character.register_component(components.Money())
        character.register_component(components.Health(True))
        self.game.outfit.outfit_starting_player(character)


def assign_racial_body(base_race):
    # TODO This is lame, we will need a better long term solution.
    return bodies.HumanoidBody()
