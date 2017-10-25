recipes_mapping = {}


def register(recipe_type):
    if recipe_type.base_item_type in recipes_mapping:
        raise Exception("Recipe already registered for this base_item_type.")
    else:
        recipes_mapping[recipe_type.base_item_type] = recipe_type


def get_recipe(base_item_type):
    recipe = recipes_mapping.get(base_item_type, None)
    if recipe is None:
        return get_recipe(base_item_type.__bases__[0])
    return recipe
