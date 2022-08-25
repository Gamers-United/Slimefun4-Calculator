from typing import Optional
from globalvar import gameIngredients
import copy

class Ingredient:
    def __init__(self, name: str, is_base: bool = False, qty: int = 1):
        """Name in format minecraft:dirt"""
        self.name: str = name
        self.is_base: bool = is_base
        self.recipe: Optional[Recipe] = None
        self.qty = qty
        gameIngredients[self.name] = self
    
    def addRecipe(self, ingredients: [], qty: int, process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        self.recipe = Recipe(ingredients, self, qty, process_host)
        return self
    
    def addShapedRecipe(self, ingredients: [], qty: int, shaped_recipe, process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        self.recipe = Recipe(ingredients, self, qty, process_host, is_shaped=True, shaped_recipe=shaped_recipe)
        return self

    def getQty(self, qty: int):
        a = copy.deepcopy(self)
        a.qty = qty
        return a

    def craft(self, ingredientList: {}, craftables: []):
        if (self.is_base):
            try:
                ingredientList[self.name] += float(self.qty)
            except KeyError:
                ingredientList[self.name] = float(self.qty)
            craftables.append(self)
        else:
            if (self.recipe != None):
                if (self.recipe.output == self):
                    factor = float(self.qty) / float(self.recipe.output_qty)
                    for item in self.recipe.input:
                        try:
                            ingredientList[item.name] += float(item.qty)*factor
                        except KeyError as e:
                            ingredientList[item.name] = float(item.qty)*factor
                        craftables.append(item.getQty(factor*item.qty))
                else:
                    print(f"Error in Ingredient {self.name}, recipe does not produce Ingredient specified")
            else:
                print(f"Error in Ingredient {self.name}, missing Recipe and is not base")