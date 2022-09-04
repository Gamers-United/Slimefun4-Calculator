import data
from globalvar import gameIngredients


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
            if item.is_base:
                continue
            else:
                state = True
        return state

    def solve(self):
        self.craftableTiersHolder[0] = []
        self.craftableTiersHolder[0].extend(self.solvables)
        worktodo = True
        while worktodo:
            self.ingredientTiersHolder[self.currentTier + 1] = {}
            self.craftableTiersHolder[self.currentTier + 1] = []
            self.craftablePrintHolder[self.currentTier] = {}
            for item in self.craftableTiersHolder[self.currentTier]:
                item.craft(self.ingredientTiersHolder[self.currentTier + 1],
                           self.craftableTiersHolder[self.currentTier + 1])
                try:
                    self.craftablePrintHolder[self.currentTier][item.name] = float(
                        self.craftablePrintHolder[self.currentTier][item.name]) + float(item.qty)
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
                print(f"Crafts occurring in layer: {self.craftablePrintHolder[i]}")
            except KeyError as e:
                print(f"No Crafts for layer {i}")

    def importUI(self, ui):
        uidata = []
        for row in range(ui.craftablesTable.model().rowCount()):
            itemindex = ui.craftablesTable.model().index(row, 0)
            item = (str(ui.craftablesTable.model().data(itemindex)))
            qtyindex = ui.craftablesTable.model().index(row, 1)
            qty = (str(ui.craftablesTable.model().data(qtyindex)))
            uidata.append([item, qty])
        for row in uidata:
            try:
                name = row[0].lower().replace(' ', '_')
                iStack = gameIngredients[name]
                self.addSolvable(iStack.getQty(row[1]))
            except Exception:
                print("Ingredient in table was null or not valid.")
        self.solve()
        self.printResult()

    def printSolvable(self):
        for item in self.solvables:
            print(str(item))


if __name__ == "__main__":
    a = Solver()
    a.addSolvable(data.carbonChunk.getQty(16))
    a.printSolvable()
    a.solve()
    a.printResult()
