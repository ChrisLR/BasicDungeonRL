class MapPieceSpawn(object):
    __slots__ = ["chance", "map_piece", "spawn_limit"]

    def __init__(self, chance, map_piece, spawn_limit=None):
        self.chance = chance
        self.map_piece = map_piece
        self.spawn_limit = spawn_limit
