from core.actions.base import Action
from services import echo
from services.selection import TargetSelectionSet
from services.selection.characterclasses import CharacterClasses
from services.selection.filters.unusedcharacterclasses import (
    PossibleCharacterClass
)
from services.selection.filters.listfilter import SingleListBased
from core.components.character_class import CharacterClass
from core.actions.listing import register


@register
class AddClass(Action):
    id = "add_class"
    """
    Special Action triggered Internally.
    Allows adding a Class to a character.
    Made for Racial Classes
    """
    target_selection = TargetSelectionSet(
        selections=CharacterClasses,
        filters=(PossibleCharacterClass, SingleListBased),
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        selected_class = target_selection[0]
        if character.character_class:
            character.character_class.add_class(selected_class)
            character.experience.evaluate_level_tables()
            character.experience.level_up()
        else:
            character.register_component(CharacterClass(selected_class))

        echo.player_echo(
            actor=character,
            message="You begin learning the path of {}!".format(
                selected_class.name)
        )

        return True
