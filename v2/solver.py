from dataclasses import replace
import data
from globalvar import gameRecipes, gameIngredients

class Solver:
    def __init__(self):
        self.solvables: [] = []
        self.ingredientTiersHolder: {{}} = {}
        self.craftableTiersHolder: {[]} = {}
        self.craftablePrintHolder = {}
        self.currentTier = 0

    def addSolvable(self, ingredientSolvable):
        self.solvables.append(ingredientSolvable)

    def checkFurtherSolvable(self) -> bool:
        state = False
        for item in self.craftableTiersHolder[self.currentTier]:
            if (item.is_base):
                continue
            else:
                state = True
        return state

    def solve(self):
        self.craftableTiersHolder[0] = []
        self.craftableTiersHolder[0].extend(self.solvables)
        worktodo = True
        while(worktodo):
            self.ingredientTiersHolder[self.currentTier+1] = {}
            self.craftableTiersHolder[self.currentTier+1] = []
            self.craftablePrintHolder[self.currentTier] = {}
            for item in self.craftableTiersHolder[self.currentTier]:
                item.craft(self.ingredientTiersHolder[self.currentTier+1], self.craftableTiersHolder[self.currentTier+1])
                try:
                    self.craftablePrintHolder[self.currentTier][item.name] = float(self.craftablePrintHolder[self.currentTier][item.name]) + float(item.qty)
                except KeyError:
                    self.craftablePrintHolder[self.currentTier][item.name] = float(item.qty)
            worktodo = self.checkFurtherSolvable()
            self.currentTier += 1

    def printResult(self):
        highest = self.currentTier
        for i in range(0, highest):
            print(f"----{i}----")
            try:
                print(f"Ingredients required by layer: {self.ingredientTiersHolder[i]}")
            except KeyError as e:
                print(f"No Ingredients for layer {i}")
            try:
                print(f"Crafts occuring in layer: {self.craftablePrintHolder[i]}")
            except KeyError as e:
                print(f"No Crafts for layer {i}")

    def importUI(self, ui):
        data = []
        for row in range(ui.craftablesTable.model().rowCount()):
            itemindex = ui.craftablesTable.model().index(row, 0)
            item = (str(ui.craftablesTable.model().data(itemindex)))
            qtyindex = ui.craftablesTable.model().index(row, 1)
            qty = (str(ui.craftablesTable.model().data(qtyindex)))
            data.append([item, qty])
        for row in data:
            try:
                name = row[0].lower().replace(' ','_').replace('slimefun:','slimefun4:')
                if name.find("slimefun4:") != -1 or name.find("minecraft:") != -1:
                    pass
                else:
                    name = "slimefun4:"+name
                iStack = gameIngredients[name]
                self.addSolvable(iStack.getQty(row[1]))
            except Exception as e:
                print("Ingredient in table was null or not valid.")
        self.solve()
        self.printResult()

    def printSolvable(self):
        for item in self.solvables:
            print(str(item))

if __name__ == "__main__":
    a = Solver()
    a.addSolvable(data.carbon_chunk.getQty(16))
    a.printSolvable()
    a.solve()
    a.printResult()