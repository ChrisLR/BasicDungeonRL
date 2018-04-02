from bflib.characters.base import Character
from core import components, flags
from core.gameobject import GameObject


class CharacterFactory(object):
    name = "character"
    type_map = Character

    def __init__(self, game):
        self.game = game

    def create_new(self, ability_score_set, base_classes, base_race, name,
                   symbol, fg_color, bg_color, display_priority=0):
        new_character = GameObject(game=self.game, blocking=True, name=name)
        new_character.register_component(
            components.CharacterStats(ability_score_set))
        new_character.register_component(
            components.CharacterClass(*base_classes))
        new_character.register_component(components.Race(base_race))
        new_character.register_component(components.Restrictions(
            base_race.restriction_set,
            *(base_class.restriction_set for base_class
              in new_character.character_class.base_classes)
        ))
        new_character.register_component(components.Equipment(
            wear_locations=new_character.race.base_race.wear_locations,
            wield_locations=new_character.race.base_race.wield_locations,
            armor_restrictions=new_character.restrictions.armor,
            weapon_restrictions=new_character.restrictions.weapons,
            weapon_size_restrictions=new_character.restrictions.weapon_size
        ))
        new_character.register_component(
            components.Experience(new_character.character_class.base_classes)
        )
        new_character.register_component(components.Money())
        new_character.register_component(components.Location())
        new_character.register_component(
            components.Display(fg_color, bg_color, symbol, display_priority))
        new_character.register_component(components.Health(True))
        new_character.register_component(components.Combat())
        new_character.register_component(components.Inventory())
        new_character.register_component(components.Vision(20))
        new_character.register_component(components.Effects())

        self.game.outfit.outfit_starting_player(new_character)

        new_character.flags.add(flags.GameObjectFlags.Character)

        return new_character
