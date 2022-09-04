from ingredient import Ingredient
from globalvar import gameRecipes
import typing


class Recipe:
    def __init__(self, ingredients: [], product: Ingredient, product_qty: int, process_host: str,
                 is_shaped: bool = False, shaped_recipe=None):
        self.input: typing.List[Ingredient] = ingredients
        self.output: Ingredient = product
        self.process_host: str = process_host
        self.output_qty: int = product_qty
        self.is_shaped = is_shaped
        self.shaped_recipe = shaped_recipe
        gameRecipes[self.output] = self

    def resolveShapedRecipe(self):
        output = []
        for col in self.shaped_recipe:
            output.append([])
            colnum = self.shaped_recipe.index(col)
            for item in col:
                if item is not None:
                    output[colnum].append(item.name)
                else:
                    output[colnum].append("")

    def __str__(self):
        input_string = ""
        for item in self.input:
            input_string += f"(Name: {item.name}, IsBase: {item.is_base}, Qty: {item.qty}), "
        output_string = f"(Name: {self.output.name}, IsBase: {self.output.is_base}, Qty: {self.output.qty}), "

        return f"(Inputs: {input_string}, Output: {output_string}, Process Host: {self.process_host}," \
               f" Qty: {self.output_qty}, Shaped: {self.is_shaped}, Shaped Recipe: {self.resolveShapedRecipe()}) "
