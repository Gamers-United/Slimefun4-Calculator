import data
from globalvar import gameRecipes, gameIngredients

class Solver:
    def __init__(self):
        self.solvables: [] = []
        self.ingredientTiersHolder: {{}} = {}
        self.craftableTiersHolder: {[]} = {}
        self.craftablePrintHolder = {}
        self.currentTier = 0

    def addSolvable(self, ingredientSolvable, qty: int):
        print(f"Solving for {qty} of {ingredientSolvable.name}")
        for item in range(0, qty):
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
        # Inject the first set of solvables if this is the first attempt at solving.
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
            try:
                print(f"Ingredients required by tier: {self.ingredientTiersHolder[i]}")
            except KeyError as e:
                print(f"No Ingredients for tier {i}")
            try:
                print(f"Crafts occuring in tier: ")
                for key in self.craftablePrintHolder[i]:
                    print(f"{key}:{self.craftablePrintHolder[i][key]}, ", end="")
                print("\n")
            except KeyError as e:
                print(f"No Crafts for tier {i}")

    def importUI(self, ui):
        data = []
        for row in range(ui.craftablesTable.model().rowCount()):
            data.append([])
            for column in range(ui.craftablesTable.model().columnCount()):
                index = ui.craftablesTable.model().index(row, column)
                data[row].append(str(ui.craftablesTable.model().data(index)))
        for row in data:
            #try:
                name = row[0]
                iStack = gameIngredients[name]
                self.addSolvable(iStack, int(row[1]))
            #except Exception as e:
                #print(e)
                #print("Ingredient was not valid")
        self.solve()
        self.printResult()

if __name__ == "__main__":
    a = Solver()
    a.addSolvable(data.carbon_chunk, 16)
    a.solve()
    a.printResult()