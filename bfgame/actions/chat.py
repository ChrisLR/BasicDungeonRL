from core.actions.base import Action
from core.components import Talker
from scenes.game.dialog import DialogScene
from services.selection import DirectionalSelection, filters
from services.selection.base import TargetSelectionSet


class Chat(Action):
    name = "chat"
    target_selection = TargetSelectionSet(
        selections=DirectionalSelection,
        filters=filters.NotConscious
    )

    def __init__(self, game):
        super().__init__(game)

    def can_select(self, character):
        return True

    def can_execute(self, character, target_selection=None):
        if target_selection[0].dialog:
            return True
        character.game.echo.player(character, "This character has nothing to say.")
        return False

    def execute(self, character, target_selection=None):
        if not character.talker:
            character.register_component(Talker())

        self.game.director.push_scene(DialogScene(self.game, character, target_selection[0]))

        return True
