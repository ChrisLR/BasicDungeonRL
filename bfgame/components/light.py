from core.components import Component, listing


@listing.register
class Light(Component):
    NAME = "light"
    __slots__ = ["bright_light_radius", "dim_light_radius", "fuel",
                 "fuel_duration", "last_life_dice", "light_shape"]

    def __init__(self, bright_light_radius, dim_light_radius,
                 fuel, fuel_duration, last_life_dice, light_shape):
        super().__init__()
        self.bright_light_radius = bright_light_radius
        self.dim_light_radius = dim_light_radius
        self.fuel = fuel
        self.fuel_duration = fuel_duration
        self.last_life_dice = last_life_dice
        self.light_shape = light_shape

    def copy(self):
        return Light(
            self.bright_light_radius, self.dim_light_radius,
            self.fuel, self.fuel_duration, self.last_life_dice, self.light_shape)
