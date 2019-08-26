from services.selection.base import Selection


class UsableAbilities(Selection):
    """
    This selects all abilities a character can use.
    """
    def resolve(self):
        abilities = set(type(ability) for ability in self.executor.query.special_ability())
        all_abilities = self.game.abilities.get_all_types()
        usable_abilities = (ability for ability in all_abilities
                            if ability.use_manually and ability.requires.issubset(abilities))

        self.resolution = sorted(usable_abilities, key=lambda ability: ability.name)
