from services.selection.filters.base import SelectionFilter


class PossibleCharacterClass(SelectionFilter):
    """
    Only includes possible character classes
    """

    def filter(self, targets):
        self.resolution = self.filter_class_choices(targets)

    def filter_class_choices(self, classes):
        race = self.executor.race.base_race
        ability_score_set = self.executor.stats.base_ability_score_set

        enabled_classes = []
        race_restriction_set = race.restriction_set
        for character_class in classes:
            class_restriction_set = character_class.restriction_set
            ability_restriction = class_restriction_set.ability_score
            if race_restriction_set.classes:
                if not race_restriction_set.classes.evaluate(character_class):
                    continue

            if ability_restriction:
                if not ability_restriction.evaluate(ability_score_set):
                    continue

            enabled_classes.append(character_class)

        return enabled_classes
