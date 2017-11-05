class Recipe(object):
    name = ""
    base_item_type = None
    depends_on = []

    @staticmethod
    def build_components(item_type):
        pass
