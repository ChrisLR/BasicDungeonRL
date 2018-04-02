from core.actions.base import Action
from core.components.character_class import CharacterClass
from services.selection import TargetSelectionSet
from services.selection.characterclasses import CharacterClasses
from services.selection.filters.listfilter import SingleListBased
from services.selection.filters.unusedcharacterclasses import (
    PossibleCharacterClass
)


class AddClass(Action):
    name = "add_class"
    """
    Special Action triggered Internally.
    Allows adding a Class to a character.
    Made for Racial Classes
    """
    target_selection = TargetSelectionSet(
        selections=CharacterClasses,
        filters=(PossibleCharacterClass, SingleListBased),
    )

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        selected_class = target_selection[0]
        if character.character_class:
            character.character_class.add_class(selected_class)
            character.experience.evaluate_level_tables()
            character.experience.level_up()
        else:
            character.register_component(CharacterClass(selected_class))

        self.game.echo.player(
            actor=character,
            message="You begin learning the path of {}!".format(selected_class.name)
        )

        return True
