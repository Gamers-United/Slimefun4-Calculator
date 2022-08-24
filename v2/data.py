from ingredient import Ingredient
from recipe import Recipe

# Base Ingredients (Minecraft)
flint = Ingredient("flint", "minecraft", True)
gravel = Ingredient("gravel", "minecraft", True)
sand = Ingredient("sand", "minecraft", True)

redstone = Ingredient("redstone", "minecraft", True)
coal = Ingredient("coal", "minecraft", True)
lapislazuli = Ingredient("lapis_lazuli", "minecraft", True)
ironingot = Ingredient("iron_ingot", "minecraft", True)

netherrack = Ingredient("netherrack", "minecraft", True)
netherquartz = Ingredient("nether_quartz", "minecraft", True)

# Base Ingredients (Slimefun4)
golddust = Ingredient("gold_dust", "slimefun4", True)

tindust = Ingredient("tin_dust", "slimefun4", True)
tiningot = Ingredient("tin_ingot", "slimefun4", True)

copperdust = Ingredient("copper_dust", "slimefun4", True)
copperingot = Ingredient("copper_ingot", "slimefun4", True)

silverdust = Ingredient("silver_dust", "slimefun4", True)
silveringot = Ingredient("silver_ingot", "slimefun4", True)

leaddust = Ingredient("lead_dust", "slimefun4", True)
leadingot = Ingredient("lead_ingot", "slimefun4", True)

irondust = Ingredient("iron_dust", "slimefun4", True)

aluminumdust = Ingredient("aluminum_dust", "slimefun4", True)
aluminumingot = Ingredient("aluminum_ingot", "slimefun4", True)

stonechunk = Ingredient("stone_chunk", "slimefun4", True)

# Minecraft Recipes (Level 1)
glass = Ingredient("glass", "minecraft", False).addRecipe([sand], 1, "furnace")

#Slimefun 4 Recipes (Level 1)
carbon = Ingredient("carbon", "slimefun4", False).addRecipe([coal.getQty(8)], 1, "slimefun4:compressor")

#Slimefun 4 Recipes (Level 2)
compressed_carbon = Ingredient("compressed_carbon", "slimefun4", False).addRecipe([carbon.getQty(4)], 1, "slimefun4:compressor")

#Slimefun 4 Recipes (Level 3)
carbon_chunk = Ingredient("carbon_chunk", "slimefun4", False).addShapedRecipe([compressed_carbon.getQty(8),flint], 1, "slimefun4:crafting_table", [[compressed_carbon, compressed_carbon, compressed_carbon], [compressed_carbon, flint, compressed_carbon], [compressed_carbon, compressed_carbon, compressed_carbon]])