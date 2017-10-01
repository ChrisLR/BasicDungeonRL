class AttackResult(object):
    __slots__ = ["hits", "total_damage"]
    def __init__(self, hits, total_damage=0):
        self.hits = hits
        self.total_damage = total_damage
