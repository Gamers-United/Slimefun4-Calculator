from ingredient import Ingredient
from globalvar import gameRecipes, phase
import typing


class Recipe:
    def __init__(self, ingredients: [], product: Ingredient, process_host: str,
                 is_shaped: bool = False, shaped_recipe=None):
        self.input: typing.List[Ingredient] = ingredients
        self.output: Ingredient = product
        self.process_host: str = process_host
        self.is_shaped = is_shaped
        self.shaped_recipe = shaped_recipe
        if phase == "SETUP":
            gameRecipes[self.output] = self

    def resolveShapedRecipe(self):
        if self.is_shaped:
            output = "["
            for col in self.shaped_recipe:
                coltext = ""
                for item in col:
                    if item is None:
                        coltext += "Air"
                    else:
                        coltext += item.name
                    coltext += ", "
                output += coltext[:-2]
                output += "], ["
            return output[:-3]
        else:
            return None

    def __str__(self):
        input_string = ""
        for item in self.input:
            input_string += f"(Name: {item.name}, IsBase: {item.is_base}, Qty: {item.qty}), "
        output_string = f"(Name: {self.output.name}, IsBase: {self.output.is_base}, Qty: {self.output.qty}), "

        return f"[Inputs: {input_string}Output: {output_string}Process Host: {self.process_host}," \
               f"Shaped: {self.is_shaped}, Shaped Recipe: {self.resolveShapedRecipe()}] "

    def prettyPrint(self) -> str:
        input_string = ""
        for item in self.input:
            input_string += f"[{item.name}:{item.qty}], "
        output_string = f"[{self.output.name}:{self.output.qty}]"
        if self.is_shaped:
            return f"Pattern ({self.resolveShapedRecipe()}) in {self.process_host} makes {output_string}"
        else:
            return f"({input_string[:-2]}) in {self.process_host} makes {output_string}"

