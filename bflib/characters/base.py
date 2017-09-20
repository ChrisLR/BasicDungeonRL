class Character(object):
    def __init__(self, name, ability_score_set, class_set, equipment_set, level_set,  money_set, race):
        self.name = name
        self.ability_score_set = ability_score_set
        self.class_set = class_set
        self.equipment_set = equipment_set
        self.level_set = level_set
        self.money_set = money_set
        self.race = race

    @property
    def armor_class(self):
        pass

    @property
    def attack_bonus(self):
        pass

    @property
    def hit_points(self):
        pass

    @property
    def saving_throws(self):
        pass
