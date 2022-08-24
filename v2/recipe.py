from ingredient import Ingredient
from globalvar import gameRecipes

class Recipe:
    def __init__(self, ingredients: [], product: Ingredient, product_qty: int, process_host: str, is_shaped: bool = False, shaped_recipe = None):
        self.input: [Ingredient] = ingredients
        self.output: Ingredient = product
        self.process_host: str = process_host
        self.output_qty: int = product_qty
        self.is_shaped = is_shaped
        self.shaped_recipe = shaped_recipe
        gameRecipes[self.output] = self