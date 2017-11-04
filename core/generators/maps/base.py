class MapPiece(object):
    name = ""
    tiles = ""
    symbolic_links = {}
    spawn_ratios = tuple()

    @classmethod
    def write_tiles_level(cls, level, left_x, top_y):
        local_x = 0
        local_y = 0
        for line in cls.tiles.splitlines():
            for char in line:
                tile_link = cls.symbolic_links.get(char, None)
                if tile_link:
                    world_coordinates = (left_x + local_x, top_y + local_y)
                    level.add_tile(world_coordinates, tile_link)
                else:
                    raise Exception("Char {} has no link".format(char))
                local_x += 1
            local_x = 0
            local_y += 1

    @classmethod
    def get_width(cls):
        return max(cls.tiles.splitlines())

    @classmethod
    def get_height(cls):
        return len(cls.tiles.splitlines())
