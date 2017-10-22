from core.gameobject import GameObject
from core import components
from core.outfits.outfitter import OutfitterService


class CharacterFactory(object):
    @classmethod
    def create_new(cls, ability_score_set, base_classes, base_race, symbol, fg_color, bg_color, display_priority=0):
        new_character = GameObject()
        new_character.register_component(components.CharacterStats(ability_score_set))
        new_character.register_component(components.CharacterClass(*base_classes))
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
        new_character.register_component(components.Display(fg_color, bg_color, symbol, display_priority))
        new_character.register_component(components.Health(True))
        new_character.register_component(components.Combat())
        new_character.register_component(components.Inventory())

        OutfitterService.outfit_starting_player(new_character)

        return new_character
