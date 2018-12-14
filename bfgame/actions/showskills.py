from bfgame.actions.base import Action
from scenes.showskills import ShowSkillsScene


class ShowSkills(Action):
    name = "show_skills"
    """
    Show Skills
    """
    target_selection = None

    def can_execute(self, character, target_selection=None):
        return True

    def execute(self, character, target_selection=None):
        self.game.director.push_scene(ShowSkillsScene(self.game))

        return True
