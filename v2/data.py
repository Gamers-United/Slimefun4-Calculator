from ingredient import Ingredient
from recipe import Recipe

# Base Ingredients (Minecraft)
flint = Ingredient("minecraft:flint", True)
gravel = Ingredient("minecraft:gravel", True)
sand = Ingredient("minecraft:sand", True)

redstone = Ingredient("minecraft:redstone", True)
coal = Ingredient("minecraft:coal", True)
lapislazuli = Ingredient("minecraft:lapis_lazuli", True)
ironingot = Ingredient("minecraft:iron_ingot", True)

netherrack = Ingredient("minecraft:netherrack", True)
netherquartz = Ingredient("minecraft:nether_quartz", True)

# Base Ingredients (Slimefun4)
golddust = Ingredient("slimefun4:gold_dust", True)

tindust = Ingredient("slimefun4:tin_dust", True)
tiningot = Ingredient("slimefun4:tin_ingot", True)

copperdust = Ingredient("slimefun4:copper_dust", True)
copperingot = Ingredient("slimefun4:copper_ingot", True)

silverdust = Ingredient("slimefun4:silver_dust", True)
silveringot = Ingredient("slimefun4:silver_ingot", True)

leaddust = Ingredient("slimefun4:lead_dust", True)
leadingot = Ingredient("slimefun4:lead_ingot", True)

irondust = Ingredient("slimefun4:iron_dust", True)

aluminumdust = Ingredient("slimefun4:aluminum_dust", True)
aluminumingot = Ingredient("slimefun4:aluminum_ingot", True)

stonechunk = Ingredient("slimefun4:stone_chunk", True)

# Minecraft Recipes (Level 1)
glass = Ingredient("minecraft:glass").addRecipe([sand], 1, "minecraft:furnace")

#Slimefun 4 Recipes (Level 1)
carbon = Ingredient("slimefun4:carbon").addRecipe([coal.getQty(8)], 1, "slimefun4:compressor")

#Slimefun 4 Recipes (Level 2)
compressed_carbon = Ingredient("slimefun4:compressed_carbon").addRecipe([carbon.getQty(4)], 1, "slimefun4:compressor")

#Slimefun 4 Recipes (Level 3)
carbon_chunk = Ingredient("slimefun4:carbon_chunk").addShapedRecipe([compressed_carbon.getQty(8),flint], 1, [[compressed_carbon, compressed_carbon, compressed_carbon], [compressed_carbon, flint, compressed_carbon], [compressed_carbon, compressed_carbon, compressed_carbon]], "slimefun4:crafting_table")