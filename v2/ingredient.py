from typing import Optional
import globalvar
import copy
import exceptions


class Ingredient:
    def __init__(self, name: str, qty=1.0, base: bool = False):
        """Name in format minecraft:dirt"""
        self.factor = None
        if ":" in name:
            self.name: str = name
        else:
            self.name: str = globalvar.game + ":" + name
        self.is_base: bool = base
        self.recipe = None
        self.linkedInputs = []
        self.qty = float(qty)
        self.gather_type: Optional[str] = None
        self.gather_description: Optional[str] = None
        if globalvar.phase == "SETUP":
            globalvar.gameIngredients[self.name] = self

    def addRecipe(self, ingredients: [], process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        self.recipe = Recipe(ingredients, self, process_host)
        return self

    def addShapedRecipe(self, shaped_recipe: [], process_host: str = "minecraft:crafting_table"):
        from recipe import Recipe
        ingredients = []
        ingredientHolder = {}
        for row in shaped_recipe:  # shaped_recipe: [[]], row: [compressedCarbon, compressedCarbon, compressedCarbon]
            for item in row:  # item is compressedCarbon
                if item is not None:
                    try:
                        ingredientHolder[item.name] += item.qty
                    except KeyError:
                        ingredientHolder[item.name] = item.qty
        for key in ingredientHolder:
            ingredients.append(globalvar.gameIngredients[key].getQty(ingredientHolder[key]))
        self.recipe = Recipe(ingredients, self, process_host, is_shaped=True, shaped_recipe=shaped_recipe)
        return self

    def getQty(self, qty: float):
        a = copy.deepcopy(self)
        a.qty = float(qty)
        return a

    def craft(self, ingredientList: {}, craftables: []):
        if self.is_base:
            try:
                ingredientList[self.name] += float(self.qty)
            except KeyError:
                ingredientList[self.name] = float(self.qty)
            craftables.append(self)
            self.linkedInputs.append(self)
        else:
            if self.recipe is not None:
                recipe_output = globalvar.gameIngredients[self.name].recipe.output.qty
                self.factor = self.qty / recipe_output
                for item in self.recipe.input:
                    try:
                        ingredientList[item.name] += item.qty * self.factor
                    except KeyError:
                        ingredientList[item.name] = item.qty * self.factor
                    a = item.getQty(self.factor * item.qty)
                    craftables.append(a)
                    self.linkedInputs.append(a)
            else:
                print(f"Error in Ingredient {self.name}, missing Recipe and is not base")

    def addAcquisitionDescriptor(self, gather_type, description):
        if not self.is_base:
            raise exceptions.AcquisitionWrongType()
        else:
            self.gather_type = gather_type
            self.gather_description = description

    def __str__(self):
        return f"(Name: {self.name}, IsBase: {self.is_base}, Qty: {self.qty}, Recipe: {str(self.recipe)})"
