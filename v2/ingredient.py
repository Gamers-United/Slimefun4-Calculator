from typing import Optional
import globalvar
import copy
import exceptions


class Ingredient:
    def __init__(self, name: str, is_base: bool = False, qty=1.0):
        """Name in format minecraft:dirt"""
        if ":" in name:
            self.name: str = name
        else:
            self.name: str = globalvar.game + ":" + name
        self.is_base: bool = is_base
        self.recipe = None
        self.qty = float(qty)
        self.gather_type: Optional[str] = None
        self.description: Optional[str] = None
        globalvar.gameIngredients[self.name] = self

    def addRecipe(self, ingredients: [], qty=1, process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        self.recipe = Recipe(ingredients, self, qty, process_host)
        return self

    def addShapedRecipe(self, shaped_recipe: [], qty=1, process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        ingredients = []
        ingredientHolder = {}
        for row in shaped_recipe:  # shaped_recipe: [[]], row: [compressedCarbon, compressedCarbon, compressedCarbon]
            for item in row:  # item is compressedCarbon
                if (item is not None):
                    try:
                        ingredientHolder[item.name] += item.qty
                    except KeyError:
                        ingredientHolder[item.name] = item.qty
        for key in ingredientHolder:
            ingredients.append(globalvar.gameIngredients[key].getQty(float(ingredientHolder[key])))
        self.recipe = Recipe(ingredients, self, qty, process_host, is_shaped=True, shaped_recipe=shaped_recipe)
        return self

    def getQty(self, qty: float):
        a = copy.deepcopy(self)
        a.qty = qty
        return a

    def craft(self, ingredientList: {}, craftables: []):
        if self.is_base:
            try:
                ingredientList[self.name] += float(self.qty)
            except KeyError:
                ingredientList[self.name] = float(self.qty)
            craftables.append(self)
        else:
            if self.recipe is not None:
                if self.recipe.output == self:
                    factor = float(self.qty) / float(self.recipe.output_qty)
                    for item in self.recipe.input:
                        try:
                            ingredientList[item.name] += float(item.qty) * factor
                        except KeyError:
                            ingredientList[item.name] = float(item.qty) * factor
                        craftables.append(item.getQty(factor * item.qty))
                else:
                    print(f"Error in Ingredient {self.name}, recipe does not produce Ingredient specified")
            else:
                print(f"Error in Ingredient {self.name}, missing Recipe and is not base")

    def addAcquisitionDescriptor(self, gather_type, description):
        if not self.is_base:
            raise exceptions.AcquisitionWrongType()
        else:
            self.gather_type = gather_type
            self.description = description

    def __str__(self):
        return f"(Name: {self.name}, IsBase: {self.is_base}, Qty: {self.qty}, Recipe: {str(self.recipe)}"
