#  Copyright 2023 Macauley Lim xmachd@gmail.com
#  This code is licensed under GNU AFFERO GENERAL PUBLIC LICENSE v3.0.
#  A copy of this license should have been provided with the code download, if not see https://www.gnu.org/licenses/
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU AGPL v3.0 for more details.

import data
import globalvar
import plotly


class Solver:
    def __init__(self):
        self.sankeyFigure = None
        self.sankeyRepresentation = None
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
        phase = "SOLVING"
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
        self.__str__()

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
                if ":" not in name:
                    name = globalvar.game + name
                iStack = globalvar.gameIngredients[name]
                self.addSolvable(iStack.getQty(row[1]))
            except Exception:
                print("Ingredient in table was null or not valid.")
        self.solve()
        self.showSankey()

    def printSolvable(self):
        for item in self.solvables:
            print(str(item))

    def generateSankey(self):
        ingredients = []
        ingredientlabels = []
        linkSource = []
        linkTarget = []
        linkValue = []
        linkdata = []
        for t in range(0, self.currentTier):
            for i in self.craftableTiersHolder[t]:
                ingredients.append(i)
        for item in ingredients:
            ingredientlabels.append(item.name)
        for item in ingredients:
            for i in item.linkedInputs:
                if item.name != i.name:
                    linkSource.append(ingredientlabels.index(item.name))
                    linkTarget.append(ingredientlabels.index(i.name))
                    linkdata.append(str(item.recipe.prettyPrint()))
                    if i.is_base:
                        linkValue.append(i.qty)
                    else:
                        linkValue.append(i.factor)

        node = {
            "pad": 30,
            "thickness": 5,
            "line": {"color": "black", "width": 0},
            "label": ingredientlabels,
            "color": "black",
        }
        link = {
            "source": linkSource,
            "target": linkTarget,
            "value": linkValue,
            "customdata": linkdata,
            "hovertemplate": "Craft: %{source.label}<br />Recipe: %{customdata}"
        }
        self.sankeyRepresentation = plotly.graph_objs.Sankey(
            node=node, link=link
        )

    def generateFigure(self):
        if self.sankeyRepresentation is None:
            self.generateSankey()
        self.sankeyFigure = plotly.graph_objs.Figure(data=self.sankeyRepresentation)
        self.sankeyFigure.update_layout(title_text="Crafting Flowchart", font_size=14)

    def showSankey(self):
        if self.sankeyFigure is None:
            self.generateFigure()
        self.sankeyFigure.show(renderer="browser")

    def writeSankey(self, file: str):
        if self.sankeyFigure is None:
            self.generateFigure()
        self.sankeyFigure.write_html(file)

    def __str__(self):
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
        return ""

    def reset():
        globalvar.phase = "SETUP"


if __name__ == "__main__":
    a = Solver()
    a.addSolvable(data.carbonChunk.getQty(16))
    a.solve()
    a.showSankey()
