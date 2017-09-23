from core.gameobject import GameObject


class Area(GameObject):
    __slots__ = ["generated_levels", "generators"]

    def __init__(self):
        super().__init__()
        self.generated_levels = {}
        self.generators = {}

    def add_generator(self, generator, z_coordinate):
        self.generators[z_coordinate] = generator

    def get_level(self, z_coordinate):
        level = self.generated_levels.get(z_coordinate, None)
        if level:
            return level

        generator = self.generators.get(z_coordinate, None)
        if generator:
            level = generator.generate()
            self.generated_levels[z_coordinate] = level
            return level

        raise Exception("No levels defined for level {}".format(z_coordinate))
